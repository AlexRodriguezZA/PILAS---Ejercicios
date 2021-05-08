from pila import Pila
#Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden números pares.

pila = Pila()
pilaAux = Pila()

for i in range(0, 5):
    numero = int((input("Ingrese los números: ")))
    pila.apilar(numero)


while(not pila.pila_vacia()):
    x = pila.desapilar()
    if (x % 2 == 0):
        pilaAux.apilar(x)

while (not pilaAux.pila_vacia()): #Volvemos a acomodar la pila original
    z = pilaAux.desapilar()
    pila.apilar(z)
    print(z)
    







        








    





