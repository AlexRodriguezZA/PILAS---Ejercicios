from pila import Pila;
#Dada una pila con nombres de los personajes de la saga de Star Wars, implemente una función
#que permita determinar si Leia Organa o Boba Fett están en dicha pila sin perder los datos.

pilaStarWars = Pila()
pilaAux = Pila()

pilaStarWars.apilar("Mace Windu")
pilaStarWars.apilar("Anakin Skywalker")
pilaStarWars.apilar("Jar Jar Binks")
pilaStarWars.apilar("Boba Fett")
pilaStarWars.apilar("Leia Organa")
pilaStarWars.apilar("Darth Maul")

validarPersonajes = False;
while not pilaStarWars.pila_vacia():
    x = pilaStarWars.desapilar();
    if (x == "Leia Organa" or x=="Boba Fett"):
        validarPersonajes = True;
    pilaAux.apilar(x)

if (validarPersonajes==True):
    print("Los personajes de Leia Organa o Boba Fett estan en la pila")
else:
    print("Los personajes de Leia Organa o Boba Fett NO estan en la pila")
    
