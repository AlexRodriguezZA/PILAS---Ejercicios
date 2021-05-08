from pila import Pila
#Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire strikes back” y la otra los del episodio VII “The force awakens”.
#Desarrollar un algoritmo quepermita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos 
# episodios.

pilaV = Pila()
pilaVII = Pila()
pilaVIIAux = Pila()
vectorNameRepeat = []


for i in range(0,3):
    nombrev = str(input("Ingrese el nombre del personaje V: "))
    pilaV.apilar(nombrev)

for i in range(0,3):
    nombrevii = str(input("Ingrese el nombre del personaje VII: "))
    pilaVII.apilar(nombrevii)

while(not pilaV.pila_vacia()):
    nameV = pilaV.desapilar()
    while (not pilaVII.pila_vacia()):
        nameVII = pilaVII.desapilar()
        pilaVIIAux.apilar(nameVII)
        if nameV == nameVII:
            vectorNameRepeat.append(nameV)
    
    while (not pilaVIIAux.pila_vacia()):
        z = pilaVIIAux.desapilar()
        pilaVII.apilar(z)

print("Los nombres que se repiten son:")
for nombres in vectorNameRepeat:
    print(nombres)


