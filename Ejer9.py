from pila import Pila;
#Resolve rel problemas del factorial de un numero utilizando una pila

pilaFactorial = Pila()

numfactorial = int(input(">> Ingrese un numero para calcular su factorial: "))

pilaFactorial.apilar(numfactorial)
for i in range(numfactorial-1):
    numfactorial -= 1;
    pilaFactorial.apilar(numfactorial)

factorial = 1;
while (not pilaFactorial.pila_vacia()):
    num = pilaFactorial.desapilar()
    factorial = num * factorial;

print(f"factorial --> {factorial}")

