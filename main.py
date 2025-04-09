from persona import Cliente, Empleado
from cita import Cita
from agenda import Agenda

cliente1 = Cliente("Ana", "ana@email.com", "123456789")
empleado1 = Empleado("Luis", "luis@email.com", "Peluquero")

cita1 = Cita(cliente1, empleado1, "2025-04-10", "10:00")
agenda = Agenda()
agenda.agregar_cita(cita1)

agenda.mostrar_citas()
