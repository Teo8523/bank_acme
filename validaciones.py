from utils import generarNumeroCuenta 

# Validar si el número de cuenta ya existe
def validacionCuenta(cuentas):
    while True:
        numeroCuenta = generarNumeroCuenta()
        if numeroCuenta not in cuentas:
            return numeroCuenta
        else:
            print("El numero de cuenta ya existe, se generará uno nuevo.")

def validacionDocumento(cuentas):
    while True:
        documento = int(input("\nIngrese su numero de documento: "))
        if documento not in [cuenta['documento'] for cuenta in cuentas.values()]:
            return documento
        else:
            print("El documento ya existe, ingrese otro.")