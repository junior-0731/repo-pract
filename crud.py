
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
    
def opciones_buscar():
    opc_buscar=input("""Desea buscar Por
                    1. id 
                    2. Nombre
                    3 Edad""")
    while True:
        if opc_buscar not in ["1","2", "3"]:
            print("Error, digita una opcion de buscar correcta")
        else:
            break
    if opc_buscar == "1":
        while True: # control de excepciones para el id
            id=input("Ingresa el id: ")
            if id not in recopilador_id():
                print("ese id no ha sido ingresado")
            else:
                break
        print(buscar_estudiante(lista,id))
    elif opc_buscar =="2":
        nombre=input("Ingresa el nombre: ")
        print(buscar_estudiante(lista,nombre,dato="nombre"))
    elif opc_buscar =="3":
        edad=input("Ingresa la edad: ")
        print(buscar_estudiante(lista,edad,dato="edad"))
        
        
            

    
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
        List: Esta funcion retorna la lista que modifico
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
#Buscar estudiantes
def buscar_estudiante(estudiantes:list,id:str = None,nombre:str = None,edad:str = None,dato:str = "id"):
    """
    Permite buscar un estudiante en especifico o varios estudiantes que tengan datos similares.

    Args:
        estudiante (list): La lista donde se quiere buscar a el estudiante. 
        id (str): Identificador único del estudiante.
        nombre (str): Nombre del estudiante.
        edad (str): Edad del estudiante.
        dato (str): El dato del estudiante o estudiantes que se quiere buscar, por defecto es el id.

    Returns:
        dic: En caso de que encuetre una unica coincidencia debuelve un diccionario que representa los datos del estudiante.
        list: En caso de que encuentre multiples coincidencisa debuelve una lista que diccionarios que representan los datos de los estudiantes.
        str: En caso de que no encuetre ninguna coincidencia debuelve un mensaje.

    """
    lista_estudiantes = [] # Aqui se guardaran todos los estudiantes que coincidan
    contador_estudiantes = 0 # Cuenta el numero de estudiantes que coinciden
    for estudiante in estudiantes: # Itera la lista de estudiantes 
        if estudiante[dato] == id or estudiante[dato] == nombre or estudiante[dato] == edad: 
            """ 
            Si encuentra un estudiante que coincida le suma 1 al contador y lo agrega a la lista de estudianes que coinciden
            """
            contador_estudiantes += 1
            if contador_estudiantes >= 1:
                lista_estudiantes.append(estudiante)
    
    if contador_estudiantes == 0: #Si no hay estudiantes que conincidan retorna un error
            return "Error: no hay estudiantes que coincidan"
    elif contador_estudiantes > 1: #Si hay mas de un estudiante que coincida 
        return lista_estudiantes
    
    return lista_estudiantes[0]
 
def menu(): # funcion menu, que se encarga de llamar las respectivas funcionees
    opcion=seleccion()
    if opcion == "1":
        solicitar_datos()
        menu()
    elif opcion =="2":
        print(eliminar())
        menu()
    elif opcion =="4":
        opciones_buscar()
        menu()
        
menu()
        

