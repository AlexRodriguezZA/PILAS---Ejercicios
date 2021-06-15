from pila import Pila;
#Dada una pila con los valores promedio de temperatura ambiente de cada día del mes de abril,
#obtener la siguiente información sin perder los datos:
#a. determinar el rango de temperatura del mes, temperatura mínima y máxima;
#b. calcular el promedio de temperatura (o media) del total de valores;
#c. determinar la cantidad de valores por encima y por debajo de la media.

pilaTemperaturas = Pila();
pilaAux = Pila();
temperaturas = [28,36,12,37,40,5,14,11]
valorMasMedia = [];
valorMenosMedia = [];

for t in temperaturas:
    pilaTemperaturas.apilar(t)
print(temperaturas)
temperaturaMaxima = 0;
temperaturaMinima = pilaTemperaturas.elemento_cima() 
acumulador = 0;
while (not pilaTemperaturas.pila_vacia()):
    dato = pilaTemperaturas.desapilar();
    acumulador = acumulador + dato;
    if (dato>=temperaturaMaxima):
        temperaturaMaxima = dato;
    if (dato<temperaturaMinima):
        temperaturaMinima = dato;
    
    pilaAux.apilar(dato)
promedio = acumulador / (pilaAux.tamanio())
rango = (temperaturaMaxima - temperaturaMinima)
while (not pilaAux.pila_vacia()):
    dato = pilaAux.desapilar()
    if (dato > promedio):
        valorMasMedia.append(dato)
    else:
        valorMenosMedia.append(dato) 
print(f"La temperatura maxima fue {temperaturaMaxima}")
print(f"La temperatura minima fue {temperaturaMinima}")
print(f"El rango de temperaturas es {rango}")
print(f"El promedio de temperaturas es {promedio}")
print(f"Las temperaturas mayores a la media son -> {valorMasMedia}")
print(f"Las temperaturas menores a la media son -> {valorMenosMedia}")

