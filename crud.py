import time
# id,nombre, edad
# lista, diccionario, id

lista=[]


def seleccion(): # funcion que se encargara de mostrar y solicitar la opcion
    opcion= input("""Que deseas hacer?
        1. Agregar estudiante
        2. Eliminar Estudiante
        3. Actualizar estudiante
        4. Ver estudiante
        5. Salir\n""")
    if opcion not in ["1","2","3","4", "5"]: # si la opcion no se encuentra
        print("Lo sentimos, pero esa opcion no existe") #en caso de no escoger una opcion del menu
        seleccion()
    else: 
        return opcion # retornar la opcion seleccionada
    
    
def solicitar_datos():
    while True: # control de excepciones para el id
            id=input("Ingresa el id: ")
            if id in recopilador_id(): #consulta la lista donde se encuentran los ids y en caso de que este le muestra que ya esta registrado
                print("ese id ya fue ingresado")
            else:
                break
    nombre=input("ingresa el nombre: ") #si esta bien sale y le pide el nombre y la edad
    edad= input("Ingresa la edad: ")
    create_students(lista,id,nombre,edad) # llamar la funcion create_students que almacena la informacion del estudiante en el diccionario
    
        
    
#Agregar estudiante
def create_students(lista:list,id:str,nombre:str,edad:str):
    """
    Agrega un estudiante a la lista de estudiantes.

    Args:
        lista (list): La lista donde se añadirá el estudiante. 
                    Se espera que contenga diccionarios con información de estudiantes.
        id (str): Identificador único del estudiante.
        nombre (str): Nombre del estudiante.
        edad (str): Edad del estudiante.

    Returns:
        None: Esta función no retorna un valor, solo modifica la lista proporcionada.
    """
    student = {
        "id":id,
        "nombre":nombre,
        "edad":edad
    }
    lista.append(student)
    return lista # retornar la lista con todos los diccionarios de los estudiantes


def recopilador_id(): #simplemente se crea una lista para llenarla de los ids registrados
    ides=[]
    for i in lista: # for que recorre la lista de diccionarios
        ides.append(i["id"])  # agregar el id a la lista ides
    return ides # retornar lista de ides

def eliminar(): # funcion eliminar que recibe como parametro el id del estudiante
    while True: # control de excepciones para el id
        id_eliminar= input("ingresa el id del estudiante que desea eliminar: ")
        if id_eliminar not in recopilador_id(): # verificar si el id se encuentra
            print("ese estudiante no se encuentra registrado")
        else:
            break
            
    posicion= recopilador_id().index(id_eliminar) # se determina la posicion del id del estudiante
    lista.pop(posicion) # y se elimina esa posicion de la lista de diccionarios
    print("Nueva lista\n")
    return lista #retornar lista con el diccionario ya eliminado

def actualizar():
    while True: # control de excepciones para el id
        id_actualizar = input("ingrese el id del estudiante que desea actualizar: ")
        if id_actualizar not in recopilador_id():
            print("ese estudiante no se encuentra registrado\n")
        else:
            break
    opcion = input("¿Desea actualizar el nombre o la edad del estudiante? (n/e): ")
    if opcion.lower() == "n": # si el usuario selecciona la opcion de actualizar el nombre
        nombre = input("ingrese el nuevo nombre del estudiante: ")
        for i in lista: # for que recorre la lista de diccionarios
            if i["id"] == id_actualizar: # si el id del estudiante coincide con el id ingresado
                i["nombre"] = nombre # se actualiza el nombre del estudiante
    elif opcion.lower() == "e": # si el usuario selecciona la opcion de actualizar la
        edad = input("ingrese la nueva edad del estudiante: ")
        for i in lista: # for que recorre la lista de diccionarios
            if i["id"] == id_actualizar: # si el id del estudiante coincide con
                i["edad"] = edad # se actualiza la edad del estudiante
    print("Nueva lista\n")
    return lista #retornar lista con el diccionario ya actualizado


def menu(): # funcion menu, que se encarga de llamar las respectivas funcionees
    while True:
        opcion=seleccion()
        if opcion == "1":
            solicitar_datos()
        elif opcion =="2":
            print(eliminar())
        elif opcion == "3":
            print(actualizar())
        else:
            print("Saliendo del programa...")
            time.sleep(2)
            break
menu()
print("--- FIN DEL PROGRAMA ---")
        
        
