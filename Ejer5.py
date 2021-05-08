from pila import Pila
#Determinar si una cadena de caracteres es un palíndromo.

pilaLetras = Pila()
pilaReversa = Pila()
pilaAux = Pila()

palabra = str(input("Ingrese una palabra: "))
cont = 0
for letra in palabra:
    print(letra)
    pilaLetras.apilar(letra)
    pilaAux.apilar(letra)

print()

while (not pilaAux.pila_vacia()):
    x = pilaAux.desapilar()
    print(x)
    pilaReversa.apilar(x)

print()

while(not pilaLetras.pila_vacia() and not pilaReversa.pila_vacia()):
    x = pilaLetras.desapilar()
    z = pilaReversa.desapilar()
    if (x == z):
        cont += 1
print(cont)
if (cont == len(palabra)):
    print("La palabra es paliendromo")
else:
    print("La palabra no es paliendromo")





