from datetime import date
from mascota import Mascota


class Perro(Mascota):
    # Clase derivada para representar un perro (CA-6: polimorfismo)
    def __init__(self, nombre: str, fecha_nacimiento: date, raza: str, categoria: str = "Normal"):
        super().__init__(nombre, fecha_nacimiento, categoria)
        self.raza = raza

    # Comportamiento específico para perros (polimorfismo)
    def ladrar(self) -> str:
        return "¡Guau!"

    # Método especial para representación legible en texto (CA-5)
    def __str__(self):
        return f"Perro(nombre={self.nombre}, fecha_nacimiento={self.fecha_nacimiento}, raza={self.raza}, categoria={self.categoria})"
