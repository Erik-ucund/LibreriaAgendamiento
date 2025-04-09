class Cita:
    def __init__(self, cliente, empleado, fecha, hora):
        self.__cliente = cliente
        self.__empleado = empleado
        self.__fecha = fecha
        self.__hora = hora

    def __str__(self):
        return f"Cita para {self.__cliente.get_nombre()} con {self.__empleado.get_nombre()} el {self.__fecha} a las {self.__hora}"
