numero_1 = int(input("Ingrese el primer número entero: "))
numero_2 = int(input("Ingrese el segundo número entero: "))

if(numero_1 > numero_2):
    print("{} es mayor a {}".format(numero_1,numero_2))
    if(numero_1 % 2 == 0):
        print("El número es par")
    else: 
        print("El número es impar")
elif(numero_1 < numero_2):
    print("{} es mayor a {}".format(numero_2, numero_1))
    if(numero_2 % 2 == 0): 
        print("El número es par")
    else:
        print("El número es impar")
else: 
    print("Los numeros ingresados son iguales")
print("---------------------------------------------")
usuario = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")
if(usuario == "admin" and password == "12345"):
    print("Acceso correcto")
else:
    print("acceso denegado")