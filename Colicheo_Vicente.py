from os import system
system("cls")

import random
comunas=("Concepcion", "Chiguayante", "Talcahuano", "Hualpen", "San Pedro")

pedido=[]

def registrar_pedido():
    dis6=0
    dis10=0
    dis20=0
    while True:
        nombre = str(input("Ingrese su nombre: "))
        if len(nombre) > 3 and nombre.isalpha():
            break
        else:
            print("Ingrese una opcion valida...")
        system("cls")
    while True:
        apellido = str(input("Ingrese su apellido: "))
        if len(apellido) > 3 and apellido.isalpha():
            break
        else:
            print("Ingrese una opcion valida...")
        system("cls")
    while True:
        print("A continuacion se presentaran las comunas disponibles.")
        print(comunas)
        print("Recuerde escribir su comuna tal cual se presenta.")
        comuna = str(input("Ingrese su comuna: "))
        if len(comuna) > 3 and comuna.isalpha() and comuna in comunas:
            system("cls")
            break
        else:
            print("Ingrese una opcion valida...")
        system("cls")
    while True: 
        op1 = int(input("""Ingrese una de las opciones
                    1. 6 Litros
                    2. 10 Litros
                    3. 20 Litros
                    0.Finalizar pedido
                       """))
        system("cls")
        if op1 <=3:
            match op1:
                case 1:
                    print("Ingresó la opnción de 6 litros.")
                    dis6=dis6+1
                case 2:
                    print("Ingresó la opnción 10 Litros.")
                    dis10=dis10+1
                case 3:
                    print("Ingresó la opción 20 Litros.")
                    dis20=dis20+1
                case 0:
                    print("Pedido finalizado...")
                    break
                case other:
                    print("Ingrese una opcion valida...")       
    id_cliente=random.randint(1000, 9999)
    pedido.append(nombre )
    pedido.append(apellido)
    pedido.append(id_cliente)
    pedido.append(comuna)
    pedido.append(dis6)
    pedido.append(dis10)
    pedido.append(dis20)
    return

def listar_pedidos():
    print(f"""
    ID pedido     Cliente           Comuna          6Lts        10Lts       20Lts
    {pedido[2]}             {pedido[0]}{pedido[1]}     {pedido[3]}     {pedido[4]}             {pedido[5]}              {pedido[6]}                                  
    """)
    system("cls")
    return

def imprimir_hojaruta():
    return

def buscar_pedido():
    buscar = int(input("Ingrese el ID del pedido que desee buscar: "))
    if buscar in pedido:
        print("Encontrado.")
        print(pedido[0,1,2,3,4,5,6])
    else:
        print("Pedido no encontrado.")
    return



while True:
    op= input("""CleanWasser
            1. Registrar pedido
            2. Listar los todos los pedidos
            3. Imprimir hoja de ruta
            4. Buscar un pedido por ID
            5. Salir del programa
            """)
    match op:
        case "1":
            registrar_pedido()
        case "2":
            listar_pedidos()
        case "3":
            imprimir_hojaruta()
        case "4":
            buscar_pedido()
        case "5":
            break
