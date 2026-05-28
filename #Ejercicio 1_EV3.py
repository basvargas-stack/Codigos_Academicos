#Ejercicio 1
import time

def Validar_contraseña(contraseña):
    
    #Parametros generales
    Largo_min = 8
    Largo_maximo = 16
    Min_num = 1
    Min_letra = 1
    Max_Caracter_especial = 1
    Max_espacios = 0

    #Caracteres especiales permitidos
    Especiales = "-_*.!?#$%"
    ultimo_caracter = contraseña[-1]

    #Contadores
    Largo = len(contraseña)
    contador_num = 0
    contador_letra = 0
    contador_Especial = 0
    contador_espacio = 0

    if Largo < Largo_min or Largo > Largo_maximo:
        print("La contraseña debe ser de minimo 8 caracteres y maximo 16")
        return "Contreseña invalida"
    
    if ultimo_caracter in Especiales:
        print("La contraseña no puede teminar en un caracter especial")
        return "Contraseña invalida"
    
    
    for caracter in (contraseña):
        if caracter.isdigit():
            contador_num += 1
        if caracter in Especiales:
            contador_Especial += 1
        elif caracter.isspace():
            contador_espacio += 1
    
    if (contador_num >= Min_num and contador_Especial <= Max_Caracter_especial) and contador_espacio == Max_espacios:
        return "Contraseña valida"
    else:
        if contador_num < Min_num:
            print("Al menos debe haber un 1 numero")
        if contador_Especial > Max_Caracter_especial:
            print("No más de un caracter especial")
        if contador_espacio > Max_espacios:
            print("La contraseña no debe tener espacios")
        return "Contraseña invalida"

while True:
    print()
    print("|==== Registro de contraseña ====|")
    print("Ingrese una contraseña: ")
    contraseña = input(":")
    print()
    
    if Validar_contraseña(contraseña) == "Contraseña valida":
        print()
        print("Contraseña valida")
        print("Contraseña registrada con éxito")
        time.sleep(1)
        break
    else:
        print()
        print("Pruebe de nuevo")






