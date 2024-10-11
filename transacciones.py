from utils import generarReferencia
import datetime
# Consignar dinero a la cuenta del usuario logueado
def consignarDinero(cuentas, movimientos):
    numeroCuenta = str(input("Ingrese cuenta a consignar: "))
    
    # Verificamos si la cuenta existe
    if numeroCuenta in cuentas:
        valor = int(input("\nCuánto desea consignar a su cuenta: "))
        if valor <= 0:
            print("\nEl valor debe ser mayor a 0")
        cuentas[numeroCuenta]["saldo"] += valor  # actualizamos el saldo en la cuenta correspondiente
        movimientos[numeroCuenta].append({
            "tipo": "Consignacion", 
            "valor": valor, 
            "referencia": generarReferencia(), 
            "descripcion": "Consignacion a su cuenta bancaria",
            "fecha y hora": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")       #lo que hace el strftime es poder poner formato
        })
        print(f"\nConsignación exitosa. Su nuevo saldo es: {cuentas[numeroCuenta]['saldo']}")
    else:
        print(f"La cuenta {numeroCuenta} no existe.")

# Consignar dinero a otra cuenta por número de cuenta o documento
def consignarDestinatario(cuentaOrigen, cuentas, movimientos, numeroCuentaActual):
    opc = int(input("1. Consignar por número de cuenta\n2. Consignar por número de documento\nSeleccione una opción: "))
    
    if opc == 1:
        numeroCuenta = str(input('\nDigite el número de cuenta del destinatario: '))
        cuentaDestinatario = cuentas.get(numeroCuenta)

    elif opc == 2:
        numeroDocumento = int(input('\nDigite el número de documento del destinatario: '))
        cuentaDestinatario = next((cuenta for cuenta in cuentas.values() if cuenta["documento"] == numeroDocumento), None)   # El None se pone para no generar un error si no se encuentra la cuenta
    else:
        print("\nOpción no válida")
        return
    
    if cuentaDestinatario:
        valor = int(input(f'\nCuánto desea consignar a la cuenta de {cuentaDestinatario["nombre"]}: '))
        if valor > cuentaOrigen["saldo"]:
            print("\nFondos insuficientes para realizar la consignación")
        elif  valor <= 0:
            print("\nEl valor a consignar debe ser mayor a cero")
        else:
            cuentaOrigen["saldo"] -= valor
            cuentaDestinatario["saldo"] += valor
            movimientos[numeroCuentaActual].append({
                "tipo": "Transferencia", 
                "valor": valor, 
                "referencia": generarReferencia(), 
                "descripcion": f"Transferencia a cuenta de {cuentaDestinatario['nombre']}",
                "fecha y hora": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
            print(f"\nConsignación exitosa. Su nuevo saldo es: {cuentaOrigen['saldo']}")
    else:
        print("\nCuenta no encontrada")

# Retirar dinero de la cuenta logueada
def retirarDinero(cuenta, movimientos, numeroCuentaActual):
    valor = int(input("\nCuánto desea retirar de su cuenta: "))
    if valor > cuenta["saldo"]:
        print("\nFondos insuficientes")
    elif  valor <= 0:
        print("\nEl valor a retirar debe ser mayor a cero")
    else:
        cuenta["saldo"] -= valor
        movimientos[numeroCuentaActual].append({"tipo": "Retiro", 
                                                "valor": valor, 
                                                "referencia": generarReferencia(), 
                                                "descripcion": "Retiro de cuenta", 
                                                "cuenta": numeroCuentaActual,
                                                "fecha y hora": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
        print(f"\nRetiro exitoso. Su nuevo saldo es: {cuenta['saldo']}")

# Pagar servicios
def pagarServicios(cuenta, movimientos, numeroCuentaActual):
    print("Seleccione el servicio que desea pagar:\n1. Agua\n2. Gas\n3. Energía")
    servicios = {1: "Agua", 2: "Gas", 3: "Energía"}
    opc = int(input("Ingrese su opción: "))
    
    # Nuestro menu es un diccionario ya que solo se necesita el nombre del servicio
    if opc in servicios:
        referencia = str(input("Ingrese la referencia del recibo: "))
        valor = int(input("Ingrese el valor del recibo: "))
        
        if valor > cuenta["saldo"]:
            print("\nFondos insuficientes para pagar el servicio")
        elif valor <= 0:
            print("\nEl valor del recibo debe ser mayor a cero")
        else:
            cuenta["saldo"] -= valor
            movimientos[numeroCuentaActual].append({"tipo": "Pago Servicio", 
                                                    "valor": valor, 
                                                    "referencia": referencia, 
                                                    "descripcion": f"Pago de servicio de {servicios[opc]}", 
                                                    "cuenta": numeroCuentaActual,
                                                    "fecha y hora": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
            print(f"\nPago exitoso. Su nuevo saldo es: {cuenta['saldo']}")
    else:
        print("\nOpción no válida")
