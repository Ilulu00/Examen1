from Producto import *  

def menu_principal():
    while True:
        print("°°°°°Bienvenido a supermercado Mariana y Santiago°°°°°")
        print("1.Ingresar como cliente")
        print("2.Ingresar como administrador")
        print("0.Salir")

        op:int = int(input("Ingrese la opción deseada: "))

        if(op == 1):
            menu_cliente()
        elif(op == 2):
            usuario:str = input("Ingrese su usuario: ")
            contraseña:str = input("Ingrese su contraseña: ")
            autenticacion = autenticador(usuario,contraseña)

            if(autenticacion == True):
                menu_admin()
            else:
                print("Error, usted no es admin") 
                break   
              
        elif(op == 0):
            print("Hasta luego")
            break
        else:
            print("Opción no válida, intente de nuevo") 

def menu_cliente():
    while True:
        print("")
        print("-----Menú clientes-----")
        print("1.Todos los productos")
        print("2.Frutas")
        print("3.Verduras")
        print("4.Carnes")
        print("5.Limpieza")
        print("0.Salir")
        print("")

        opC:int = int(input("Ingrese la opción deseada: "))   

        if(opC == 1):
            print("")
            verInventario("Fruta", "Verdura", "Carne", "Limpieza")
        elif(opC == 2):
            print("")
            verFruta("Fruta.txt")  
        elif(opC == 3):
            print("")
            verVerdura("Verdura.txt")    
        elif(opC == 4):
            print("")
            verCarnes("Carne.txt")   
        elif(opC == 5):
            print("")
            verLimpio("Limpieza.txt") 
        elif(opC == 0):
            print("")
            print("Hasta luego")
            break    
        else:
            print("")
            ("Opción no válida, intente de nuevo")              

def menu_admin():
    while True:
        print("")
        print("-----Menú adiministrador-----")
        print("1.Inventario")            
        print("2.Agregar producto")            
        print("3.Eliminar producto")            
        print("4.Modificar producto")       
        print("0.Salir")
        print("")

        opA:int = int(input("Ingrese la opción deseada: "))     

        if(opA == 1):
            print("")
            verInventario("Fruta", "Verdura", "Carne", "Limpieza")

        elif(opA == 2):
            opU = menu_productos()
            if(opU == 1):
                print("")
                codigo:int = int(input("Ingrese el código del producto: "))
                nombre:str = input("Ingrese el nombre del produto: ")
                precio:float = float(input("Ingrese el precio del producto: "))
                stock:int = int(input("Ingrese el stock del producto: "))
                vitaminas:str = input("Ingrese las vitaminas que contiene: ")
                Fruta.nueva_fruta(codigo,nombre,precio,stock,vitaminas)
                print("")
            elif(opU == 2):
                print("")
                codigo:int = int(input("Ingrese el código del producto: "))
                nombre:str = input("Ingrese el nombre del produto: ")
                precio:float = float(input("Ingrese el precio del producto: "))
                stock:int = int(input("Ingrese el stock del producto: "))
                conservacion:str = input("Ingrese el metodo de conservación: ")
                print("")
                Verdura.nueva_verdura(codigo,nombre,precio,stock,conservacion)
            elif(opU == 3):
                print("")
                codigo:int = int(input("Ingrese el código del producto: "))
                nombre:str = input("Ingrese el nombre del produto: ")
                precio:float = float(input("Ingrese el precio del producto: "))
                stock:int = int(input("Ingrese el stock del producto: "))
                animal:str = input("Ingrese el animal de donde proviene: ")
                print("")
                Carne.nueva_carne(codigo,nombre,precio,stock,animal)
            elif(opU == 4):
                print("")
                codigo:int = int(input("Ingrese el código del producto: "))
                nombre:str = input("Ingrese el nombre del produto: ")
                precio:float = float(input("Ingrese el precio del producto: "))
                stock:int = int(input("Ingrese el stock del producto: "))
                descripcion:str = input("Ingrese la descripción: ")
                print("")
                Limpieza.nuevo_limpieza(codigo,nombre,precio,stock,descripcion)
            elif(opU == 0):
                print("")
                print("Hasta luego")
                print("")
                break 
            else:
                print("")
                print("Opción no válida, intente de nuevo")     
                print("")

        elif(opA == 3):
            opU = menu_productos()
            if(opU == 1):
                print("")
                codigo:int = int(input("Ingrese el código del producto: "))
                Fruta.eliminar_fruta(codigo)
            elif(opU == 2):
                print("")
                codigo:int = int(input("Ingrese el código del producto: "))
                Verdura.eliminar_verdura(codigo)    
            elif(opU == 3):
                print("")
                codigo:int = int(input("Ingrese el código del producto: "))
                Carne.eliminar_carne(codigo)    
            elif(opU == 4):
                print("")
                codigo:int = int(input("Ingrese el código del producto: "))
                Limpieza.eliminar_limpieza(codigo)    
            elif(opU == 0):
                print("")
                print("Hasta luego")
                print("")
                break
            else:
                print("")
                print("Opción no válida, intente de nuevo")  
                print("")  

        elif(opA == 4):
            opU:int = menu_productos()
            if(opU == 1):
                print("")
                codigo:int = int(input("Ingrese el código del producto: "))
                campoCambiar:str = input("Ingrese el campo del valor a cambiar (nombre, precio, stock, vitaminas): ")
                Nvalor = input("Ingrese el nuevo valor: ")
                print("")
                Fruta.actualizar_fruta(codigo,campoCambiar,Nvalor)
            elif(opU == 2):
                print("")
                codigo:int = int(input("Ingrese el código del producto: "))
                campoCambiar:str = input("Ingrese el campo del valor a cambiar (nombre, precio, stock, conservacion): ")
                Nvalor = input("Ingrese el nuevo valor: ")
                print("")
                Verdura.actualizar_verdura(codigo,campoCambiar,Nvalor)   
            elif(opU == 3):
                print("")
                codigo:int = int(input("Ingrese el código del producto: "))
                campoCambiar:str = input("Ingrese el campo del valor a cambiar: (nombre, precio, stock, animalProviene): ")
                Nvalor = input("Ingrese el nuevo valor: ")
                print("")
                Carne.actualizar_carne(codigo,campoCambiar,Nvalor)  
            elif(opU == 4):
                print("")
                codigo:int = int(input("Ingrese el código del producto: "))
                campoCambiar:str = input("Ingrese el campo del valor a cambiar: (nombre, precio, stock, descripcion): ")
                Nvalor = input("Ingrese el nuevo valor: ")
                print("")
                Limpieza.actualizar_Limpieza(codigo,campoCambiar,Nvalor)   
            elif(opU == 0):
                print("")
                print("Hasta luego")
                print("")
                break
            else:
                print("")
                print("Opción no válida, intente de nuevo")    
                print("") 
        elif(opA == 0):
            print("")
            print("Hasta luego")
            print("")
            break
        else:
            print("")
            print("Opción no válida, intente de nuevo")
            print("")

def menu_productos() -> int:
    print("")
    print("1.Frutas")
    print("2.Verduras")
    print("3.Carnes")
    print("4.Limpieza")
    print("0.Salir")
    print("")

    opP:int = int(input("Ingrese la opción deseada: "))   
    print("")

    return opP

def autenticador(user: str, contraseña: str) -> bool:
    with open("Admin.txt", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue
            usuario_archivo, contraseña_archivo = linea.split(",")
            
            if user == usuario_archivo and contraseña == contraseña_archivo:
                return True
    return False

menu_principal() 