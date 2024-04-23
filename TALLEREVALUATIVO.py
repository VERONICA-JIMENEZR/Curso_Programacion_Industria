#PUNTO 1 PROGRAMACIÓN ORIENTADA A OBJETOS
#Año es lo mismo que ano , problema con la ñ
# Definición de la clase Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
    def obtener_marca(self):
        return self.__marca

    def obtener_modelo(self):
        return self.__modelo

    def obtener_ano(self):
        return self.__ano
    def establecer_marca(self, marca):
        self.__marca = marca

    def establecer_modelo(self, modelo):
        self.__modelo = modelo

    def establecer_ano(self, ano):
        self.__ano = ano

    def detalles(self):
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}, Año: {self.__ano}"

# Creación de un objeto de la clase Vehiculo
mi_vehiculo = Vehiculo("Ford", "Mustang", 2018)
mi_vehiculo.establecer_marca("Honda")
mi_vehiculo.establecer_modelo("Civic")
mi_vehiculo.establecer_ano(2022)

# Información del vehículo
print(mi_vehiculo.detalles())


#PUNTO 2 
#Resolución de Problemas Matemáticos

def es_primo(num):
    "Funcion es primo"
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def suma_primos(n):
    "Funcion que suma primos"
    suma = 0
    for i in range(2, n+1):
        if es_primo(i):
            suma += i
    return suma

# Prueba de la función con el valor n=30
print("La suma de todos los números primos menores o iguales a 30 es:", suma_primos(30))

#PUNTO 3 
#Trabajar con un API
import requests

# URL base de la API
url = "https://jsonplaceholder.typicode.com"

# Obtener usuarios (GET)
respuesta = requests.get(f"{url}/users")
usuarios = respuesta.json()
print("Usuarios obtenidos.")

# Elegir un usuario y actualizar su nombre (PATCH)
id_usuario = usuarios[0]['id']  # Elegir el primer usuario
respuesta = requests.patch(f"{url}/users/{id_usuario}", data={"name": "Nuevo nombre"})
print("Nombre de usuario actualizado.")

# Crear un nuevo post 
respuesta = requests.post(f"{url}/posts", data={"userId": id_usuario, "title": "Nuevo post", "body": "Contenido del nuevo post"})
nuevo_post = respuesta.json()
print("Nuevo post creado.")

# Eliminar el post creado 
respuesta = requests.delete(f"{url}/posts/{nuevo_post['id']}")
if respuesta.status_code == 200:
    print("Post eliminado correctamente.")
else:
    print("Error al eliminar el post.")
