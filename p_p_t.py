import random
while True:
    aleatorio  = random.randrange(0,3)
    eligePc = ""
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    opcion = int(input("Elige una opción"))
    
    if opcion == 1:
        eligeUsuario = "Piedra"
    elif opcion == 2:
        eligeUsuario = "Papel"
    elif opcion == 3:
        eligeUsuario = "Tijera"
    print("Elegiste: ", eligeUsuario)

    if aleatorio == 0 :
        eligePc = "Piedra"
    elif aleatorio == 1:
        eligePc = "Papel"
    elif opcion == 2:
        eligePc = "Tijera"
    print("La máquina elijio: ", eligePc)
    print("...")

    if eligePc == "Piedra" and eligeUsuario == "Papel":
        print("¡Ganaste! papel envuelve piedra")
    elif eligePc == "Papel" and eligeUsuario == "Tijera":
        print("¡Ganaste! tijera corta papel")
    elif eligePc == "Tijera" and eligeUsuario == "Piedra":
        print("¡Ganaste! piedra machaca tijera ")
    if eligePc == "Papel" and eligeUsuario == "Piedra":
        print("Perdiste :( , papel envuelve piedra")
    elif eligePc == "Tijera" and eligeUsuario == "Papel":
        print("Perdiste :( , tijera corta papel")
    elif eligePc == "Piedra" and eligeUsuario == "Tijera":
        print("Perdiste :(  piedra machaca tijera ")
    elif eligePc == eligeUsuario:
        print("Empate")