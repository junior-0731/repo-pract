
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
        print("Lo sentimos, pero esa opcion no existe")
        seleccion()
    else: 
        return opcion # retornar la opcion seleccionada
    
    
def solicitar_datos():
    while True: # control de excepciones para el id
            id=input("Ingresa el id: ")
            if id in recopilador_id():
                print("ese id ya fue ingresado")
            else:
                break
    nombre=input("ingresa el nombre: ")
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


def recopilador_id():
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

def menu(): # funcion menu, que se encarga de llamar las respectivas funcionees
    opcion=seleccion()
    if opcion == "1":
        solicitar_datos()
        menu()
    elif opcion =="2":
        print(eliminar())
        menu()
menu()
        
        
