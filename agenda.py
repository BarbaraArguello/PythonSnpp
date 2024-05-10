agenda ={} # global para todas las funciones

def cargar_agenda(nombre, telefono): #Funcion con las variables nombre y telefono
    agenda[nombre] = telefono           # agenda es el DICCIONARIO
                                        # nombre es la CLAVE y teléfono es el VALOR

def ver_agenda(): # ESTA FUNCION ES SOLO PARA IMPRIMIR
    print(agenda)

def ver_agenda_detalle():
    print("lista de contactos")
    for nombre,tel in agenda.items(): # PARA QUE SIRVE .items??????? >>> 
        print(f"{nombre} : {tel}")
############################################################# Aca recién empieza nuestro programa
if __name__ == "__main__":
    print("Agenda de Contactos")
    #cargar_agenda("Moises", "0986123456")
    #cargar_agenda("Camila", "0994654123")
    #ver_agenda()
    #ver_agenda_detalle()

    while True:
        resp = input("¿Desea agregar un contacto?: (s/n) ")
        if resp == "s":
            nombre = input("Ingrese un nombre\n")
            tel = input("Ingrese un número de teléfono\n")
            cargar_agenda(nombre, tel)
        else:
            break
    ver_agenda_detalle()

