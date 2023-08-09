class CuentaBancaria:
    def __init__(self, titular, cantidad, saldo):
        self.titular = titular
        self.cantidad = cantidad
        self.__saldo = saldo
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
        
        
    def imprimir(self):
        print("Titular:", self.titular)
        print("Cantidad:", self.cantidad)
        print("Saldo:", self.saldo)
        
        
cuenta = CuentaBancaria("Saul", 1000, 500)
cuenta.imprimir()
    
