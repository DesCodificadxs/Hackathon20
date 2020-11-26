import os
import time
import sys

print("""
______________    ___  
| ___ \ ___ \ \  / /  
| |_/ / |_/ /\ \/ / /\ 
| ___ \ ___ \ \  / /  \ 
| |_/ / |_/ /  \/ / /\ \\
\____/\____/     / /  \ \\
             CHIQUIBANCO                         
                          
""")
time.sleep(3)
os.system("clear")
opcion = ()
nombre = ()
apellidos = ()
nombre2 = ()
apellidos2 = ()

print("¿Eres cliente nuevo o cliente antiguo?")
print("1. Cliente Nuevo")
print("2. Cliente Antiguo")
print("")
opcion = input("Selecciona una opcion: ")
os.system("clear")

if opcion is "1":
    try:
        print("1. Cliente Nuevo")
        print("")
        nombre = input("Nombre del niño: ")
        apellidos = input("Apellidos del niño: ")
        os.system("clear")
        conversion = input("¿Cuantos puntos son 1 euro?: ")
        paga = input("¿Cada cuantos dias recibirá la paga?: ")
        numerocuenta = input("Número de cuenta desde la que desea emitir la paga al niño: ")
        time.sleep(3)
        os.system("clear")
        print("Resumen de la información aportada:")
        time.sleep(3)
        print(nombre, apellidos)
        print("Número de cuenta desde la que realziará el pago: ", numerocuenta)
        print("El pago se realizará cada", paga, " días.")
        print("1 punto ganado equivale a ", 1/int(conversion), " euros")
        time.sleep(10)
        os.system("clear")
    except Exception:
        pass

else:
    print("""
         ▄              ▄
        ▌▒█           ▄▀▒▌
        ▌▒▒▀▄       ▄▀▒▒▒▐
       ▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐         OINK!!!!
    ▄▄▀▒▒▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐
   ▄▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀██▀▒▌
  ▐▒▒▒▄▄▄▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄▒▒▌
  ▌▒▒▐▄█▀▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐
  ▒▒▒▒▒▒▒▒▒▒▒▌██▀▒▒▒▒▒▒▒▒▀▄▌
 ▌▒▀▄██▄▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▌
 ▌▀▐▄█▄█▌▄▒▀▒▒▒▒▒▒░░░░░░▒▒▒▐
▐▒▀▐▀▐▀▒▒▄▄▒▄▒▒▒▒▒░░░░░░▒▒▒▒▌
▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒░░░░░░▒▒▒▐
 ▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒▒▒░░░░▒▒▒▒▌
 ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐
  ▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▌
    ▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀
   ▐▀▒▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀
   ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀""")
    sys.exit("Y tu pa ke kiereh sabeh eso.")
    

print("Quieres añadir mas hijos al sistema?: ")
mashijos = input("S/N: ")

if mashijos.upper() == "S":
        nombre2 = input("Nombre del niño/a: ")
        apellidos2 = input("Apellidos del niño/a: ")
        os.system("clear")
        conversion2 = input("¿Cuantos puntos son 1 euro?: ")
        paga2 = input("¿Cada cuantos dias recibirá la paga?: ")
        numerocuenta2 = input("Número de cuenta desde la que desea emitir la paga al niño: ")
        time.sleep(3)
        os.system("clear")
        print("Resumen de la información aportada:")
        time.sleep(3)
        print(nombre2, apellidos2)
        print("Número de cuenta desde la que realziará el pago: ", numerocuenta2)
        print("El pago se realizará cada", paga2, " días.")
        print("1 punto ganado equivale a ", 1/int(conversion2), " euros")
        time.sleep(10)
        os.system("clear")
else:
    pass
print("¿Sobre que niño quieres operar en CHIQUIBANCO?")
print(" 1. ",nombre,apellidos,"\n","2. ",nombre2,apellidos2)
eleccionniño = input("Eleccion: ")
os.system("clear")
if eleccionniño == "1":
    print(nombre, apellidos)
    print("")
    saldo = "0"
    print("")
    print("PRODUCTOS ASOCIABLES")
    print("1. Chiquicuenta")
    print("2. Chiquiprestamo")
    producto = input("Selecciona un producto para añadir: ")
    os.system("clear")
    if producto == "1":
        print(nombre, apellidos)
        print("PRODUCTOS ASOCIADO:")
        print("1. Chiquicuenta      Saldo:", saldo)
        print("")
        print("PRODUCTOS ASOCIABLES")
        print("2. Chiquiprestamo")
        producto = input("Selecciona producto para añadir: ")
        if producto == "2":
            os.system("clear")
            print("CHIQUIPRESTAMOS")
            print("")
            print(nombre,apellidos)
            tareas = ()
            objetivo = ()
            print("""
            OBJETIVOS:
            TAREAS:""")
            objetivo = input("¿Que objetivo quieres añadir para el prestamo? (Bicicleta, Consola, Viaje...: ")
            objetivopuntos = input("¿Cuantos puntos vale este objetivo? ")
            os.system("clear")
            print(nombre,apellidos)
            print("OBJETIVOS: ", objetivo, "y son ",objetivopuntos, "puntos para conseguirlo.")
            print("TAREAS: ")
            print("1. Hacer la cama         2 puntos.")
            print("2. Sacar al perro            3 puntos")
            print("3. Recoger la mesa despues de comer          3 puntos")
            tareas = input("¿Que tareas quieres asociar al objetivo? ")
            if tareas == "1":
                tareas = "1. Hacer la cama         2 puntos."
                os.system("clear")
                print(nombre,apellidos)
                print("OBJETIVOS: ",objetivo)
                print("TAREAS:\n",tareas)
                print("")
                print("Conseguirás tu objetivo en ", (int(objetivopuntos)/2)*int(paga), "días. ")
            if tareas == "2":
                tareas = "2. Sacar al perro            3 puntos"
                os.system("clear")
                print(nombre,apellidos)
                print("OBJETIVOS: ",objetivo)
                print("TAREAS:\n",tareas)
                print("")
                print("Conseguirás tu objetivo en ", (int(objetivopuntos)/3)*int(paga), "días. ")
            if tareas == "3":
                tareas = "3. Recoger la mesa despues de comer          3 puntos"
                os.system("clear")
                print(nombre,apellidos)
                print("OBJETIVOS: ",objetivo)
                print("TAREAS:\n",tareas)
                print("")
                print("Conseguirás tu objetivo en ", (int(objetivopuntos)/3)*int(paga), "días. ")

            
    if producto == "2":
        os.system("clear")
        print("CHIQUIPRESTAMOS")
        print("")
        print(nombre,apellidos)
        tareas = ()
        objetivo = ()
        print("""
        OBJETIVOS:
        TAREAS:""")
        objetivo = input("¿Que objetivo quieres añadir para el prestamo? (Bicicleta, Consola, Viaje...: ")
        objetivopuntos = input("¿Cuantos puntos vale este objetivo? ")
        os.system("clear")
        print(nombre,apellidos)
        print("OBJETIVOS: ", objetivo, "y son ",objetivopuntos, "puntos para conseguirlo.")
        print("TAREAS: ")
        print("1. Hacer la cama         2 puntos.")
        print("2. Sacar al perro            3 puntos")
        print("3. Recoger la mesa despues de comer          3 puntos")
        tareas = input("¿Que tareas quieres asociar al objetivo? ")
        if tareas == "1":
            tareas = "1. Hacer la cama         2 puntos."
            os.system("clear")
            print(nombre,apellidos)
            print("OBJETIVOS: ",objetivo)
            print("TAREAS:\n",tareas)
            print("")
            print("Conseguirás tu objetivo en ", (int(objetivopuntos)/2)*int(paga), "días. ")
        if tareas == "2":
            tareas = "2. Sacar al perro            3 puntos"
            os.system("clear")
            print(nombre,apellidos)
            print("OBJETIVOS: ",objetivo)
            print("TAREAS:\n",tareas)
            print("")
            print("Conseguirás tu objetivo en ", (int(objetivopuntos)/3)*int(paga), "días. ")
        if tareas == "3":
            tareas = "3. Recoger la mesa despues de comer          3 puntos"
            os.system("clear")
            print(nombre,apellidos)
            print("OBJETIVOS: ",objetivo)
            print("TAREAS:\n",tareas)
            print("")
            print("Conseguirás tu objetivo en ", (int(objetivopuntos)/3)*int(paga), "días. ")

if eleccionniño == "2":
    print(nombre2, apellidos2)
    print("")
    saldo = "0"
    print("")
    print("PRODUCTOS ASOCIABLES")
    print("1. Chiquicuenta")
    print("2. Chiquiprestamo")
    producto2 = input("Selecciona un producto para añadir: ")
    os.system("clear")
    if producto2 == "1":
        print(nombre2, apellidos2)
        print("PRODUCTOS ASOCIADO:")
        print("1. Chiquicuenta      Saldo:", saldo2)
        print("")
        print("PRODUCTOS ASOCIABLES")
        print("2. Chiquiprestamo")
        producto2 = input("Selecciona producto para añadir: ")
        if producto2 == "2":
            os.system("clear")
            print("CHIQUIPRESTAMOS")
            print("")
            print(nombre2,apellidos2)
            tareas2 = ()
            objetivo2 = ()
            print("""
            OBJETIVOS:
            TAREAS:""")
            objetivo2 = input("¿Que objetivo quieres añadir para el prestamo? (Bicicleta, Consola, Viaje...: ")
            objetivopuntos2 = input("¿Cuantos puntos vale este objetivo? ")
            os.system("clear")
            print(nombre2,apellidos2)
            print("OBJETIVOS: ", objetivo2, "y son ",objetivopuntos2, "puntos para conseguirlo.")
            print("TAREAS: ")
            print("1. Hacer la cama         2 puntos.")
            print("2. Sacar al perro            3 puntos")
            print("3. Recoger la mesa despues de comer          3 puntos")
            tareas2 = input("¿Que tareas quieres asociar al objetivo? ")
            if tareas2 == "1":
                tareas2 = "1. Hacer la cama         2 puntos."
                os.system("clear")
                print(nombre2,apellidos2)
                print("OBJETIVOS: ",objetivo2)
                print("TAREAS:\n",tareas2)
                print("")
                print("Conseguirás tu objetivo en ", (int(objetivopuntos2)/2)*int(paga2), "días. ")
            if tareas2 == "2":
                tareas2 = "2. Sacar al perro            3 puntos"
                os.system("clear")
                print(nombre2,apellidos2)
                print("OBJETIVOS: ",objetivo2)
                print("TAREAS:\n",tareas2)
                print("")
                print("Conseguirás tu objetivo en ", (int(objetivopuntos2)/3)*int(paga2), "días. ")
            if tareas2 == "3":
                tareas2 = "3. Recoger la mesa despues de comer          3 puntos"
                os.system("clear")
                print(nombre2,apellidos2)
                print("OBJETIVOS: ",objetivo2)
                print("TAREAS:\n",tareas2)
                print("")
                print("Conseguirás tu objetivo en ", (int(objetivopuntos2)/3)*int(paga2), "días. ")

            
    if producto == "2":
        os.system("clear")
        print("CHIQUIPRESTAMOS")
        print("")
        print(nombre2,apellidos2)
        tareas2 = ()
        objetivo2 = ()
        print("""
        OBJETIVOS:
        TAREAS:""")
        objetivo2 = input("¿Que objetivo quieres añadir para el prestamo? (Bicicleta, Consola, Viaje...: ")
        objetivopuntos2 = input("¿Cuantos puntos vale este objetivo? ")
        os.system("clear")
        print(nombre2,apellidos2)
        print("OBJETIVOS: ", objetivo2, "y son ",objetivopuntos2, "puntos para conseguirlo.")
        print("TAREAS: ")
        print("1. Hacer la cama         2 puntos.")
        print("2. Sacar al perro            3 puntos")
        print("3. Recoger la mesa despues de comer          3 puntos")
        tareas2 = input("¿Que tareas quieres asociar al objetivo? ")
        if tareas2 == "1":
            tareas2 = "1. Hacer la cama         2 puntos."
            os.system("clear")
            print(nombre2,apellidos2)
            print("OBJETIVOS: ",objetivo2)
            print("TAREAS:\n",tareas2)
            print("")
            print("Conseguirás tu objetivo en ", (int(objetivopuntos2)/2)*int(paga2), "días. ")
        if tareas2 == "2":
            tareas2 = "2. Sacar al perro            3 puntos"
            os.system("clear")
            print(nombre2,apellidos2)
            print("OBJETIVOS: ",objetivo2)
            print("TAREAS:\n",tareas2)
            print("")
            print("Conseguirás tu objetivo en ", (int(objetivopuntos2)/3)*int(paga2), "días. ")
        if tareas2 == "3":
            tareas2 = "3. Recoger la mesa despues de comer          3 puntos"
            os.system("clear")
            print(nombre2,apellidos2)
            print("OBJETIVOS: ",objetivo2)
            print("TAREAS:\n",tareas2)
            print("")
            print("Conseguirás tu objetivo en ", (int(objetivopuntos2)/3)*int(paga2), "días. "
