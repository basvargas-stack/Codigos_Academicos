#Maquina de bebidas

import time

Inventario = {
    "Coca Cola": 1000 ,
    "Pepsi":  1000 ,
    "Fanta":  1000 ,
    "Becker":  2000 ,
    "Heineken":  2100 
    }

def Bebidas():
    contador = 1
    for key, value in Inventario.items():
        print(f"{contador} ) {key}| Precio: $ {value}")
        contador += 1

def Menú_Bebidas():
    lista_Bebidas = []
    opc = 999999
    Total = 0
    print("---Menú---")
    while opc != 0:
        Bebidas()
        print("Presione 0 para Terminar el pedido")
        print("Eliga un producto")
        opc = int(input(":"))
        nombres_Bebidas = list(Inventario.keys())
        precios_Bebidas = list(Inventario.values())
        match opc:
            case 1:
                lista_Bebidas.append(nombres_Bebidas[0])
                print("Se ha sumado ", Inventario["Coca Cola"])
                print()
                Total += precios_Bebidas[0]
                

            case 2:
                lista_Bebidas.append(nombres_Bebidas[1])
                print("Se ha sumado ", Inventario["Pepsi"])
                print()
                Total += precios_Bebidas[1]
                

            case 3:
                lista_Bebidas.append(nombres_Bebidas[2])
                print("Se ha sumado ", Inventario["Fanta"])
                print()
                Total += precios_Bebidas[2]
                

            case 4:
                lista_Bebidas.append(nombres_Bebidas[3])
                print(f"Se ha sumado ", Inventario["Becker"])
                print()
                Total += precios_Bebidas[3]
            
            case 5:
                lista_Bebidas.append(nombres_Bebidas[4])
                print(f"Se ha sumado ", Inventario["Heineken"])
                print()
                Total += precios_Bebidas[4]

            case 0:
                print()
                print("Pedido finalizado")
            case _:
                print("Opcion invalida")


        print(f"Monto acumulado: ", Total)

    return lista_Bebidas, Total
        


def Menú_main():
    Lista_Main = []
    opc = 9999
    opc2 = 9999
    Total_Main = 0
    while opc != 0:
        print()
        print("1)Realizar pedido\n2)Listado de productos\n3)Pagar\n4)Eliminar producto\n5)Cancelar pedido")
        print()
        print("Seleccione una opción: ")
        opc = int(input(":"))
        match opc:
            case 1:
                Lista_Main, Total_Main = Menú_Bebidas()
            case 2:
                print(Lista_Main)
            case 3:
                print("El total a pagar es: ", "$", Total_Main)
                print("Procesando pago...")
                time.sleep(1)
                print("¡Pago completado!\n¡Hasta pronto!")
                break
            case 4:
                print(Lista_Main)
                print("Ingrese el nombre de un producto que desea eliminar: ")
                print("Ingrese 0 para terminar")
                opc2 = input(":")
                while opc2 != 0:
                    match opc2:
                        case "Coca Cola":
                            Lista_Main.remove("Coca Cola")
                            Total_Main -= 1000
                        case "Pepsi":
                            Lista_Main.remove("Coca Cola")
                            Total_Main -= 1000
                        case "Fanta":
                            Lista_Main.remove("Coca Cola")
                            Total_Main -= 1000
                        case "Becker":
                            Lista_Main.remove("Coca Cola")
                            Total_Main -= 2000
                        case "Heineken":
                            Lista_Main.remove("Coca Cola")
                            Total_Main -= 2100
                    print("Su nuevo total es: ", Total_Main)
            case 5:
                print("Cancelando pedido...")
                time.sleep(1)
                print("Pedido cancelado con exito, hasta pronto!!")
                break
                    
                        

                

    
Menú_main()