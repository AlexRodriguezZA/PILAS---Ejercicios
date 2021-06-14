from pila import Pila;
#Insertar el nombre de la diosa griega Atenea en I-nésima posición debajo de la cima de una 
#pila de nombre de dioses griegos

pilaDioses = Pila();
pilaAux = Pila()
pilaDioses.apilar("Kratos")
pilaDioses.apilar("Zeus")
pilaDioses.apilar("Hades")
pilaDioses.apilar("Poseidón")
pilaDioses.apilar("Hefesto")

contadorSegundaPos = 0; #Para contar la i-nésima pos
while (not pilaDioses.pila_vacia()):
    x = pilaDioses.desapilar()
    contadorSegundaPos +=1
    if (contadorSegundaPos!=2):
        pilaAux.apilar(x)
    else:
        pilaAux.apilar("Atenea")

#REACOMODAMOS LA PILA ORIGINAL
while (not pilaAux.pila_vacia()):
    z = pilaAux.desapilar();
    pilaDioses.apilar(z)

#BARRIDO
while (not pilaDioses.pila_vacia()):
    x = pilaDioses.desapilar();
    print(x)

