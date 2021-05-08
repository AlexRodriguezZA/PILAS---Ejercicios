from pila import Pila

#Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden ordenados de forma creciente.
#Solo puede utilizar una pila auxiliar como estructura extra, no se pueden utilizar métodos de ordenamiento.

pila = Pila()
pilaAux = Pila()

for i in range(0,6):
    numero = int(input("Ingrese un numero: "))
    if pila.pila_vacia():
        pila.apilar(numero)
    else:
        if numero>=pila.elemento_cima():
            pila.apilar(numero)
        else:
            while (not pila.pila_vacia()) and (pila.elemento_cima() > numero):
                x = pila.desapilar()
                pilaAux.apilar(x)
            pila.apilar(numero)
            while not pilaAux.pila_vacia():
                z = pilaAux.desapilar()
                pila.apilar(z)

while not pila.pila_vacia():
    y = pila.desapilar()
    print(y)










    





