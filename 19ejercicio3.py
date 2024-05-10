# Operadores aritméticos
# Imprimir la suma de 3+4
print("La suma de 10 + 4 es:", 10+4)
#Resolver todas las operaciónes: 10-4, 10*4, 10/4, 10%4, 10//4, 10**4
print("La resta de 10 - 4 es:", 10-4) #RESTA
print("La producto de 10 por 4 es:", 10+4) #MULTIPLICACIÓN
print("La división de 10 entre 4 es:", 10/4) #DIVISIÓN
print("El resto de divir 10 entre 4 es:", 10%4) #RESTO
print("La cociente de dividir 10 entre 4 es:", 10//4) #COCIENTE
print("La potencia 10 a la 4ta es:", 10**4) #POTENCIA

# Resolver la ecuación cuadrática: 2x^{2}-7x+3=0
a = 2
b = -7
c = 3
print("La primera raíz es:",(-b+(b**2-4*a*c)**(1/2))/(2*a))
print("La segunda raíz es:",(-b-(b**2-4*a*c)**(1/2))/(2*a))

#Operadores con cadena de texto
print("SNPP" + "PROGRAMACIÓN PYTHON")
print("AULA" + str(2102)) #AQUI HAY UN ERROR , 2102 NO ES UNA CADENA DE TEXTO usar str()

##operaciones mixtas
print("Tun chi" * 5)
print("Ja" * (2**3))

##operadores de comparación
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

#Operaciones con cadenas de texto
print("python" > "PYTHON")
print("aaaa" >= "abaa") # ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa")) # cuneta de caracteres
print("python" != "PYTHON")

### Operadores Lógicos
print(10>4 and "Z">"A")
print(10>4 or "Z">"A")
print(not(10>4) and "Z">"A")

