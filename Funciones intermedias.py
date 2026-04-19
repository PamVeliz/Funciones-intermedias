#1. Actualizar valores en diccionarios y listas
print("Ejercicio 1: Actualizar valores en diccionarios y listas")
matriz = [ [10, 15, 20], [3, 7, 14] ]
print(matriz)

matriz[1][0] = 6
print(matriz, "\n")

cantantes = [
	{"nombre": "Ricky Martin", "pais": "Puerto Rico"},
	{"nombre": "Chayanne", "pais": "Puerto Rico"}
	]
print(cantantes)

cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes, "\n")


ciudades = {
	"México": ["Ciudad de México", "Guadalajara", "Cancún"],
	"Chile": ["Santiago", "Concepción", "Viña del Mar"]
	}
print(ciudades)

ciudades["México"][2] = "Monterrey"
print(ciudades, "\n")

coordenadas = [
	{"latitud": 8.2588997, "longitud": -84.9399704}
	]
print(coordenadas)

latitud = coordenadas[0]["latitud"]
coordenadas[0]["latitud"] = 9.9355431
print(coordenadas, "\n")

#*Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
#*Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
#*En ciudades, cambia “Cancún” por “Monterrey”
#*En las coordenadas, cambia el valor de “latitud” por 9.9355431

#2. Iterar a través de una lista de diccionarios: Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios y 
# recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente.

print("\nEjercicio 2: Iterar a través de una lista de diccionarios")
cantantes = [
	{"nombre": "Ricky Martin", "pais": "Puerto Rico"},
	{"nombre": "Chayanne", "pais": "Puerto Rico"},
	{"nombre": "José José", "pais": "México"},
	{"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
	]

def iterarDiccionario(lista):
    for diccionario in lista:
        for llave, valor in diccionario.items():
            print(f"{llave}: {valor}")
iterarDiccionario(cantantes)

#3. Obtener valores de una lista de diccionarios
print("\nEjercicio 3: Obtener valores de una lista de diccionarios")
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        print(diccionario.get(llave))
iterarDiccionario2("nombre", cantantes)

#4. Iterar a través de un diccionario con valores de lista
print("\nEjercicio 4: Iterar a través de un diccionario con valores de lista")
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}
print(costa_rica)
def imprimirInformacion(diccionario):
    for llave, valor in diccionario.items():
        print(f"{len(valor)} {llave.upper()}")
        for item in valor:
            print(f"- {item}")
imprimirInformacion(costa_rica)