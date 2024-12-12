# id,nombre, edad
# lista, diccionario, id

lista = [{"id":123},{"id":435},{"id":864}] #demo
lista = [
    {"id": 1, "nombre": "Juan", "edad": 20},
    {"id": 2, "nombre": "Ana", "edad": 22},
    # Agrega más estudiantes según sea necesario
]

def listar():
    for e,i in enumerate(lista):
        print(f"Student {e+1}")
        print(i)

listar()

def consultar():
    prueba = False
    try:
        id = int(input("Ingresa el id que deseas consultar: "))
    except ValueError:
        print("Error, el id debe ser un número")
    for t,u in enumerate(lista):
        if u["id"] == id:
            print(f"Student N.{t} encontrado...")
            print(u)
            print("-----------------")
            prueba = True
    if not prueba:
        print("No se encontro nada")
        
consultar()
