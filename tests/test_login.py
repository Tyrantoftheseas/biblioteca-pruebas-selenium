import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# Ajusta la ruta a tu usuario real
URL = r"file:///C:/Users/George S S R/Documents/GitHub/biblioteca-pruebas-selenium/app/index.html"

def test_login_exitoso(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 5) # Espera máxima de 5 segundos

    # Esperar a que el usuario sea visible y escribir
    wait.until(EC.visibility_of_element_located((By.ID, "usuario"))).send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")
    
    # Esperar a que el botón sea cliqueable y click
    wait.until(EC.element_to_be_clickable((By.ID, "btnLogin"))).click()
    
    # Validar redirección (esperar a que la URL cambie)
    wait.until(EC.url_contains("dashboard.html"))
    assert "dashboard.html" in driver.current_url
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/login_exitoso_{timestamp}.png")
    print("✓ Login exitoso - OK")

def test_login_contrasena_incorrecta(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 5)

    wait.until(EC.visibility_of_element_located((By.ID, "usuario"))).send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("wrong")
    
    wait.until(EC.element_to_be_clickable((By.ID, "btnLogin"))).click()
    
    # Esperar a que aparezca el mensaje de error
    msg_element = wait.until(EC.visibility_of_element_located((By.ID, "msgError")))
    assert "incorrectos" in msg_element.text.lower()
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/login_incorrecto_{timestamp}.png")
    print("✓ Login incorrecto - OK")

def test_login_campos_vacios(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 5)

    wait.until(EC.element_to_be_clickable((By.ID, "btnLogin"))).click()
    
    msg_element = wait.until(EC.visibility_of_element_located((By.ID, "msgError")))
    text = msg_element.text.lower()
    assert "vacíos" in text or "campos" in text
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/login_vacio_{timestamp}.png")
    print("✓ Campos vacíos - OK")