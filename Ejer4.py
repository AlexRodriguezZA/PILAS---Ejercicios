from pila import Pila
#Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra.

pila = Pila()
pilaAux = Pila()

for i in range(0,5):
    numero = int(input("Ingrese un numero: "))
    pila.apilar(numero)

while(not pila.pila_vacia()):
    x = pila.desapilar()
    pilaAux.apilar(x)
    print(x)
