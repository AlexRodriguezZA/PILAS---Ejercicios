from pila import Pila;
#Dada una pila de objetos de una oficina de los que se dispone de su nombre y peso (por ejemplo
#monitor 1 kg, teclado 0.25 kg, silla 7 kg, etc.), ordenar dicha pila de acuerdo a su peso del 
#objeto más liviano al más pesado–. Solo pueden utilizar pilas auxiliares como estructuras extras, 
# no se pueden utilizar métodos de ordenamiento.

pilaObjetos = Pila();
pilaAux = Pila()

objetosOficina = [
    {"objeto":"Teclado","peso":2.5},
    {"objeto":"mouse","peso":0.5},
    {"objeto":"silla","peso":5},
    {"objeto":"mesa","peso":13},
]
for objeto in objetosOficina:
    if (pilaObjetos.pila_vacia() == True):
        pilaObjetos.apilar(objeto)
    else:
        if objeto["peso"] <= pilaObjetos.elemento_cima()["peso"]:
            pilaObjetos.apilar(objeto)
        else:
            while((not pilaObjetos.pila_vacia()) and (objeto["peso"] > pilaObjetos.elemento_cima()["peso"])): 
                dato = pilaObjetos.desapilar()
                pilaAux.apilar(dato)
            pilaObjetos.apilar(objeto)
            while(not pilaAux.pila_vacia()):
                dato = pilaAux.desapilar()
                pilaObjetos.apilar(dato)

while not pilaObjetos.pila_vacia():
    ob = pilaObjetos.desapilar()
    print(ob)

        

