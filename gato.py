from datetime import date
from mascota import Mascota


class Gato(Mascota):
    # Clase derivada para representar un gato (CA-6: polimorfismo)
    def __init__(self, nombre: str, fecha_nacimiento: date, color: str, categoria: str = "Normal"):
        super().__init__(nombre, fecha_nacimiento, categoria)
        self.color = color

    # Comportamiento específico para gatos (polimorfismo)
    def maullar(self) -> str:
        return "¡Miau!"

    # Método especial para representación legible en texto (CA-5)
    def __str__(self):
        return f"Gato(nombre={self.nombre}, fecha_nacimiento={self.fecha_nacimiento}, color={self.color}, categoria={self.categoria})"
