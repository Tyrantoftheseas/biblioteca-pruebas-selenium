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
    wait.until(EC.element_to_be_clickable((By.ID, "btnLogin"))).click()
    
    # Esperar redirección
    wait.until(EC.url_contains("dashboard.html"))

def test_agregar_libro_exitoso(driver):
    hacer_login(driver)
    wait = WebDriverWait(driver, 5)

    wait.until(EC.visibility_of_element_located((By.ID, "titulo"))).send_keys("Cien años de soledad")
    driver.find_element(By.ID, "autor").send_keys("Gabriel García Márquez")
    driver.find_element(By.ID, "anio").send_keys("1967")
    
    select = Select(driver.find_element(By.ID, "estado"))
    select.select_by_value("leido")
    
    wait.until(EC.element_to_be_clickable((By.ID, "btnAgregar"))).click()
    
    # Esperar mensaje de éxito
    msg_exito = wait.until(EC.visibility_of_element_located((By.ID, "msgExito")))
    assert "agregado" in msg_exito.text.lower()
    
    # Esperar que aparezca en la tabla
    wait.until(EC.text_to_be_present_in_element((By.ID, "booksTable"), "Cien años de soledad"))
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/agregar_exitoso_{timestamp}.png")
    print("✓ Agregar libro exitoso - OK")

def test_agregar_libro_campos_vacios(driver):
    hacer_login(driver)
    wait = WebDriverWait(driver, 5)

    wait.until(EC.visibility_of_element_located((By.ID, "titulo"))).clear()
    driver.find_element(By.ID, "autor").send_keys("Autor X")
    driver.find_element(By.ID, "anio").send_keys("2000")
    
    wait.until(EC.element_to_be_clickable((By.ID, "btnAgregar"))).click()
    
    msg_error = wait.until(EC.visibility_of_element_located((By.ID, "msgForm")))
    assert "obligatorios" in msg_error.text.lower()
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/agregar_vacio_{timestamp}.png")
    print("✓ Campos vacíos validado - OK")

def test_agregar_libro_anio_invalido(driver):
    hacer_login(driver)
    wait = WebDriverWait(driver, 5)
    
    wait.until(EC.visibility_of_element_located((By.ID, "titulo"))).send_keys("El Principito")
    driver.find_element(By.ID, "autor").send_keys("Antoine de Saint-Exupéry")
    driver.find_element(By.ID, "anio").send_keys("abc")
    
    driver.find_element(By.ID, "btnAgregar").click()
    msg_error = wait.until(EC.visibility_of_element_located((By.ID, "msgForm")))
    assert "obligatorios" in msg_error.text.lower()
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/agregar_anio_invalido_{timestamp}.png")
    print("✓ Año inválido - OK")