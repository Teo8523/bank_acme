# Importar modulos
from modulos.cuentas import crearCuenta, login, mostrarCuenta
from modulos.transacciones import consignarDinero, consignarDestinatario, retirarDinero, pagarServicios
from modulos.cuentas import consultarMovimientos

# Menú principal
def menu():
    print('=============================================')
    print(f'BIENVENIDO AL SISTEMA\n 1. Crear cuenta\n 2. Realizar consignacion \n 3. Login\n 0. Salir del programa')
    opc = int(input('Ponga una opción:'))
    return opc

# Menú de cliente
def menuCliente():
    print('=============================================')
    print(f'BIENVENIDO AL LOGIN\n 1. Consignar dinero a una cuenta\n 2. Retirar dinero de su cuenta\n 3. Pagar servicios \n 4. Consultar movimientos \n 0. Salir de la cuenta')
    print('=============================================')  
    opc = int(input('Ponga una opción:'))
    return opc


# Datos iniciales
movimientos = {}
cuentas = {}

# Ejecución del programa
opc = 10

while opc != 0:
    try:
        opc = menu()
        if opc == 1:
            print('\nCrear cuenta ''')
            print(crearCuenta(cuentas, movimientos))
        elif opc == 2:
            print('\nConsignar a mi cuenta\n')
            consignarDinero(cuentas, movimientos)  # Aquí paso 'cuentas' y 'movimientos'
        elif opc == 3:
            print('\nLogin')
            numeroCuentaActual = login(cuentas)   # Aquí paso 'cuentas' y se busca obtener el numero de cuenta
            cuentaActual = cuentas.get(numeroCuentaActual)      # Aqui con el numero de cuenta se busca la cuenta en el diccionario    
            if cuentaActual:
                opcCliente = 10
                while opcCliente != 0:
                    opcCliente = menuCliente()
                    if opcCliente == 1:
                        print('\nConsignar a otra cuenta')
                        consignarDestinatario(cuentaActual, cuentas, movimientos, numeroCuentaActual)
                    
                    elif opcCliente == 2:
                        print('\nRetirar de su cuenta\n')
                        retirarDinero(cuentaActual, movimientos, numeroCuentaActual)
                    
                    elif opcCliente == 3:
                        print('\nPagar servicios\n')
                        pagarServicios(cuentaActual, movimientos, numeroCuentaActual)

                    elif opcCliente == 4:
                        print('\nConsultar movimientos\n')
                        consultarMovimientos(numeroCuentaActual, movimientos)

                    # Estas son funciones de prueba, para ver si guarda las cuentas (no son parte del ejercicio)
                    elif opcCliente == 5:
                        mostrarCuenta(cuentas)

                    # Esta tambien es otra opcion de pruebas 
                    elif opcCliente == 6:
                        print(movimientos)
                        print(cuentas)
                        print(cuentaActual)

                    elif opcCliente == 0:
                        print('\nSaliendo...')
                    
                    else:
                        print('\nEscoja una opción válida\n')
            else:
                print('\nDatos incorrectos, verifíquelos\n')
        elif opc == 0:
            print('\nSaliendo...')
            exit()
        else:
            print('\nEscoja 0 a 3\n ')
    except ValueError:
        print('\nLa opcion tiene que ser un numero\n')
