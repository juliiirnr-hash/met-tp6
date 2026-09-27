from typing import List
from mascota import Mascota


class Dueño:
    # Clase para representar un dueño de mascotas
    def __init__(self, nombre: str, telefono: str):
        self.nombre = nombre
        self.telefono = telefono
        self.mascotas: List[Mascota] = []

    # CA-1: Al registrar una nueva mascota asociada a un cliente existente, 
    # el sistema la almacena en la lista interna del objeto Dueño
    def registrar_mascota(self, mascota: Mascota) -> None:
        self.mascotas.append(mascota)

    # Método especial para representación legible en texto (CA-5)
    def __str__(self):
        return f"Dueño(nombre={self.nombre}, telefono={self.telefono}, mascotas={len(self.mascotas)})"
