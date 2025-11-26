import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from datetime import datetime

# Ajusta la ruta a tu usuario real
URL = r"file:///C:/Users/George S S R/Documents/GitHub/biblioteca-pruebas-selenium/app/index.html"


#   FUNCIONES HELPER

def hacer_login(driver):
    driver.get(URL)
    time.sleep(1)
    
    driver.find_element(By.ID, "usuario").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.ID, "btnLogin").click()
    time.sleep(2)
    # Redirección manual para asegurar dashboard
    driver.get("file:///C:/Users/George S S R/Documents/GitHub/biblioteca-pruebas-selenium/app/dashboard.html")
    time.sleep(2)


def agregar_libro(driver, titulo, autor, anio, estado):
    driver.find_element(By.ID, "titulo").send_keys(titulo)
    driver.find_element(By.ID, "autor").send_keys(autor)
    driver.find_element(By.ID, "anio").send_keys(str(anio))
    
    select = Select(driver.find_element(By.ID, "estado"))
    select.select_by_value(estado)
    
    driver.find_element(By.ID, "btnAgregar").click()
    time.sleep(1)

#   TEST 1: ELIMINAR ÚNICO LIBRO 

def test_eliminar_libro_exitoso(driver):
    """
    Agrega un libro, intenta eliminarlo, ACEPTA la alerta y verifica.
    """
    hacer_login(driver)
    driver.execute_script("localStorage.clear();")
    driver.refresh()
    time.sleep(1)

    # 1. Agregar libro
    agregar_libro(driver, "Libro a Borrar", "Autor X", 2024, "pendiente")

    # 2. Eliminar
    btn_eliminar = driver.find_element(By.XPATH, "//tbody[@id='booksTable']/tr[1]//button[contains(@class, 'btnEliminar')]")
    btn_eliminar.click()
    time.sleep(0.5) 

    # MANEJO DE ALERTA 
    alert = driver.switch_to.alert
    alert.accept() 
    time.sleep(1)

    # 4. Verificar que desapareció
    filas = driver.find_elements(By.XPATH, "//tbody[@id='booksTable']/tr")
    assert len(filas) == 0

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/eliminar_exitoso_{timestamp}.png")
    print("✓ Eliminar libro único (con alerta) - OK")

#   TEST 2: CANCELAR ELIMINACIÓN (NUEVO)

def test_cancelar_eliminacion(driver):
    """
    Prueba que al dar clic en 'Cancelar' en la alerta, el libro NO se borra.
    """
    hacer_login(driver)
    driver.execute_script("localStorage.clear();")
    driver.refresh()
    time.sleep(1)

    agregar_libro(driver, "Libro Salvado", "Autor Y", 2025, "leido")

    # Clic en Eliminar
    btn_eliminar = driver.find_element(By.XPATH, "//tbody[@id='booksTable']/tr[1]//button[contains(@class, 'btnEliminar')]")
    btn_eliminar.click()
    time.sleep(0.5)

    # MANEJO DE ALERTA 
    alert = driver.switch_to.alert
    alert.dismiss() # Clic en "Cancelar"
    time.sleep(1)
    tabla_texto = driver.find_element(By.ID, "booksTable").text
    assert "Libro Salvado" in tabla_texto

    filas = driver.find_elements(By.XPATH, "//tbody[@id='booksTable']/tr")
    assert len(filas) == 1

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/eliminar_cancelado_{timestamp}.png")
    print("✓ Cancelar eliminación - OK")

#   TEST 3: ELIMINAR UNO DE VARIOS

def test_eliminar_libro_especifico(driver):
    """
    Elimina uno específico aceptando la alerta.
    """
    hacer_login(driver)
    driver.execute_script("localStorage.clear();")
    driver.refresh()
    time.sleep(1)

    agregar_libro(driver, "Libro A (Borrar)", "Autor A", 2000, "leido")
    agregar_libro(driver, "Libro B (Conservar)", "Autor B", 2001, "pendiente")

    # Eliminar el PRIMERO
    btn_eliminar_primero = driver.find_element(By.XPATH, "//tbody[@id='booksTable']/tr[1]//button[contains(@class, 'btnEliminar')]")
    btn_eliminar_primero.click()
    time.sleep(0.5)

    # Aceptar alerta
    driver.switch_to.alert.accept()
    time.sleep(1)

    # Verificaciones
    tabla_texto = driver.find_element(By.ID, "booksTable").text
    assert "Libro A (Borrar)" not in tabla_texto
    assert "Libro B (Conservar)" in tabla_texto

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/eliminar_especifico_{timestamp}.png")
    print("✓ Eliminar uno de varios - OK")

#   TEST 4: PERSISTENCIA AL ELIMINAR

def test_eliminar_y_persistencia(driver):
    """
    Elimina, acepta alerta, refresca y verifica.
    """
    hacer_login(driver)
    driver.execute_script("localStorage.clear();")
    driver.refresh()
    time.sleep(1)

    agregar_libro(driver, "Libro Fantasma", "Gasparin", 1995, "pendiente")

    # Eliminar
    driver.find_element(By.XPATH, "//tbody[@id='booksTable']/tr[1]//button[contains(@class, 'btnEliminar')]").click()
    time.sleep(0.5)
    
    # Aceptar alerta
    driver.switch_to.alert.accept()
    time.sleep(1)

    # Refrescar página
    driver.refresh()
    time.sleep(2)

    filas = driver.find_elements(By.XPATH, "//tbody[@id='booksTable']/tr")
    assert len(filas) == 0

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/eliminar_persistencia_{timestamp}.png")
    print("✓ Eliminar y persistencia - OK")