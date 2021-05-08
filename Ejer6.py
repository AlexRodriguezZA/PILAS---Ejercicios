from pila import Pila
#Leer una palabra y visualizarla en forma inversa.

pilaLetras = Pila()

palabra = str(input("INgrese la palabra: "))

print(palabra)

for letra in palabra:
    pilaLetras.apilar(letra)
    print(letra)

print("Inversa")

while(not pilaLetras.pila_vacia()):
    x = pilaLetras.desapilar()
    print(x)
    