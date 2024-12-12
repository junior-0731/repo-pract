lista=[
    {
    "id":"131313",
    "nombre":"junior",
    "edad":"13"
        
    },
    {
    "id":"1212",
    "nombre":"pepe",
    "edad":"13"
        
    },
    {
    "id":"1313",
    "nombre":"lucas",
    "edad":"13"
        
    }
    
]

def eliminar(id_estudiante): # funcion eliminar que recibe como parametro el id del estudiante
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