from multipledispatch import dispatch 

class Videojuego:
    @dispatch(str , str, int)
    def __init__ (self,n,p,cj):
        self.nombre = n
        self.plataforma = p
        self.cantJugadores = cj
        
    @dispatch()
    def __init__ (self):
        self.nombre = "free fire"
        self.plataforma = "android"
        self.cantJugadores = 1
        
    @dispatch(str,str)
    def __init__ (self , n,p):
        self.nombre = n
        self.plataforma = p
        self.cantJugadores = 3
        
    @dispatch()
    def mostrar(self):
        print("---------videojuego---------")
        print("Nombre:", self.nombre)
        print("Plataforma:", self.plataforma)
        print("Cantidad de Jugadores:", self.cantJugadores)
        
    @dispatch()
    def agregarJugador(self):
        self.cantJugadores += 1
        print("Se agregó un jugador.")
        print("Cantidad de Jugadores:", self.cantJugadores)
    
    @dispatch(int)
    def agregarJugador(self, cant):
        self.cantJugadores += cant
        print("Se agregaron", cant, "jugadores.")
        print("Cantidad de Jugadores:", self.cantJugadores)
        
        
a=Videojuego("FIFA 23", "PS5", 1)
a.mostrar()
a.agregarJugador()
a.agregarJugador(3)


b=Videojuego("Call of Duty", "PC", 4)
b.mostrar()
b.agregarJugador()
b.agregarJugador(2)

   
c=Videojuego() 
c.mostrar()
c.agregarJugador()
c.agregarJugador(2)


d=Videojuego("League of Legends", "PC")
d.mostrar()
d.agregarJugador()
d.agregarJugador(2)
