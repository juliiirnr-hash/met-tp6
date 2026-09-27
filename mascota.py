from datetime import date
from typing import List


class Mascota:
    # Clase base para representar una mascota
    def __init__(self, nombre: str, fecha_nacimiento: date, categoria: str = "Normal"):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.categoria = categoria
        self.turnos: List['Turno'] = []

    # Método especial para representación legible en texto (CA-5)
    def __str__(self):
        return f"Mascota(nombre={self.nombre}, fecha_nacimiento={self.fecha_nacimiento}, categoria={self.categoria})"

    # Método para agregar un turno a la mascota
    def agregar_turno(self, turno: 'Turno') -> None:
        self.turnos.append(turno)

    # CA-3: Devuelve únicamente los turnos cuya fecha sea anterior a la actual
    def obtener_historial_turnos(self) -> List['Turno']:
        fecha_actual = date.today()
        return [turno for turno in self.turnos if turno.fecha < fecha_actual]

    # CA-4: Calcula el costo total con descuento del 10% si es VIP
    def calcular_costo_total(self, costo_base: float) -> float:
        if self.categoria == "VIP":
            return costo_base * 0.9  # Descuento del 10%
        return costo_base
