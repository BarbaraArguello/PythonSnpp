#Calculo de imc (índice de masa corporal)
peso = float(input('Ingrese su peso en kilogramos: '))
altura = float(input('Ingrese su altura en metros: '))
imc = peso/altura**2
print ('Su imc es', imc)