from multipledispatch import dispatch
class Oficina:
    @dispatch(int,int,int)
    def __init__(self, s,esc,est):
        self.nroSillas=s
        self.nroEscritorios=esc
        self.nroEstanterias=est
        
    @dispatch()
    def __init__(self):
        self.nroSillas=10
        self.nroEscritorios=10
        self.nroEstanterias=5
        
    @dispatch()
    def mostrar(self):
        print("---------Oficina---------")
        print("Numero de Sillas:",self.nroSillas)
        print("Numero de Escritorios:",self.nroEscritorios)
        print("Numero de Estanterias:",self.nroEstanterias)
    
    @dispatch()
    def cantMuebles(self):
        return self.nroSillas+self.nroEscritorios+self.nroEstanterias
    
class Aula:
    @dispatch(str,int,int)
    def __init__(self, n,c,p):
        self.nombre=n
        self.capacidad=c
        self.pupitres=p
        
    @dispatch()
    def __init__(self):
        self.nombre="Aula 1"
        self.capacidad=100
        self.pupitres=101
    
    @dispatch()
    def mostrar(self):
        print("---------Aula---------")
        print("Nombre:",self.nombre)
        print("Capacidad:",self.capacidad)
        print("Pupitres:",self.pupitres)
        
    @dispatch()
    def cantMuebles(self):
        return self.pupitres
    
class Laboratorio:
    @dispatch(str,int,int,int)
    def __init__(self,n,c,m,s):
        self.nombre=n
        self.capacidad=c
        self.nroMesas=m
        self.nroSillas=s
        
    @dispatch()
    def __init__(self):
        self.nombre="Laboratorio 1"
        self.capacidad=150
        self.nroMesas=75
        self.nroSillas=150
        
    @dispatch()
    def mostrar(self):
        print("---------Laboratorio---------")
        print("Nombre:",self.nombre)
        print("Capacidad:",self.capacidad)
        print("Numero de Mesas:",self.nroMesas)
        print("Numero de Sillas:",self.nroSillas)
        
    @dispatch()
    def cantMuebles(self):
        return self.nroMesas+self.nroSillas
    
a=Oficina()
a.mostrar()
print("Cantidad de muebles:",a.cantMuebles())

b=Oficina(5,5,3)
b.mostrar()
print("Cantidad de muebles:",b.cantMuebles())

c=Aula()
c.mostrar()
print("Cantidad de muebles:",c.cantMuebles())

d=Aula("Aula 2",150,151)
d.mostrar()
print("Cantidad de muebles:",d.cantMuebles())

e=Laboratorio()
e.mostrar()
print("Cantidad de muebles:",e.cantMuebles())

print ("--------------------")
print("MUEBLES TOTALES: ",a.cantMuebles()+b.cantMuebles()+c.cantMuebles()+d.cantMuebles()+e.cantMuebles())