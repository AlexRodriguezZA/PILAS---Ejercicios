from pila import Pila
#Eliminar el i-ésimo elemento debajo de la cima de una pila de palabras.

pila = Pila()
pilaAux = Pila()

for i in range(0,5):
    numero = int(input("Ingrese un numero: "))
    pila.apilar(numero)
#5
#4 --> eliminar
#3
#2
#1
cont=0
while (not pila.pila_vacia()):
    x = pila.desapilar()
    cont +=1
    if (cont != 2):
        pilaAux.apilar(x)
        print(x)





