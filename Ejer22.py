from pila import Pila

#Se recuperaron las bitácoras de las naves del cazarrecompensas Boba Fett y Din Djarin (TheMandalorian), 

# las cuales se almacenaban en una pila (en su correspondiente nave) en cada

# misión de caza que emprendió, con la siguiente información: planeta visitado, a quien capturó,costo de la recompensa. 

# Resolver las siguientes actividades:

#a. mostrar los planetas visitados en el orden que hicieron las misiones cada uno de los cazzarrecompensas;

#b. determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos quien obtuvo mayor fortuna;

#c. determinar el número de la misión –es decir su posición desde el fondo de la pila en la que Boba Fett capturo a Han Solo, 

# suponga que dicha misión está cargada;

#d. indicar la cantidad de capturas realizadas por cada cazarrecompensas.


pilaBOBAFETT = Pila()

pilaDINDJARIN = Pila()


planetasVisitadosBobaFett = []
planetasVisitadoDinDjarin = []
CreditosGalacticosBobaFett = 0;
CreditosGalacticosDinDjarin = 0;


Informacion_bobafett = ["marte",400000,"baby yoda"]

pilaBOBAFETT.apilar(Informacion_bobafett)

Informacion_bobafett = ["venus",340000,"Han Solo"]

pilaBOBAFETT.apilar(Informacion_bobafett)

Informacion_bobafett = ["planeta tierra",4000000,"yoda"]

pilaBOBAFETT.apilar(Informacion_bobafett)


Informacion_dinDjarin = ["Arvala-7",50000,"Luke"]

pilaDINDJARIN.apilar(Informacion_dinDjarin)

Informacion_dinDjarin = ["mandalore",50000,"Grogu"]

pilaDINDJARIN.apilar(Informacion_dinDjarin)

Informacion_dinDjarin = ["Arvala-78",50000,"C3po"]

pilaDINDJARIN.apilar(Informacion_dinDjarin)


HanSolo = pilaBOBAFETT.tamanio()

contadorCapturasBobaFett = 0;

contadorCapturasDinDjarin = 0; 

while not pilaBOBAFETT.pila_vacia():

    x = pilaBOBAFETT.desapilar()

    contadorCapturasBobaFett += 1;

    HanSolo -= 1;

    if (x[2] == "Han Solo"):

        print(">> Han solo fue capturado en la misión N° ",HanSolo+1)

    planetasVisitadosBobaFett.append(x[0])

    CreditosGalacticosBobaFett += x[1];
        



while not pilaDINDJARIN.pila_vacia():

    z = pilaDINDJARIN.desapilar()

    contadorCapturasDinDjarin += 1
    planetasVisitadoDinDjarin.append(z[0])

    CreditosGalacticosDinDjarin += z[1]


print(">>Los planetas vistados por Boba Fett son:")

for planetasBobaFett in planetasVisitadosBobaFett:
    print("-",planetasBobaFett);



print(">>Los planetas vistados por Din Djarin son:")

for planetasDinDjarin in planetasVisitadoDinDjarin:
    print("-",planetasDinDjarin);

print()

print("Los recuadado por Boba fett es --> ", CreditosGalacticosBobaFett)

print("Los recuadado por Djin Djarin es --> ", CreditosGalacticosDinDjarin)


if CreditosGalacticosBobaFett>CreditosGalacticosDinDjarin:

    print("Boba Fett obtuvo mayor ganacias") 

elif CreditosGalacticosBobaFett<CreditosGalacticosDinDjarin:

    print("Din Djarin obtuvo mayor ganacias")

else:

    print("Obtuvieron las mismas ganancias") 


print("La cantidad de capturas realizadas por Boba Fett es de --> ",contadorCapturasBobaFett)

print("La cantidad de capturas realizadas por Din Djarin es de --> ",contadorCapturasDinDjarin )







