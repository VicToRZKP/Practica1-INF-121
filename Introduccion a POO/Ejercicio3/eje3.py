class Coche:
    def __init__(self,ma,mo,v):
        self.marca=ma
        self.modelo=mo
        self.velocidad=v
    def mostrar (self):
        print (f"Marca: {self.marca}, Modelo: {self.modelo}, Velocidad: {self.velocidad}")
    def acelerar(self):
        aceleracion=self.velocidad+10
        print("Acelerando a",aceleracion)
    def frenar(self):
        frenar=self.velocidad-10
        print("Frenando a",frenar)


a=Coche("Toyota","Corolla",15)
a.acelerar()
a.frenar()
a.mostrar()
b=Coche("Ford","Focus",20)
b.acelerar()
b.frenar()
b.mostrar()
        