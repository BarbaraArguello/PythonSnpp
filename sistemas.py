class Persona:
    nombre = None
    edad = None
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar(self):
        return f"{self.nombre}, edad: {self.edad}"

class Empleado(Persona):
    sueldo_bruto = None

    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo_bruto = sueldo

    def mostrar(self):
        return super().mostrar() + f" SN: {self.calcular_salario_neto()}"

    def calcular_salario_neto(self):
        return self.sueldo_bruto * 0.9

class Cliente(Persona): 
    telefono = None

    def __init__(self, nombre, edad, telefono):
        super().__init__(nombre, edad)
        self.telefono = telefono
    
    def mostrar(self):
        return super().mostrar() + f" Teléfono: {self.telefono}"
   
class Directivo(Empleado):
    categoria = None

    def __init__(self, nombre, edad, sueldo, categoria):
        super().__init__(nombre, edad, sueldo)
        self.categoria = categoria

    def mostrar(self):
        return super().mostrar() + f" Categoría: {self.categoria}"

class Empresa:
    nombre = None

    def __init__ (self, nombre):
        self.nombre = nombre
    def mostrar(self):
        return f"{self.nombre}"


if __name__ == '__main__':
    emp = Cliente("Moises", 35, 981123456)
    print ("Cliente: ", emp.mostrar())

    emp = Empleado("Moises", 35, 2500000)
    print ("Empleado: ", emp.mostrar())

    emp = Directivo("Moises", 35, 2500000, "Director")
    print ("Directivo: ", emp.mostrar())

    emp = Empresa("SNPP")
    print ("Empresa: ", emp.mostrar())


