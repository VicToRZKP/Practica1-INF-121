class Celular:
    def __init__(self, bateria=100, espacio=1024):
        self.bateria = bateria
        self.espacio = espacio
        self.apps = [[None, None] for _ in range(20)]
        self.apps[0] = ["Galería", 100]

    def instalar(self, nombre, tamaño):
        tamaño = int(tamaño)
        if (self.espacio - tamaño) < 0:
            print("No hay espacio suficiente")
            return

        for i in range(20):
            if self.apps[i][0] is None:
                self.apps[i][0] = nombre
                self.apps[i][1] = tamaño
                self.espacio -= tamaño
                print(f"Aplicación '{nombre}' instalada.")
                print("Espacio disponible:", self.espacio)
                return

        print("No hay ranuras disponibles para instalar más aplicaciones.")

    def utilizarApp(self, nombre, tiempo):
        for i in range(20):
            if self.apps[i][0] == nombre:
                mb = self.apps[i][1]
                if mb <= 100:
                    consumo = (tiempo / 10) * 1
                elif mb <= 250:
                    consumo = (tiempo / 10) * 2
                else:
                    consumo = (tiempo / 10) * 5

                if self.bateria >= consumo:
                    self.bateria -= consumo
                else:
                    self.bateria = 0
                    print("Batería baja. El celular se apagó.")
                    return

                print(f"Usaste '{nombre}' por {tiempo} minutos.")
                print("Batería restante:", self.bateria)
                print("--------------------")
                return

        print(f"La aplicación '{nombre}' no está instalada.")

cel = Celular()
cel.instalar("Facebook", 100)
cel.instalar("Instagram", 200)
cel.instalar("Twitter", 300)

cel.utilizarApp("Facebook", 10)
cel.utilizarApp("Instagram", 20)
