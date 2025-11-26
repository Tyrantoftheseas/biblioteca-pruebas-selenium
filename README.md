# Biblioteca Personal - Pruebas Automatizadas

Sistema de gestión de biblioteca personal con pruebas automatizadas usando Selenium.

## 🚀 Características

- Login con validación
- CRUD completo de libros (Título, Autor, Año, Estado)
- Confirmación al eliminar
- 15 casos de prueba automatizados

## 🛠️ Tecnologías

- **Frontend:** HTML, CSS, JavaScript (localStorage)
- **Testing:** Selenium WebDriver, Pytest
- **Reporte:** pytest-html

## 📋 Requisitos

- Python 3.8+
- Google Chrome
- ChromeDriver (se instala automáticamente con webdriver-manager)

## ⚙️ Instalación

1. Clonar repositorio:

```bash
git clone https://github.com/tu-usuario/biblioteca-pruebas-selenium.git
cd biblioteca-pruebas-selenium
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

## 🧪 Ejecutar Pruebas

**Todas las pruebas:**

```bash
python run_tests.py
```

**Pruebas individuales:**

```bash
pytest tests/test_login.py -v
```

## 📊 Reporte HTML

Después de ejecutar las pruebas, el reporte se genera en `reports/reporte_final_YYYYMMDD_HHMMSS.html`

## 🎯 Historias de Usuario

Documentadas en Azure DevOps:
https://dev.azure.com/20240001/Biblioteca-Selenium/_boards/board/t/Biblioteca-Selenium%20Team/Issues

**5 Historias de Usuario implementadas:**

- HU-01: Inicio de Sesión
- HU-02: Agregar Libro
- HU-03: Ver Lista de Libros
- HU-04: Editar Libro
- HU-05: Eliminar Libro

## 👤 Autor

George S S R - Estudiante de Programación 3

## 📧 Contacto

- Correo: 20240001@itla.edu.do
- GitHub: Tyrantoftheseas

```

```
