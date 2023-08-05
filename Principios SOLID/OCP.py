class Notificador:
    def __init__(self, usuario, notificacion):
        self.usuario = usuario
        self.notificacion = notificacion
    
    def notificar(self):
        #raise sirve para lanzar una excepcion (error)
        raise NotImplementedError("Notificar no esta implementado")
    
class NotificacionEmail(Notificador):
    def Notificar(self):
        print(f"Enviando email a {self.usuario.email}")
        
class NotificacionSMS(Notificador):
    def Notificar(self):
        print(f"Enviando SMS a {self.usuario.sms}")