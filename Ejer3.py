from pila import Pila
#Reemplazar todas las ocurrencias de un determinado elemento en una pila.

pila = Pila()
pilaAux = Pila()

for i in range(0,10):
    NumeroIngresado = int(input("Ingrese un numero: "))
    pila.apilar(NumeroIngresado)

NumeroRemplazado = int(input("INgrese el numero que desee reemplazar: "))

#Reemplazamos por cero

while(not pila.pila_vacia()):
    x = pila.desapilar()
    if (x == NumeroRemplazado):
        x = 0;
        pilaAux.apilar(x)
    else:
        pilaAux.apilar(x)
        
#Acomodamos los datos
while(not pilaAux.pila_vacia()):
    z = pilaAux.desapilar()
    pila.apilar(z)
    print(z)


