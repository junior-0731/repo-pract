def exeption_operation(funct):
    def wraper_operation(*args,**kwargs):
        try:
            funct(*args,**kwargs)
        except ValueError: 
            return "Error los datos deben ser numeros"
        except Exception as e:
            return "Error inesperado: ",e
    return wraper_operation
@exeption_operation
def suma(a:int,b:int):
    return a + b
def multiplicacion(a:int,b:int):
    return a * b

print(suma("5",20))
print(multiplicacion(5,20))