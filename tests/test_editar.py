import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from datetime import datetime

# Ajusta la ruta a tu usuario real
URL = r"file:///C:/Users/George S S R/Documents/GitHub/biblioteca-pruebas-selenium/app/index.html"


# ============================
#   FUNCIONES HELPER
# ============================

def hacer_login(driver):
    driver.get(URL)
    time.sleep(1)
    
    driver.find_element(By.ID, "usuario").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.ID, "btnLogin").click()
    time.sleep(2)

    # Redirección manual para asegurar que estamos en dashboard
    driver.get("file:///C:/Users/George S S R/Documents/GitHub/biblioteca-pruebas-selenium/app/dashboard.html")
    time.sleep(2)


def agregar_libro(driver, titulo, autor, anio, estado):
    driver.find_element(By.ID, "titulo").clear()
    driver.find_element(By.ID, "titulo").send_keys(titulo)
    
    driver.find_element(By.ID, "autor").clear()
    driver.find_element(By.ID, "autor").send_keys(autor)
    
    driver.find_element(By.ID, "anio").clear()
    driver.find_element(By.ID, "anio").send_keys(str(anio))
    
    select = Select(driver.find_element(By.ID, "estado"))
    select.select_by_value(estado)
    
    driver.find_element(By.ID, "btnAgregar").click()
    time.sleep(1)


# ============================
#   TEST 1: CAMINO FELIZ
# ============================

def test_editar_libro_camino_feliz(driver):
    """
    Prueba básica: Agrega un libro, lo edita y verifica el cambio.
    """
    hacer_login(driver)
    
    # Limpiar entorno
    driver.execute_script("localStorage.clear();")
    driver.refresh()
    time.sleep(1)

    # 1. Agregar libro base
    agregar_libro(driver, "Libro Viejo", "Autor X", 1990, "pendiente")

    # 2. Clic en Editar (del primer libro en la tabla)
    btn_editar = driver.find_element(By.XPATH, "//tbody[@id='booksTable']/tr[1]//button[contains(@class, 'btnEditar')]")
    btn_editar.click()
    time.sleep(1)

    # 3. Modificar datos
    driver.find_element(By.ID, "titulo").clear()
    driver.find_element(By.ID, "titulo").send_keys("Libro Editado VIP")

    select = Select(driver.find_element(By.ID, "estado"))
    select.select_by_value("leido")
    time.sleep(1)

    # 4. Guardar cambios
    driver.find_element(By.ID, "btnUpdate").click()
    time.sleep(2)

    # 5. Verificaciones
    tabla_texto = driver.find_element(By.ID, "booksTable").text
    assert "Libro Editado VIP" in tabla_texto
    assert "leido" in tabla_texto
    
    # Verificar mensaje de éxito
    msg = driver.find_element(By.ID, "msgExito").text
    assert "actualizado correctamente" in msg

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/editar_feliz_{timestamp}.png")
    print("✓ Editar libro camino feliz - OK")


# ============================
#   TEST 2: PERSISTENCIA
# ============================

def test_editar_y_persistencia(driver):
    """
    Edita un libro, refresca la página (F5) y verifica que el cambio se guardó.
    """
    hacer_login(driver)
    driver.execute_script("localStorage.clear();")
    driver.refresh()
    time.sleep(1)

    agregar_libro(driver, "Original", "Autor", 2020, "pendiente")

    # Editar
    driver.find_element(By.XPATH, "//tbody[@id='booksTable']/tr[1]//button[contains(@class, 'btnEditar')]").click()
    time.sleep(1)

    # Cambiar título
    driver.find_element(By.ID, "titulo").clear()
    driver.find_element(By.ID, "titulo").send_keys("Modificado Final")
    driver.find_element(By.ID, "btnUpdate").click()
    time.sleep(1)

    # REFRESCO DE PÁGINA
    driver.refresh()
    time.sleep(2)

    tabla_texto = driver.find_element(By.ID, "booksTable").text
    assert "Modificado Final" in tabla_texto
    assert "Original" not in tabla_texto

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/editar_persistencia_{timestamp}.png")
    print("✓ Editar y persistencia - OK")


# ============================
#   TEST 3: CASO NEGATIVO (Validación)
# ============================

def test_editar_campos_vacios(driver):
    """
    Intenta editar borrando campos obligatorios. 
    Debe aparecer mensaje de error y NO guardar.
    """
    hacer_login(driver)
    driver.execute_script("localStorage.clear();")
    driver.refresh()
    time.sleep(1)

    agregar_libro(driver, "Libro X", "Autor X", 2001, "pendiente")

    # 1. Clic en Editar
    driver.find_element(By.XPATH, "//tbody[@id='booksTable']/tr[1]//button[contains(@class, 'btnEditar')]").click()
    time.sleep(1)

    # 2. Limpiar campos obligatorios
    driver.find_element(By.ID, "titulo").clear()
    driver.find_element(By.ID, "autor").clear()
    driver.find_element(By.ID, "anio").clear()
    time.sleep(1)

    # 3. Intentar Actualizar
    driver.find_element(By.ID, "btnUpdate").click()
    time.sleep(1)

    # 4. Verificar mensaje de error
    msg_error = driver.find_element(By.ID, "msgForm").text
    assert "obligatorios" in msg_error.lower()
    
    btn_update = driver.find_element(By.ID, "btnUpdate")
    assert btn_update.is_displayed() == True

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/editar_error_vacio_{timestamp}.png")
    print("✓ Editar con campos vacíos (Validación) - OK")