class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print(self.nombre, 'anda caminando')

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print(self.nombre, 'anda moviendose en su bicicleta')

if __name__ == '__main__':
    persona = Persona('Pepe')
    persona.avanza()
    ciclista =Ciclista('Juanca')
    ciclista.avanza()
