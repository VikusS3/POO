# class Pajaro:
#     def volar(self):
#         return "Puedo volar"
        
        
# class Pinguino(Pajaro):
#     def volar(self):
#         return "No puedo volar"
    
    
# def hacer_volar(pajaro = Pajaro):
#     return pajaro.volar()

# print(hacer_volar(Pinguino()))


class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "Puedo volar"
    
class AveNoVoladora(Ave):
    pass