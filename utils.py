import random

# Generar números de cuenta
def generarNumeroCuenta():
    numero = random.randint(10, 999)        # El randint define el rango de los numeros que se van a generar
    return str(numero).zfill(3)             # El zfill rellena con ceros a la izquierda

# Generar referencias
def generarReferencia():
    numero = random.randint(1, 99999)       # 50
    return str(numero).zfill(5)             # "00050"