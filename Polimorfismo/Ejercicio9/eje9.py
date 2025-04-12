from multipledispatch import dispatch

class BloqueCofre:
    @dispatch(int, int, str)
    def __init__(self, c, r, t):
        self.capcidad = c
        self.resistencia = r
        self.tipo = t

    @dispatch()
    def __init__(self):
        self.capcidad = 50
        self.resistencia = 10
        self.tipo = "cofre comun"
        
    @dispatch()
    def mostrar(self):
        print("---------Bloque Cofre---------")
        print("Capacidad:", self.capcidad)
        print("Resistencia:", self.resistencia)
        print("Tipo:", self.tipo)
        
    @dispatch()
    def accion(self):
        print("El cofre se abre , Capcidad:", self.capcidad)
        
    @dispatch()
    def romper(self):
        print("El cofre se rompio")
        
    @dispatch(str)
    def colocar(self, x):
        print("El cofre se coloco en la", x)
        
class BloqueTnt:
    @dispatch(str,int)
    def __init__(self, t,d):
        self.tipo = t
        self.danio = d
        
    @dispatch()
    def __init__(self):
        self.tipo = "tnt comun"
        self.danio = 100
        
    @dispatch()
    def mostrar(self):
        print("---------Bloque Tnt---------")
        print("Tipo:", self.tipo)
        print("Daño:", self.danio)
        
    @dispatch()
    def accion(self):
        print("se activa el TNT")
        print("!explotara¡")
        
    @dispatch()
    def romper(self):
        print("El TNT se rompio")
        print("causo daño de:", self.danio)
        
    @dispatch(str)
    def colocar(self, x):
        print("El TNT se coloco en la", x)
        
class BloqueHorno:
    
    @dispatch(str,int)
    def __init__(self, c,cc):
        self.color=c
        self.capacidadcomida=cc
       
    @dispatch() 
    def __init__(self):
        self.color="cafe"
        self.capacidadcomida=10
        
    @dispatch()
    def mostrar(self):
        print("---------Bloque Horno---------")
        print("Color:", self.color)
        print("Capacidad comida:", self.capacidadcomida)
        
    @dispatch()
    def accion(self):
        print("El horno se enciende")
        print("se puede cocinar:", self.capacidadcomida, "comidas")
        
    @dispatch()
    def romper(self):
        print("El horno se rompio")
        print("se perdio comida")
        
    @dispatch(str)
    def colocar(self, x):
        print("El horno se coloco en la", x)

a = BloqueCofre()
a.mostrar()
a.accion()
a.colocar("abajo")
a.romper()

b = BloqueCofre(20, 15, "cofre")
b.mostrar()
b.accion()
b.colocar("izquierda")
b.romper()

c = BloqueTnt()
c.mostrar()
c.colocar("arriba")
c.romper()
c.accion()

d = BloqueTnt( "TNT",200)
d.mostrar()
d.colocar("debajo")
d.romper()
c.accion()

e = BloqueHorno()
e.mostrar()
e.colocar("arriba")
e.romper()
e.accion()

f = BloqueHorno()
f.mostrar()
f.colocar("abajo")
f.romper()
f.accion()
