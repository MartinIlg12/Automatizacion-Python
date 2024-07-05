import cv2
class Humano:
    def imprimirTresCaracteristicas(self):
        nombre = input("Ingrese su nombre: ")
        print(f"Características de {nombre}:")
        print("* Sentimientos")
        print("* Lenguaje")
        print("* Socializacion")
    def obtenerPoblacion(self, edad):
        if edad <= 25:
            poblacion1995 = 5760000000  
            print(f"Población mundial en 1995: {poblacion1995} personas")
        else:
            poblacion2024 = 7800000000  
            print(f"Población mundial en 2024: {poblacion2024} personas")
    def abrirCamara(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('Camara', frame)
            if cv2.waitKey(1) & 0xFF == ord('h'):  
                break
        cap.release()
        cv2.destroyAllWindows()
if __name__ == "__main__":
    humano = Humano()
    humano.imprimirTresCaracteristicas()
    edad = int(input("Ingrese su edad: "))
    humano.obtenerPoblacion(edad)
    print("Abriendo la cámara📸")
    humano.abrirCamara()
