class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return (self.base+self.altura)*2

class Cuadrado(Rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado)

if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=4)
    print("Área del rectángulo: ", rectangulo.area())
    rectangulo = Rectangulo(base=3, altura=4)
    print("Perimetro del rectángulo: ", rectangulo.perimetro())

    cuadrado = Cuadrado(lado=5)
    print("Área del cuadrado: ", cuadrado.area())
    print("Perimetro del cuadrado: ", cuadrado.perimetro())