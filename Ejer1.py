from pila import Pila

#Determinar el número de ocurrencias de un determinado elemento en una pila.

pila = Pila()

for i in range(0,5):
    NumeroIngresado = int(input("Ingrese un numero: "))
    pila.apilar(NumeroIngresado)

NumeroBuscado = int(input("Ingrese el número que desee buscar: "))
CantidaRep = 0
while (not pila.pila_vacia()):
    x = pila.desapilar()
    if (x == NumeroBuscado):
        CantidaRep +=1

print("-La cantidad de veces que se repite el numero es de --> ", CantidaRep)






