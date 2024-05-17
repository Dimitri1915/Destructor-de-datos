import os
import random
import string

def overwrite_with_ones(file_path):
    with open(file_path, 'wb') as file:
        file.write(b'\xFF' * os.path.getsize(file_path))

def overwrite_with_zeros(file_path):
    with open(file_path, 'wb') as file:
        file.write(b'\x00' * os.path.getsize(file_path))

def overwrite_with_random_data(file_path):
    with open(file_path, 'wb') as file:
        random_data = os.urandom(os.path.getsize(file_path))
        file.write(random_data)

def secure_erase(file_path):
    overwrite_with_ones(file_path)
    overwrite_with_zeros(file_path)
    overwrite_with_random_data(file_path)

# Ejemplo de uso:
if _name_ == "_main_":
    file_to_erase = "archivo_a_borrar.dat"
    if os.path.exists(file_to_erase):
        secure_erase(file_to_erase)
        os.remove(file_to_erase)
        print(f"Eliminación segura de {file_to_erase} completada.")
    else:
        print(f"El archivo {file_to_erase} no existe.")