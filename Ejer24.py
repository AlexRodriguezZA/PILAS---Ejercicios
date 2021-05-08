from pila import Pila
#Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:
#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-ción uno la cima de la pila;
#b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar 
# la cantidad de películas en la que aparece;
#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

pila = Pila()
pilaAux = Pila()

avenger = ["thor",9]
pila.apilar(avenger)
avenger = ["Rocket Raccoon",4]
pila.apilar(avenger)
avenger = ["Groot",8]
pila.apilar(avenger)
avenger = ["Black widow",4]
pila.apilar(avenger)
avenger = ["Hulk",4]
pila.apilar(avenger)
avenger = ["Capitan america",5]
pila.apilar(avenger)

vectorPersonajesInicialies = []
indice = 0;
pelisBlackWidow = 0;
while not pila.pila_vacia():
    indice+=1
    x = pila.desapilar()
    #Punto C
    if x[0] == "Black widow":
        pelisBlackWidow = x[1]
    #Punto A
    if x[0] == "Rocket Raccoon":
        print("Rocket Raccoonestá en la posicion  N° ",indice)
    if x[0] == "Groot":
        print("Groot está en la posicion  N° ",indice)
    #Punto D
    if (x[0][0] == "C") or (x[0][0] == "D") or (x[0][0] == "G"):
        vectorPersonajesInicialies.append(x[0])
    #Punto B
    if (x[1] > 5):
        pilaAux.apilar(x)

print("Black widow participo en --> ",pelisBlackWidow, " películas" )
print(">>Los personajes que empiezan con las letras C, D o G son:") 
for elementos in vectorPersonajesInicialies:
    print(elementos)

print()

print(">>Los personajes que tiene mas de 5 peliculas son:")
while (not pilaAux.pila_vacia()):
    z = pilaAux.desapilar()
    print("-Personaje: ",z[0], "/ Peliculas: ",z[1])


 
        










