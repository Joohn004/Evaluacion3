import random

libro=[]
lista=[]

for lista in libro:
    for elemento in lista:
        print(elemento)
    print("******")

def menu():
    print("---Libro Mágico---")
    print("1.Agregar libro")
    print("2.Buscar libro")
    print("3.Imprimir etiquetas")
    print("4.Salir")
    op=int(input("Ingrese Opción:\n>"))
    return op

def registrar():

    while True:
     titulolibro=input("Ingrese título libro: ")
     if (len(titulolibro)>=10 and len(titulolibro)<=50) and titulolibro.isalnum():
        break
     else:
        print("Ingrese datos válidos. El título debe contener mínimo 10 caracteres y máximo 50.")

    while True:
        preciolibro = input("Ingrese precio del libro: ")
        if preciolibro.isdigit() and int(preciolibro) > 4500:
            break
        else:
            print("El precio del libro debe ser un número entero superior a $4500.")

    autorlibro=input("Ingrese autor libro: ")
    generolibro=input("Ingrese género libro: ")
    numeropaginas=input("Ingrese el número páginas libro: ")

    lista=[titulolibro,preciolibro,autorlibro,generolibro,numeropaginas]
    libro.append(lista)

def listar_libro():
    for lista in libro:
        for dato in lista:
            print(dato)

def buscar(titulo):
    i=1
    for lista in libro:
        if lista[0] == titulo:
            print(f"titulo libro: {lista[0]} ")
            print(f"precio libro: ${lista[1]} ")
            print(f"autor libro: {lista[2]} ")
            print(f"genero libro: {lista[3]} ")
            print(f"numero de paginas: {lista[4]}")
            print("----------------------")
            i = 0
    if i==1:
        print("No se encontro el libro")

def emitir_etiquetas():
    print("----Imprimiendo Etiquetas----")
    for lista in libro:
        print(f"titulo libro: {lista[0]} ")
        print(f"precio libro: ${lista[1]} ")
        print(f"autor libro: {lista[2]} ")
        print(f"genero libro: {lista[3]}")
        print(f"numero de paginas: {lista[4]}")
        print("----------------------")

while True:
    try:
        opcion=menu()

        if opcion==1:
            registrar()
        elif opcion==2:
            while True:
                titulo=input("Ingrese título a buscar:\n")
                if (len(titulo)>=10 and len(titulo)<=50):
                    buscar(titulo)
                    break
                else:
                    print("Ingrese datos validos el titulo debe contener minimo 10 caracteres maximo 50")
        elif opcion==3:
            emitir_etiquetas()
        elif opcion==4:
            break
        else:
            print("Opción Incorrecta")
    except :
            print("Error Inesperado")
