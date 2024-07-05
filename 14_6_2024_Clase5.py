nombres = ["martin", "paula", "franlin", "Arturo", "Julia", "Stefany"]
mamiferos = ["vaca", "cerdo", "perro", "gato", "murcielago", "mono"]
diccionario = {}

for i in range(6):
    diccionario[nombres[i]] = mamiferos[i]
    print(diccionario)

def imprimir(diccionario, primerNombre='Antonia', segundoNombre='Maty'):
    print(primerNombre)
    for clave in diccionario:
        print(clave)
    print(segundoNombre)
    for value in diccionario.values():
        print(value)

imprimir(diccionario)
