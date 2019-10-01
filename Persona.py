#!/usr/bin/python3

# guardar en la carpeta del proyecto como:
#'Persona.py'

class Persona:
    """ clase que representa a una Persona
        En chile
        self -> rol similar al this de Java
        El constructor se llama siempre
        (doble underscore)init(doble underscore)
        Todas las operaciones de la clase reciben
        al self como primer parametro!!!
    """ 
    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut

    # OJO todos los metodos reciben el self como parametro
    def imprimir(self):
        texto = " ".join(["soy", self.nombre, ", mi rut es",self.rut])
        print(texto)


