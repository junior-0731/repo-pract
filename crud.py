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
        
    
    
        
        

print(eliminar("1"))