class Persona:
    def __init__(self, n, e, c):
        self.nombre = n
        self.edad = e
        self.ciudad = c

    def mostrarsaludo(self):
        print("Hola soy", self.nombre, "de", self.ciudad)

    def mayorDeEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False

a = Persona("Juan", 20, "Lima")
a.mostrarsaludo()
print(a.mayorDeEdad())
b= Persona("Pedro", 15, "Lima")
b.mostrarsaludo()
print(b.mayorDeEdad())
c= Persona("Maria", 17, "Lima")
c.mostrarsaludo()  
print(c.mayorDeEdad())
