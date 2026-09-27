import pytest
from datetime import date, timedelta
from mascota import Mascota
from perro import Perro
from gato import Gato
from dueno import Dueño
from turno import Turno


# CA-1: Al registrar una nueva mascota asociada a un cliente existente, 
# el sistema la almacena en la lista interna del objeto Dueño
def test_ca1_registrar_mascota_en_dueno():
    dueño = Dueño("Juan Pérez", "123456789")
    perro = Perro("Firulais", date(2020, 1, 1), "Labrador")
    
    dueño.registrar_mascota(perro)
    
    assert len(dueño.mascotas) == 1
    assert dueño.mascotas[0] == perro
    assert dueño.mascotas[0].nombre == "Firulais"


# CA-2: Al solicitar un turno para una fecha pasada, el sistema rechaza la operación lanzando una excepción
def test_ca2_rechazar_turno_fecha_pasada():
    fecha_pasada = date.today() - timedelta(days=10)
    
    with pytest.raises(ValueError, match="No se puede solicitar un turno para una fecha pasada"):
        Turno(fecha_pasada, "Vacunación", 50.0)


# CA-2: Se permite crear turno con fecha futura
def test_ca2_aceptar_turno_fecha_futura():
    fecha_futura = date.today() + timedelta(days=10)
    turno = Turno(fecha_futura, "Vacunación", 50.0)
    
    assert turno.fecha == fecha_futura
    assert turno.motivo == "Vacunación"
    assert turno.costo == 50.0


# CA-3: El método obtener_historial_turnos() de la clase Mascota devuelve únicamente los turnos cuya fecha sea anterior a la actual
def test_ca3_obtener_historial_turnos():
    mascota = Mascota("Pelusa", date(2020, 1, 1))
    
    # Crear turnos con fechas pasadas (usando validar_fecha=False para tests)
    fecha_pasada1 = date.today() - timedelta(days=20)
    fecha_pasada2 = date.today() - timedelta(days=10)
    fecha_futura = date.today() + timedelta(days=5)
    
    turno_pasado1 = Turno(fecha_pasada1, "Vacunación", 50.0, validar_fecha=False)
    turno_pasado2 = Turno(fecha_pasada2, "Control", 30.0, validar_fecha=False)
    turno_futuro = Turno(fecha_futura, "Peluquería", 40.0)
    
    mascota.agregar_turno(turno_pasado1)
    mascota.agregar_turno(turno_pasado2)
    mascota.agregar_turno(turno_futuro)
    
    historial = mascota.obtener_historial_turnos()
    
    assert len(historial) == 2
    assert turno_pasado1 in historial
    assert turno_pasado2 in historial
    assert turno_futuro not in historial


# CA-4: Al calcular el costo total de la atención, se aplica un descuento del 10% si la mascota está registrada en la categoría "VIP"
def test_ca4_descuento_vip():
    mascota_vip = Mascota("Rex", date(2020, 1, 1), "VIP")
    mascota_normal = Mascota("Luna", date(2020, 1, 1), "Normal")
    
    costo_base = 100.0
    
    assert mascota_vip.calcular_costo_total(costo_base) == 90.0  # 10% descuento
    assert mascota_normal.calcular_costo_total(costo_base) == 100.0  # Sin descuento


# CA-5: Todas las clases implementan el método especial __str__ para retornar una representación legible en texto de sus atributos
def test_ca5_metodo_str_mascota():
    mascota = Mascota("Firulais", date(2020, 1, 1), "VIP")
    str_repr = str(mascota)
    
    assert "Firulais" in str_repr
    assert "2020-01-01" in str_repr
    assert "VIP" in str_repr


def test_ca5_metodo_str_perro():
    perro = Perro("Firulais", date(2020, 1, 1), "Labrador")
    str_repr = str(perro)
    
    assert "Firulais" in str_repr
    assert "Labrador" in str_repr
    assert "Perro" in str_repr


def test_ca5_metodo_str_gato():
    gato = Gato("Michi", date(2020, 1, 1), "Negro")
    str_repr = str(gato)
    
    assert "Michi" in str_repr
    assert "Negro" in str_repr
    assert "Gato" in str_repr


def test_ca5_metodo_str_dueno():
    dueño = Dueño("Juan Pérez", "123456789")
    str_repr = str(dueño)
    
    assert "Juan Pérez" in str_repr
    assert "123456789" in str_repr
    assert "Dueño" in str_repr


def test_ca5_metodo_str_turno():
    fecha = date.today() + timedelta(days=1)
    turno = Turno(fecha, "Vacunación", 50.0)
    str_repr = str(turno)
    
    assert "Vacunación" in str_repr
    assert "50.0" in str_repr
    assert "Turno" in str_repr


# CA-6: El código implementa obligatoriamente una clase base 'Mascota' de la cual heredan las clases derivadas 'Perro' y 'Gato', 
# utilizando polimorfismo para el comportamiento específico
def test_ca6_herencia_perro():
    perro = Perro("Firulais", date(2020, 1, 1), "Labrador")
    
    assert isinstance(perro, Mascota)
    assert isinstance(perro, Perro)
    assert hasattr(perro, 'nombre')
    assert hasattr(perro, 'fecha_nacimiento')
    assert hasattr(perro, 'categoria')
    assert hasattr(perro, 'raza')  # Atributo específico de Perro


def test_ca6_herencia_gato():
    gato = Gato("Michi", date(2020, 1, 1), "Negro")
    
    assert isinstance(gato, Mascota)
    assert isinstance(gato, Gato)
    assert hasattr(gato, 'nombre')
    assert hasattr(gato, 'fecha_nacimiento')
    assert hasattr(gato, 'categoria')
    assert hasattr(gato, 'color')  # Atributo específico de Gato


def test_ca6_polimorfismo():
    perro = Perro("Firulais", date(2020, 1, 1), "Labrador")
    gato = Gato("Michi", date(2020, 1, 1), "Negro")
    
    # Comportamiento específico de cada clase
    assert perro.ladrar() == "¡Guau!"
    assert gato.maullar() == "¡Miau!"
    
    # Ambos heredan métodos de Mascota
    assert isinstance(perro, Mascota)
    assert isinstance(gato, Mascota)
