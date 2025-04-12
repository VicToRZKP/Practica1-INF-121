from multipledispatch import dispatch

class Perro:
    @dispatch(str,int,str)
    def __init__(self,n,e,r):
        self.nombre=n
        self.edad=e
        self.raza=r
       
    @dispatch() 
    def __init__(self):
        self.nombre="pepe"
        self.edad=12
        self.raza="quqer"
        
    @dispatch()
    def mostrar(self):
        print("---------Perro---------")
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)
        print("Raza:",self.raza)
        
    @dispatch( str)
    def hacerSonido(self,x):
        if "perro"==x:
            print("el perro dice :Guau Guau")
        else:
            if "gato"==x:
                print("el gato dice: miau")
            else:
                print("el pajaro dice: pio pio")
                
    @dispatch()
    def moverse(self):
        print("el perro corre")
        
class Gato:
    @dispatch(str,str)
    def __init__(self,n,c):
        self.nombre=n
        self.color=c

    @dispatch()
    def __init__(self):
        self.nombre="fifi"
        self.color="cafe"    
    
    @dispatch()
    def mostrar(self):
        print("---------Gato---------")
        print("Nombre:",self.nombre)
        print("Color:",self.color)
        
    @dispatch()
    def hacerSonido(self):
        print("el gato dice: miau")
        
    @dispatch()
    def moverse(self):
        print("el gato camina")
        
class Pajaro:
    
    @dispatch(str,str)
    def __init__(self,n,t):
        self.nombre=n
        self.tipo=t

    @dispatch()
    def __init__(self):
        self.nombre="plumita"
        self.tipo="loro"
        
    @dispatch()
    def mostrar(self):
        print("---------Pajaro---------")
        print("Nombre:",self.nombre)
        print("Tipo:",self.tipo)
    
    @dispatch()
    def hacerSonido(self):
        print("el pajaro dice: pio pio")
        
    @dispatch()
    def moverse(self):
        print("el pajaro vuela")
        
        
a=Perro()
a.mostrar() 
a.hacerSonido("perro")
a.moverse()

b=Gato()
b.mostrar()
b.hacerSonido()
b.moverse()

c=Pajaro()
c.mostrar()
c.hacerSonido()
c.moverse()

