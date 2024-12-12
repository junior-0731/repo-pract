
print("Calculadora")

#solicitar numeros
def solicitar_numeros():
    print("Ingresa los dos digitos \n")
    numeros=[]
    for i in range(2):
        numero = int(input(f"Ingresa el numero {i+1}: "))
        numeros.append(numero)
    return numeros


#funcion multiplicar
def multiplicar(n1,n2):
    print(n1 * n2) 
# funcion restar
def restar(n1,n2):
    print(n1 - n2) 
#funcion suma
def suma(n1,n2):
    print(n1 + n2) 
#funcion division
def division(n1,n2):
    print(n1 / n2) 
#menu
def menu():
    try:
        listaNumeros = solicitar_numeros()
        n1 = listaNumeros[0]
        n2 = listaNumeros[1]
        o= input("""Que deseas hacer
            1. sumar
            2. multiplicar
            3. Restar
            4. Dividir\n""")
        if o =="3":
            restar(n1,n2)
        elif o == "2":
            multiplicar(n1,n2)
        elif o == "1":
            suma(n1,n2)
        elif o == "4":
            division(n1,n2)
    except ValueError:
        print("Los datos deben ser numeros")
        menu()
    except Exception as e:
        print("Error inesperado: ", e)
        menu()
menu()

