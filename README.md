# Biblioteca Personal - Pruebas Automatizadas

Sistema de gestión de biblioteca personal con pruebas automatizadas usando Selenium y Python.

## Características

- **Autenticación:** Login con validación de credenciales y campos vacíos
- **CRUD Completo:** Gestión de libros (Título, Autor, Año, Estado: Leído/Pendiente)
- **Confirmación de Eliminación:** Diálogo de confirmación con opción de cancelar
- **Persistencia:** Almacenamiento local con localStorage
- **16 Pruebas Automatizadas:** 3 tipos por historia (camino feliz, negativa, límites)

## Tecnologías

- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Testing:** Selenium WebDriver, Pytest
- **Reportes:** pytest-html con screenshots automáticos
- **Gestión de Drivers:** webdriver-manager (instalación automática de ChromeDriver)

## Requisitos Previos

- Python 3.8+
- Google Chrome (última versión)
- Git

## Instalación

1. **Clonar el repositorio:**

```bash
git clone https://github.com/Tyrantoftheseas/biblioteca-pruebas-selenium.git
cd biblioteca-pruebas-selenium
```

2. **Instalar dependencias:**

```bash
pip install -r requirements.txt
```

## Ejecutar Pruebas automatizadas

### Prueba unitaria (Recomendado)

```bash
python run_tests.py
```

Esto ejecutará las 16 pruebas en orden lógico:

1. Login (3 tests)
2. Agregar libro (3 tests)
3. Listar libros (3 tests)
4. Editar libro (3 tests)
5. Eliminar libro (4 tests)

### Pruebas Individuales por Módulo

```bash
pytest tests/test_login.py -v
pytest tests/test_agregar.py -v
pytest tests/test_listar.py -v
pytest tests/test_editar.py -v
pytest tests/test_eliminar.py -v
```

## Reportes y Evidencias

### Reporte HTML

Después de ejecutar `python run_tests.py`, el reporte se genera en:

```
reports/reporte_final_YYYYMMDD_HHMMSS.html
```

**Contenido del reporte:**

- Resultado de cada test (Pass/Fail)
- Tiempos de ejecución
- Metadata del ambiente (Python, pytest, plataforma)
- Estadísticas generales

### Screenshots Automáticos

Cada test genera screenshots en `screenshots/` con formato:

```
test_nombre_TIMESTAMP.png
```

Los screenshots capturan el estado de la aplicación en momentos clave de cada prueba.

## Historias de Usuario

**Documentación completa en Azure DevOps:**  
[Ver Tablero de Historias](https://dev.azure.com/20240001/Biblioteca-Selenium/_boards/board/t/Biblioteca-Selenium%20Team/Issues)

### Cobertura de Pruebas

| Historia                       | P.historia | Test Cases | Variantes                                        |
| ------------------------------ | ---------- | ---------- | ------------------------------------------------ |
| **HU-01:** Inicio de Sesión    | 3          | TC-01      | Exitoso, Incorrecta, Vacíos                      |
| **HU-02:** Agregar Libro       | 5          | TC-02      | Exitoso, Vacíos, Año Inválido                    |
| **HU-03:** Ver Lista de Libros | 2          | TC-03      | Con Datos, Sin Datos, Múltiples                  |
| **HU-04:** Editar Libro        | 5          | TC-04      | Exitoso, Persistencia, Vacíos                    |
| **HU-05:** Eliminar Libro      | 3          | TC-05      | Confirmación, Cancelar, Persistencia, Específico |

**Total:** 18 Puntos de historia | 16 Casos de Prueba

Cada Test Case incluye:

- Descripción de las variantes
- Pasos detallados
- Resultados esperados
- Screenshots de evidencia (adjuntos en Azure DevOps)

## Tipos de Pruebas

Cada historia de usuario cubre:

1. **Camino Feliz:** Flujo principal sin errores
2. **Prueba Negativa:** Validación de errores y rechazos
3. **Prueba de Límites:** Casos extremos y validaciones de borde

## Estructura del Proyecto

```
biblioteca-pruebas-selenium/
├── app/                          # Aplicación web
│   ├── index.html               # Login
│   ├── dashboard.html           # CRUD
│   ├── styles.css              # Estilos
│   └── script.js               # Lógica JS
├── tests/                       # Pruebas automatizadas
│   ├── conftest.py             # Configuración pytest
│   ├── test_login.py           # 3 tests
│   ├── test_agregar.py         # 3 tests
│   ├── test_listar.py          # 3 tests
│   ├── test_editar.py          # 3 tests
│   └── test_eliminar.py        # 4 tests
├── screenshots/                 # Capturas automáticas
├── reports/                     # Reportes HTML
├── run_tests.py                # Script de ejecución
├── requirements.txt            # Dependencias Python
└── README.md                   # Documentación
```

## Video Demostración

**Ver demostración completa en YouTube:**

**Contenido del video:**

- Demostración de la aplicación web funcionando
- Ejecución completa de las 16 pruebas automatizadas
- Navegación por el reporte HTML generado
- Revisión de Test Cases en Azure DevOps

## Autor

**George Steven Santana Rosario**  
Estudiante de Programación 3 - ITLA  
Proyecto Académico: Tarea 4 - Pruebas Automatizadas con Selenium

## Contacto

- **Correo:** 20240001@itla.edu.do
- **GitHub:** [Tyrantoftheseas](https://github.com/Tyrantoftheseas)
- **Azure DevOps:** [Biblioteca-Selenium](https://dev.azure.com/20240001/Biblioteca-Selenium)

## Licencia

Este proyecto es de uso académico para el Instituto Tecnológico de Las Américas (ITLA).

---

**Proyecto desarrollado como parte del curso de Programación 3**
