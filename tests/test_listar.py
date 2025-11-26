import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time # Usaremos time.sleep MUY poco, solo para refrescos forzados

URL = r"file:///C:/Users/George S S R/Documents/GitHub/biblioteca-pruebas-selenium/app/index.html"

def hacer_login(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.ID, "usuario"))).send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.ID, "btnLogin").click()
    # Esperamos  la redirección
    wait.until(EC.url_contains("dashboard.html"))
    # Forzamos la carga del dashboard si la redirección fue interna
    driver.get("file:///C:/Users/George S S R/Documents/GitHub/biblioteca-pruebas-selenium/app/dashboard.html")

def agregar_libro_rapido(driver, titulo, autor, anio, estado):
    # Versión sin esperas largas, confiando en la velocidad del driver
    driver.find_element(By.ID, "titulo").send_keys(titulo)
    driver.find_element(By.ID, "autor").send_keys(autor)
    driver.find_element(By.ID, "anio").send_keys(str(anio))
    Select(driver.find_element(By.ID, "estado")).select_by_value(estado)
    driver.find_element(By.ID, "btnAgregar").click()
    
    # Pequeña espera para asegurar que JS procesó la adición antes de la siguiente
    WebDriverWait(driver, 2).until(EC.text_to_be_present_in_element((By.ID, "booksTable"), titulo))
    
    # Limpiar campos para el siguiente (importante si agregamos múltiples)
    driver.find_element(By.ID, "titulo").clear()
    driver.find_element(By.ID, "autor").clear()
    driver.find_element(By.ID, "anio").clear()

def test_listar_libros_con_datos(driver):
    hacer_login(driver)
    driver.execute_script("localStorage.clear();")
    driver.refresh()
    
    agregar_libro_rapido(driver, "1984", "George Orwell", 1949, "leido")
    agregar_libro_rapido(driver, "Fahrenheit 451", "Ray Bradbury", 1953, "pendiente")

    tabla = driver.find_element(By.ID, "booksTable").text
    assert "1984" in tabla
    assert "Fahrenheit 451" in tabla

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/listar_con_datos_{timestamp}.png")
    print("✓ Listar libros con datos - OK")

def test_listar_sin_libros(driver):
    hacer_login(driver)
    driver.execute_script("localStorage.clear();")
    driver.refresh()
    
    # Esperamos a que la tabla esté presente (aunque esté vacía)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "booksTable")))
    
    filas = driver.find_elements(By.XPATH, "//tbody[@id='booksTable']/tr")
    assert len(filas) == 0

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/listar_sin_libros_{timestamp}.png")
    print("✓ Listar sin libros - OK")

def test_listar_despues_de_agregar_multiples(driver):
    hacer_login(driver)
    driver.execute_script("localStorage.clear();")
    driver.refresh()

    libros = [
        ("Libro A", "Autor A", 2001, "leido"),
        ("Libro B", "Autor B", 2002, "leido"),
        ("Libro C", "Autor C", 2003, "pendiente"),
        ("Libro D", "Autor D", 2004, "pendiente"),
        ("Libro E", "Autor E", 2005, "leido"),
    ]

    for t, a, y, e in libros:
        agregar_libro_rapido(driver, t, a, y, e)

    # Verificación final
    filas = driver.find_elements(By.XPATH, "//tbody[@id='booksTable']/tr")
    assert len(filas) == 5

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/listar_multiples_{timestamp}.png")
    print("✓ Listar múltiples - OK")