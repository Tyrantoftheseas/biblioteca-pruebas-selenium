import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

URL = r"file:///C:/Users/George S S R/Documents/GitHub/biblioteca-pruebas-selenium/app/index.html"

def hacer_login(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.ID, "usuario"))).send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.ID, "btnLogin").click()
    wait.until(EC.url_contains("dashboard.html"))
    driver.get("file:///C:/Users/George S S R/Documents/GitHub/biblioteca-pruebas-selenium/app/dashboard.html")

def agregar_libro(driver, titulo, autor, anio, estado):
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.ID, "titulo"))).send_keys(titulo)
    driver.find_element(By.ID, "autor").send_keys(autor)
    driver.find_element(By.ID, "anio").send_keys(str(anio))
    Select(driver.find_element(By.ID, "estado")).select_by_value(estado)
    driver.find_element(By.ID, "btnAgregar").click()
    wait.until(EC.text_to_be_present_in_element((By.ID, "booksTable"), titulo))

def test_eliminar_libro_exitoso(driver):
    hacer_login(driver)
    driver.execute_script("localStorage.clear();")
    driver.refresh()
    wait = WebDriverWait(driver, 5)

    agregar_libro(driver, "Libro a Borrar", "Autor X", 2024, "pendiente")

    # Eliminar
    btn_eliminar = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//tbody[@id='booksTable']/tr[1]//button[contains(@class, 'btnEliminar')]")
    ))
    btn_eliminar.click()

    wait.until(EC.alert_is_present()) 
    alert = driver.switch_to.alert
    alert.accept()
    
    # 1. Verificar que la tabla se vacíe
    wait.until(lambda d: len(d.find_elements(By.XPATH, "//tbody[@id='booksTable']/tr")) == 0)
    
    # 2. Verificar MENSAJE DE ÉXITO (Nuevo)
    msg_exito = wait.until(EC.visibility_of_element_located((By.ID, "msgExito")))
    assert "eliminado" in msg_exito.text.lower()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/eliminar_exitoso_{timestamp}.png")
    print("✓ Eliminar libro único (con mensaje) - OK")

def test_cancelar_eliminacion(driver):
    hacer_login(driver)
    driver.execute_script("localStorage.clear();")
    driver.refresh()
    wait = WebDriverWait(driver, 5)

    agregar_libro(driver, "Libro Salvado", "Autor Y", 2025, "leido")

    btn_eliminar = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//tbody[@id='booksTable']/tr[1]//button[contains(@class, 'btnEliminar')]")
    ))
    btn_eliminar.click()

    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.dismiss() # Cancelar

    # Verificar que el libro SIGUE ahí
    tabla_texto = driver.find_element(By.ID, "booksTable").text
    assert "Libro Salvado" in tabla_texto

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/eliminar_cancelado_{timestamp}.png")
    print("✓ Cancelar eliminación - OK")

def test_eliminar_libro_especifico(driver):
    hacer_login(driver)
    driver.execute_script("localStorage.clear();")
    driver.refresh()
    wait = WebDriverWait(driver, 5)

    agregar_libro(driver, "Libro A (Borrar)", "Autor A", 2000, "leido")
    driver.find_element(By.ID, "titulo").clear()
    driver.find_element(By.ID, "autor").clear()
    driver.find_element(By.ID, "anio").clear()
    agregar_libro(driver, "Libro B (Conservar)", "Autor B", 2001, "pendiente")

    btn_eliminar = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//tbody[@id='booksTable']/tr[1]//button[contains(@class, 'btnEliminar')]")
    ))
    btn_eliminar.click()

    wait.until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    
    # Esperar a que Libro A desaparezca
    wait.until_not(EC.text_to_be_present_in_element((By.ID, "booksTable"), "Libro A (Borrar)"))

    # Verificar mensaje
    msg_exito = wait.until(EC.visibility_of_element_located((By.ID, "msgExito")))
    assert "eliminado" in msg_exito.text.lower()

    tabla_texto = driver.find_element(By.ID, "booksTable").text
    assert "Libro B (Conservar)" in tabla_texto

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/eliminar_especifico_{timestamp}.png")
    print("✓ Eliminar uno de varios (con mensaje) - OK")

def test_eliminar_y_persistencia(driver):
    hacer_login(driver)
    driver.execute_script("localStorage.clear();")
    driver.refresh()
    wait = WebDriverWait(driver, 5)

    agregar_libro(driver, "Libro Fantasma", "Gasparin", 1995, "pendiente")

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//tbody[@id='booksTable']/tr[1]//button[contains(@class, 'btnEliminar')]")
    )).click()
    
    wait.until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    
    wait.until(lambda d: len(d.find_elements(By.XPATH, "//tbody[@id='booksTable']/tr")) == 0)

    driver.refresh()
    
    filas = driver.find_elements(By.XPATH, "//tbody[@id='booksTable']/tr")
    assert len(filas) == 0

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/eliminar_persistencia_{timestamp}.png")
    print("✓ Eliminar y persistencia - OK")