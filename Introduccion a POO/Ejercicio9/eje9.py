class ComponentesComputadora:
    def __init__(self, estado, placa, ram, procesador, gpu, disco):
        self.estado = estado
        self.placa = placa
        self.ram = ram
        self.procesador = procesador
        self.gpu = gpu
        self.disco = disco
    def mostrar(self):
        print("Componentes de la computadora:")
        print("Estado:", self.estado)
        print("Placa:", self.placa)
        print("RAM:", self.ram)
        print("Procesador:", self.procesador)
        print("GPU:", self.gpu)
        print("Disco:", self.disco)
    def inicializarComponentes(self):
        self.estado = "encendido"
        self.placa = "Asus"
        self.ram = 16
        self.procesador = "Intel i7"
        self.gpu = "Nvidia"
        self.disco = 512
       
    def mostrarEstado(self):
        if self.estado == "encendido":
            print("La computadora está encendida")
        else:
            print("La computadora está apagada")

    def encenderyApagar(self, m):
        if m == "encender":
            self.estado = "encendido"
            print("La computadora se encendió")
        else:
            self.estado = "apagado"
            print("La computadora se apagó")

a = ComponentesComputadora("apagado", "Asus", 16, "Intel i7", "Nvidia", 512)
a.mostrar()
a.mostrarEstado()
a.encenderyApagar("encender")

