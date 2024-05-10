#funciones matematicas

def suma(a,b):
        return a+b
        #pass     # es igual a escribir return (0), retornar vacío
def resta(a,b):
        return a-b
def multiplicacion(a,b):
        return a*b
def division(a,b):
    if(b == 0):
        return "No se puede dividir entre Cero"
    else:
        return a/b
def raiz(a,b=2):
         return a**(1/b)
         
# Cuando ejecutamos el script, __name__ para ser igual al string '__main__'
if __name__ == '__main__':
    a = int(input("Ingrese el primer numero"))
    b = int(input("Ingrese el segundo numero"))

    print("La suma de", a, "y", b," es", suma(a,b))
    print("La resta de 3 y 4 es", resta(3,4))
    print("La multiplicación de 3 por 4 es", multiplicacion(3,4))
    print("La division de 3 entre 4 es", division(3,4))
    print("La raiz de 4ta de 3 es ", raiz(3,4)) 
    
   