from multipledispatch import dispatch

class Cosinero:
    
    def __init__(self,n,sm,he,sh):
        self.nombre=n
        self.sueldoMensual=sm
        self.horasExtras=he
        self.sueldoHora=sh
    
    
    @dispatch()
    def sueldoTotal(self):
        st=self.sueldoMensual+(self.horasExtras*self.sueldoHora)
        return st
    
    @dispatch()
    def mostrar(self):
        print("---------cosinero---------")
        print("Nombre:",self.nombre)
        print("Sueldo Mensual:",self.sueldoMensual)
        print("Horas Extras:",self.horasExtras)
        print("Sueldo Hora:",self.sueldoHora)
        print("Sueldo Total:",self.sueldoTotal())
        
    @dispatch(float)
    def mostrar(self, x):
        if self.sueldoMensual==x:
            print("-----------cosinero que gana igual a x sueldo----------")
            print("Nombre:",self.nombre)
            print("Sueldo Mensual:",self.sueldoMensual)
            print("Horas Extras:",self.horasExtras)
            print("Sueldo Hora:",self.sueldoHora)
            print("Sueldo Total:",self.sueldoTotal())
        else:
            print("no se encontro")
            
class Mesero:
    def __init__(self,n,sm,he,sh,p):
        self.nombre=n
        self.sueldoMensual=sm  
        self.horasExtras=he
        self.sueldoHora=sh
        self.propina=p

    @dispatch()
    def sueldoTotal(self):
        st=self.sueldoMensual+(self.horasExtras*self.sueldoHora)+self.propina
        return st
    
    @dispatch()
    def mostrar(self):
        print("---------Mesero---------")
        print("Nombre:",self.nombre)
        print("Sueldo Mensual:",self.sueldoMensual)
        print("Horas Extras:",self.horasExtras)
        print("Sueldo Hora:",self.sueldoHora)
        print("Propina:",self.propina)
        print("Sueldo Total:",self.sueldoTotal())
        
    @dispatch(float)
    def mostrar(self, x):
        if self.sueldoMensual==x:
            print("-----------mesero que gana igual x sueldo total----------")
            print("Nombre:",self.nombre)
            print("Sueldo Mensual:",self.sueldoMensual)
            print("Horas Extras:",self.horasExtras)
            print("Sueldo Hora:",self.sueldoHora)
            print("Propina:",self.propina)
            print("Sueldo Total:",self.sueldoTotal())
        else:
            print("no se encontro")
            
class Administrativo:
    def __init__(self ,n,sm,c ):
        self.nombre=n
        self.sueldoMensual=sm
        self.cargo=c
    
    @dispatch()
    def sueldoTotal(self):
        return self.sueldoMensual
    
    @dispatch()
    def mostrar(self):
        print("---------Administrativo---------")
        print("Nombre:",self.nombre)
        print("Sueldo Mensual:",self.sueldoMensual)
        print("Cargo:",self.cargo)
        print("Sueldo Total:",self.sueldoTotal())
    
    @dispatch(float)   
    def mostrar(self, x):
        if self.sueldoMensual==x:
            print("-----------administrativo que gana igual x sueldo----------")
            print("Nombre:",self.nombre)
            print("Sueldo Mensual:",self.sueldoMensual)
            print("Cargo:",self.cargo)
            print("Sueldo Total:",self.sueldoTotal())
        else:
            print("no se encontro")
            
            
a=Cosinero("Juan", 1000, 10, 50)
a.mostrar()
a.sueldoTotal()
a.mostrar(1200.0)

b=Mesero("Pedro", 1000, 10, 50, 200)
b.mostrar()
b.sueldoTotal()
b.mostrar(1200.0)

c=Mesero("Maria", 1000, 10, 50, 200)
c.mostrar()
c.sueldoTotal()
c.mostrar(1200.0)

d=Administrativo("Jose", 1000, "Gerente")
d.mostrar()
d.sueldoTotal()
d.mostrar(1200.0)

e=Administrativo("Ana", 1200, "Secretaria")
e.mostrar()
e.sueldoTotal()
e.mostrar(1200.0)
