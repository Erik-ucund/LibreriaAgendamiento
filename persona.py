class Persona:
    def __init__(self, nombre, correo):
        self.__nombre = nombre
        self.__correo = correo

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def __str__(self):
        return f"{self.__nombre} ({self.__correo})"

class Cliente(Persona):
    def __init__(self, nombre, correo, telefono):
        super().__init__(nombre, correo)
        self.__telefono = telefono

    def get_telefono(self):
        return self.__telefono

class Empleado(Persona):
    def __init__(self, nombre, correo, area):
        super().__init__(nombre, correo)
        self.__area = area

    def get_area(self):
        return self.__area
