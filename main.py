import pandas as pd
import numpy as np
import random
import os
from datetime import datetime, timedelta

# Configuración de la semilla aleatoria para reproducibilidad
np.random.seed(42)

# Función para generar fechas aleatorias
def random_dates(start, end, n):
    date_range = (end - start).days
    return [start + timedelta(days=random.randint(0, date_range)) for _ in range(n)]

# Tabla 1: Pacientes
n_pacientes = 1000
pacientes = pd.DataFrame({
    'ID_Paciente': range(1, n_pacientes + 1),
    'Edad': np.random.randint(18, 80, n_pacientes),
    'Genero': np.random.choice([0, 1], n_pacientes),  # 0: Femenino, 1: Masculino
    'Codigo_Postal': np.random.randint(10000, 99999, n_pacientes),
    'Fecha_Registro': random_dates(datetime(2020, 1, 1), datetime(2024, 12, 31), n_pacientes)
})

# Tabla 2: Citas
n_citas = 5000
citas = pd.DataFrame({
    'ID_Cita': range(1, n_citas + 1),
    'ID_Paciente': np.random.choice(pacientes['ID_Paciente'], n_citas),
    'ID_Dentista': np.random.randint(1, 11, n_citas),  # Asumimos 10 dentistas
    'Fecha_Cita': random_dates(datetime(2023, 1, 1), datetime(2024, 12, 31), n_citas),
    'Duracion_Minutos': np.random.choice([30, 45, 60, 90], n_citas),
    'Estado': np.random.choice([0, 1, 2], n_citas)  # 0: Programada, 1: Completada, 2: Cancelada
})

# Tabla 3: Tratamientos
n_tratamientos = 3000
tratamientos = pd.DataFrame({
    'ID_Tratamiento': range(1, n_tratamientos + 1),
    'ID_Cita': np.random.choice(citas['ID_Cita'], n_tratamientos),
    'Codigo_Tratamiento': np.random.randint(100, 999, n_tratamientos),
    'Costo': np.random.uniform(50, 1000, n_tratamientos).round(2),
    'Duracion_Minutos': np.random.choice([15, 30, 45, 60, 90], n_tratamientos)
})

# Tabla 4: Pagos
n_pagos = 2500
pagos = pd.DataFrame({
    'ID_Pago': range(1, n_pagos + 1),
    'ID_Paciente': np.random.choice(pacientes['ID_Paciente'], n_pagos),
    'Fecha_Pago': random_dates(datetime(2023, 1, 1), datetime(2024, 12, 31), n_pagos),
    'Monto': np.random.uniform(50, 2000, n_pagos).round(2),
    'Metodo_Pago': np.random.choice([0, 1, 2, 3], n_pagos)  # 0: Efectivo, 1: Tarjeta, 2: Transferencia, 3: Otro
})

# Tabla 5: Inventario
n_items = 200
inventario = pd.DataFrame({
    'ID_Item': range(1, n_items + 1),
    'Cantidad': np.random.randint(0, 1000, n_items),
    'Precio_Unitario': np.random.uniform(1, 500, n_items).round(2),
    'Fecha_Ultima_Reposicion': random_dates(datetime(2023, 1, 1), datetime(2024, 12, 31), n_items),
    'Proveedor_ID': np.random.randint(1, 21, n_items)  # Asumimos 20 proveedores
})

# Guardar los DataFrames en archivos CSV
if not os.path.exists('data'):
    os.makedirs('data')
pacientes.to_csv('data/pacientes.csv', index=False)
citas.to_csv('data/citas.csv', index=False)
tratamientos.to_csv('data/tratamientos.csv', index=False)
pagos.to_csv('data/pagos.csv', index=False)
inventario.to_csv('data/inventario.csv', index=False)

print("Archivos CSV generados exitosamente.")