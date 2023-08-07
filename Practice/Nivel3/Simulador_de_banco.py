#programa que simula un banco

class Cliente:
    def __init__(self, nombre, identificacion, direccion, telefono):
        self.nombre = nombre
        self.identificacion = identificacion
        self.direccion = direccion
        self.telefono = telefono
        
    def mostrar_datos_cliente(self):
        print("Nombre: ", self.nombre)
        print("Identificacion: ", self.identificacion)
        print("Direccion: ", self.direccion)
        print("Telefono: ", self.telefono)
        
  
class CuentaBancaria:
    def __init__(self, numero_de_cuenta, propietario, saldo):
        self.numero_de_cuenta = numero_de_cuenta
        self.propietario = propietario
        self.saldo = saldo
        
        
    def mostrar_datos_cuenta(self):
        print("Numero de cuenta: ", self.numero_de_cuenta)
        self.propietario.mostrar_datos_cliente()
        print("Saldo: ", self.saldo)

    
    def depositar(self, monto):
        if monto > 0: 
            self.saldo = self.saldo + monto
            print("Deposito realizado con exito")
        
    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo = self.saldo - monto
            print("Retiro realizado con exito")
        else:
            print("No se puede realizar el retiro")
        
    def transferir(self, monto, cuenta_destino):
        self.retirar(monto)
        cuenta_destino.depositar(monto)
        
        
class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []
        self.clientes = []
        
    def crear_cuenta(self, numero_de_cuenta, propietario, saldo):
        print("Creando cuenta")
        cuenta = CuentaBancaria(numero_de_cuenta, propietario, saldo)
        self.cuentas.append(cuenta)
        
    def crear_cliente(self, nombre, identificacion, direccion, telefono):
        cliente = Cliente(nombre, identificacion, direccion, telefono)
        self.clientes.append(cliente)
        
    def listar_cuentas(self):
        for cuenta in self.cuentas:
            cuenta.mostrar_datos_cuenta()
            print("***********************")
            
    def listar_cliente(self):
        for cliente in self.clientes:
            cliente.mostrar_datos_cliente()
            print("***********************")
            
    def buscar_cuenta(self, numero_de_cuenta):
        for cuenta in self.cuentas:
            if cuenta.numero_de_cuenta == numero_de_cuenta:
                return cuenta
            
        return None
    
    def buscar_cliente(self, identificacion):
        for cliente in self.clientes:
            if cliente.identificacion == identificacion:
                return cliente
            
        return None
    
    def realizar_transaccion(self):
        numero_de_cuenta = int(input("Ingrese el numero de cuenta: "))
        cuenta = self.buscar_cuenta(numero_de_cuenta)
        
        if cuenta == None:
            print("No existe la cuenta")
            return
        
        identificacion = int(input("Ingrese la identificacion: "))
        cliente = self.buscar_cliente(identificacion)
        
        if cliente == None:
            print("No existe el cliente")
            return
        
        print("1. Depositar")
        print("2. Retirar")
        print("3. Transferir")
        
        opcion = int(input("Ingrese una opcion: "))
        
        if opcion == 1:
            monto = float(input("Ingrese el monto a depositar: "))
            cuenta.depositar(monto)
        elif opcion == 2:
            monto = float(input("Ingrese el monto a retirar: "))
            cuenta.retirar(monto)
        elif opcion == 3:
            numero_de_cuenta_destino = int(input("Ingrese el numero de cuenta destino: "))
            cuenta_destino = self.buscar_cuenta(numero_de_cuenta_destino)
            
            if cuenta_destino == None:
                print("No existe la cuenta destino")
                return
            
            monto = float(input("Ingrese el monto a transferir: "))
            cuenta.transferir(monto, cuenta_destino)
        else:
            print("Opcion no valida")
            
banco = Banco("Banco de los pobres")

#mostrar opciones para el usuario
while True:
    print("1. Crear cuenta")
    print("2. Crear cliente")
    print("3. Listar cuentas")
    print("4. Realizar transaccion")
    print("5. Listar clientes")
    print("6. Salir")
    
    opcion = int(input("Ingrese una opcion: "))
    
    if opcion == 1:
        numero_de_cuenta = int(input("Ingrese el numero de cuenta: "))
        identificacion = int(input("Ingrese la identificacion del cliente: "))
        cliente = banco.buscar_cliente(identificacion)
        banco.crear_cuenta(numero_de_cuenta, cliente, 0)
        
    elif opcion == 2:
        nombre = input("Ingrese el nombre del cliente: ")
        identificacion = int(input("Ingrese la identificacion del cliente: "))
        direccion = input("Ingrese la direccion del cliente: ")
        telefono = int(input("Ingrese el telefono del cliente: "))
        banco.crear_cliente(nombre, identificacion, direccion, telefono)
        
    elif opcion == 3:
        banco.listar_cuentas()
        
    elif opcion == 4:
        banco.realizar_transaccion()
        
    elif opcion == 5:
        banco.listar_cliente()
        
    elif opcion == 6:
        
        break
    
    else:
        print("Opcion no valida")
        
        

        
        