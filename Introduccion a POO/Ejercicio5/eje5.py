class Estudiante:
    def __init__(self, n,n1,n2):
        self.nombre=n
        self.nota_1=n1
        self.nota_2=n2
    def promedio(self):
        prom=(self.nota_1+self.nota_2)/2
        print(prom)
        return prom
    def aprobo(self):
        if self.promedio() >= 6:
            print(self.nombre,"Aprobo")
        else:
            print( self.nombre, "No aprobo")
        
        
a=Estudiante("Juan",8,7)
a.promedio()
a.aprobo()
b=Estudiante("Pedro",5,4)
b.promedio()
b.aprobo()
c=Estudiante("Maria",7,8)
c.promedio()
c.aprobo()