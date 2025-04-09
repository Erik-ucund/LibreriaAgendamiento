class Agenda:
    def __init__(self):
        self.__citas = []

    def agregar_cita(self, cita):
        self.__citas.append(cita)

    def mostrar_citas(self):
        for cita in self.__citas:
            print(cita)
