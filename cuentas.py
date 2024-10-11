from .validaciones import validacionCuenta, validacionDocumento

# Esta función crea las cuentas de forma personalizada para cada usuario
def crearCuenta(cuentas, movimientos):
    while True:
        name = input("Ingrese su nombre: ")
        if name.isalpha():          # Lo que hace isalpha() es ver si name solo contiene letras
            break
        else:
            print("El nombre solo debe contener letras. Intente nuevamente.")

    while True:
        document = validacionDocumento(cuentas)
        if document > 0:
            break
        else:
            print("El documento debe ser un número positivo. Intente nuevamente.")
    clave = str(input('\nDigite la clave que quiere para su cuenta: '))
    numeroCuenta = validacionCuenta(cuentas)      # Llamo a mi función para generar el numero de cuenta del usuario que esté haciendo el registro
    cuentas[numeroCuenta] = {"documento": document, "nombre": name, "clave": clave, "saldo": 0}
    movimientos[numeroCuenta] = []                 # Se inicializa el diccionario de movimientos con un arreglo vacio para comenzar a poner datos
    return f'\n===================== | Bienvenido {name.upper()} | ===================== \n\nEl numero de su cuenta es: {numeroCuenta}\n'

# Esta función muestra las cuentas (para pruebas)
# El ljust() lo que hace es poner espacios vacios a su derecha para dar formato

def mostrarCuenta(cuentas):
    print ("\n\n=================== Mostrar Datos Cuenta ===================")
    print("CUENTA".ljust(15) + "DOCUMENTO".ljust(15) + "NOMBRE".ljust(15) + "SALDO".ljust(15))
    for numeroCuenta, cuenta in cuentas.items():
        print(f"{str(numeroCuenta).ljust(15)}{str(cuenta['documento']).ljust(15)}{cuenta['nombre'].ljust(15)}{str(cuenta['saldo']).ljust(15)}\n")
# Consultar movimientos de la cuenta
def consultarMovimientos(numeroCuenta, movimientos):
    print ("\n\n=================== Extracto de movimientos ===================\n")
    print("Tipo de movimiento".ljust(30)+"Valor".ljust(15) +"Referencia".ljust(15)+"Descripción".ljust(40)+"Fecha y hora")
    if numeroCuenta in movimientos:
        for mov in movimientos[numeroCuenta]:
            print(f"{str(mov['tipo']).ljust(30)}{str(mov['valor']).ljust(15)}{str(mov['referencia']).ljust(15)}{str(mov['descripcion']).ljust(40)}{str(mov['fecha y hora'])}\n")
    else:
        print("\nNo hay movimientos en la cuenta")

# Login de usuario
def login(cuentas):
    numeroCuenta = str(input('\nEscriba su numero de cuenta: '))
    clave = str(input('\nEscriba su clave: '))
    cuenta = cuentas.get(numeroCuenta)      # Se obtine la cuenta para verificar que exista
    if cuenta:
        if clave == cuenta["clave"]:
            return numeroCuenta             # Se retorna porque se necesita extraer los datos del usuario en el Main.py
        else:
            return None
    return None