class calculadora:
    numero1 = None
    numero2 = None
    resultado = None
    historial = None

    def __init__(self,n,m):
        self.numero1 = n
        self.numero2 = m
        self.resultado = 0
        historial = []

    def sumar(self):
        return self.numero1 + self.numero2
    def restar(self):
        return self.numero1 - self.numero2

if __name__ == "__main__":
    casio = calculadora(45,50) #declaracion e instanciación
    casio2 = calculadora(96,85)
    print("Suma: ", casio.sumar())
    print("Resta: ", casio.restar())
    print("Suma de la otra calc: ", casio2.sumar())
