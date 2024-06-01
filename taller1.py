#Taller1
#Franklin Martin Ilguan Guerrero
# Diccionario de personas que quieren viajar
viajeros = {
    "Martin": {},
    "Franklin": {},
    "Paula": {},
    "Arturo": {},
    "Stefany": {},
    "William": {},
    "Sebas": {},
    "Maty": {},
    "Julia": {},
    "Joe": {}
}
# Diccionario de lugares y sus caracteristicas
destinos = {
    "Guayaquil": {"Población": "2.698 millones", "Clima": "Cálido", "Lugar Turistico": "Cerro Santa Ana", "Comida Típica": "Bolon"},
    "Manta": {"Población": "271.145 mil", "Clima": "Cálido", "Lugar Turistico": "Playa el Murcielago", "Comida Típica": "Ceviche"},
    "Canoa": {"Población": "22.025 mil", "Clima": "Cálido", "Lugar Turistico": "Canoa Beach", "Comida Típica": "Encebollado"},
    "Republica Dominicana": {"Población": "11.23 millones", "Clima": "Cálido", "Lugar Turistico": "Punta Cana", "Comida Típica": "Mangú"},
    "Panamá": {"Población": "4.409 millones", "Clima": "Cálido", "Lugar Turistico": "Casco Antiguio", "Comida Típica": "Rondón"},
    "Colombia": {"Población": "51.87 millones", "Clima": "Cálido", "Lugar Turistico": "Valle de Cocora", "Comida Típica": "Bandeja Paisa"},
    "Centro histórico de Quito": {"Lugares a visitar":"La ronda", "Comidas Tipicas":"Espumillas", "Transporte:":"Bus, Metro", "Horarios:":"Todo el dia"},
    "Iglesia de la Basílica": {"Lugares a visitar":"Cupula de la iglesia", "Comidas Tipicas":"Espumillas", "Transporte:":"Bus, Taxi", "Horarios:":"10am - 8pm"},
    "Museo del agua": {"Estante a visitar:":"Burbujas Gigantes", "Comidas Tipicas":"Espumillas", "Transporte:":"Bus, Taxi", "Horarios:":"8am - 4pm"}
}
def lugaresQuePuedoVisitar(dinero):
    if dinero > 1000:
        return ["Republica Dominicana", "Panamá", "Colombia"]
    elif dinero > 500:
        return ["Guayaquil", "Manta", "Canoa"]
    else:
        return ["Centro histórico de Quito", "Iglesia de la Basílica", "Museo del agua"]
# Creacion del programa
def progrma ():
    while True:
        nombre = input("Ingrese su nombre: ")
        if nombre in viajeros:
            break
        else:
            print("Nombre no encontrado. Inténtelo de nuevo.")
    dinero = float(input("Ingrese la cantidad de dinero que tiene: "))
    destinosPosibles = lugaresQuePuedoVisitar(dinero)
    print(f"Con ${dinero}, puede viajar a los siguientes destinos: {', '.join(destinosPosibles)}")
    while True:
        lugarElegido = input("Ingrese el nombre del lugar al que desea ir: ")
        if lugarElegido in destinosPosibles:
            break
        else:
            print("Destino no válido. Inténtelo de nuevo.")
    detalles = destinos[lugarElegido]
    print(f"Detalles del lugar {lugarElegido}:")
    for key, value in detalles.items():
        print(f"{key}: {value}")
# Correr el programa
progrma()
