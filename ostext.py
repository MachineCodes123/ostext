import zipfile
import time
import os
from blessed import Terminal
import psutil


t=Terminal()

print(t.on_red+"Cargando el sistema"+t.normal)

# Obtener la información de memoria
memoria = psutil.virtual_memory()

# Imprimir la memoria RAM disponible en bytes
print("Memoria RAM disponible:", memoria.available)

# Imprimir la memoria RAM disponible en formato legible
print("Memoria RAM disponible:", psutil._common.bytes2human(memoria.available))

