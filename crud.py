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
    return lista


def eliminar(id_estudiante): # funcion eliminar que recibe como parametro el id del estudiante
    lista= create_students
    ides=[] # lista donde se almacenaran todos los ides
    for i in lista: # for que recorre la lista de diccionarios
        ides.append(i["id"])  # agregar el id a la lista ides
    
    
    if id_estudiante not in ides: # verificar si el id se encuentre
        return ("ese estudiante no se encuentra registrado")
    else: # en caso de que se encuentre
        posicion= ides.index(id_estudiante) # se determina la posicion del id del estudiante
        lista.pop(posicion) # y se elimina esa posicion de la lista de diccionarios
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
    
