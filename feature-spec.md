\# feature-spec.md – Gestión de Mascotas y Turnos

CA-1 (funcional): Al registrar una nueva mascota asociada a un cliente existente, el sistema la almacena en la lista interna del objeto Dueño.

CA-2 (funcional): Al solicitar un turno para una fecha pasada, el sistema rechaza la operación lanzando una excepción.

CA-3 (funcional): El método obtener\_historial\_turnos() de la clase Mascota devuelve únicamente los turnos cuya fecha sea anterior a la actual.

CA-4 (funcional): Al calcular el costo total de la atención, se aplica un descuento del 10% si la mascota está registrada en la categoría "VIP".

CA-5 (no funcional): Todas las clases implementan el método especial \_\_str\_\_ para retornar una representación legible en texto de sus atributos.

CA-6 (no funcional): El código implementa obligatoriamente una clase base 'Mascota' de la cual heredan las clases derivadas 'Perro' y 'Gato', utilizando polimorfismo para el comportamiento específico.

