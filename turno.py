from datetime import date


class Turno:
    # Clase para representar un turno de atención
    def __init__(self, fecha: date, motivo: str, costo: float, validar_fecha: bool = True):
        # CA-2: Validar que la fecha no sea pasada
        if validar_fecha and fecha < date.today():
            raise ValueError("No se puede solicitar un turno para una fecha pasada")
        self.fecha = fecha
        self.motivo = motivo
        self.costo = costo

    # Método especial para representación legible en texto (CA-5)
    def __str__(self):
        return f"Turno(fecha={self.fecha}, motivo={self.motivo}, costo={self.costo})"
