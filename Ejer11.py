from pila import Pila
#Dada una pila de letras determinar cuántas vocales contiene.

pilaLetras = Pila()

vocales = ["a","e","i","o","u"]
cont=0

palabra = str(input("Ingrese la palabra: "))

for letra in palabra:
    pilaLetras.apilar(letra)

while(not pilaLetras.pila_vacia()):
    x = pilaLetras.desapilar()
    if (x in vocales):
        cont +=1

print("La cantidad de vocales que tiene es de --> ", cont)


