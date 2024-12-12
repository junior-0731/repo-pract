
def exeption_operation(funct):
    def wraper_operation(*args,**kwargs):
        try:
            funct(*args,**kwargs)
        except ValueError: 
            return "Error los datos deben ser numeros"
        except Exception as e:
            return "Error inesperado: ",e
    return wraper_operation

print("Calculadora")

#solicitar numeros
def solicitar_numeros():
    print("Ingresa los dos digitos \n")
    numeros=[]
    for i in range(2):
        numero = int(input(f"Ingresa el numero {i+1}: "))
        numeros.append(numero)
    return numeros
#menu
def menu():
    listaNumeros = solicitar_numeros()
    n1 = listaNumeros[0]
    n2 = listaNumeros[1]
    o= input("""Que deseas hacer
        1. sumar
        2. multiplicar
        3. Restar
        4. Dividir\n""")
    if o =="1":
        print(suma(n1,n2))
    elif o == "2":
        print(multiplicar(n1,n2))
    elif o == "3":
        print(restar(n1,n2))
    elif o == "4":
        print(division(n1,n2))
    
#funcion multiplicar
def multiplicar(n1,n2):
    return n1 * n2
# funcion restar
def restar(n1,n2):
    return n1-n2
#funcion suma
def suma(n1,n2):
    return  n1+ n2

#funcion division
def division(n1,n2):
    return n1 / n2

menu()


