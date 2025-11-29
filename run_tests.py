import pytest
import os
from datetime import datetime

# 1. Configuración de carpetas
if not os.path.exists("reports"):
    os.makedirs("reports", exist_ok=True)

# 2. Generar nombre del reporte con fecha y hora
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_file = f"reports/reporte_final_{timestamp}.html"

# 3. Argumentos para pytest
#orden explícito de ejecución
args = [
    
    "tests/test_login.py",    # 1. Autenticación
    "tests/test_agregar.py",  # 2. Crear datos
    "tests/test_listar.py",   # 3. Leer datos
    "tests/test_editar.py",   # 4. Actualizar datos
    "tests/test_eliminar.py", # 5. Borrar datos 

    # --- OPCIONES ---
    "-v",                   # Muestra detalles en consola
    "-s",                   # Muestra tus prints() en consola
    f"--html={report_file}", # Genera el reporte visual en tu carpeta reports
    "--self-contained-html" 
]

print("="*60)
print(f" INICIANDO PRUEBAS AUTOMATIZADAS")
print(f" Carpeta de reportes: {os.path.abspath('reports')}")
print("="*60 + "\n")

# 4. Ejecutar pytest
exit_code = pytest.main(args)

# 5. Resumen final
print("\n" + "="*60)
if exit_code == 0:
    print(f"✅  Todas las pruebas pasaron correctamente.")
    print(f" Reporte generado: {report_file}")
else:
    print(f"ALGUNAS PRUEBAS FALLARON.")
    print(f"Revise el reporte para ver los errores: {report_file}")
print("="*60)