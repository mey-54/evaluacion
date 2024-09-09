class Vehiculo:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_atributos(self):
        return f"Llantas: {self.llantas}, Color: {self.color}, Precio: {self.precio}"

    def aplicar_descuento(self):
        if self.precio > 100000:
            descuento = self.precio * 0.10
            self.precio -= descuento
        return self.precio

class Moto(Vehiculo):
    def __init__(self, color, precio):
        super().__init__(llantas=2, color=color, precio=precio)

class Carro(Vehiculo):
    def __init__(self, color, precio):
        super().__init__(llantas=4, color=color, precio=precio)

# Crear objetos para cada clase
moto1 = Moto(color="Rojo", precio=120000)
carro1 = Carro(color="Azul", precio=150000)

# Mostrar atributos antes de aplicar el descuento
print("Antes del descuento:")
print("Moto:", moto1.mostrar_atributos())
print("Carro:", carro1.mostrar_atributos())

# Aplicar descuento
moto1.aplicar_descuento()
carro1.aplicar_descuento()

# Mostrar atributos después de aplicar el descuento
print("\nDespués del descuento:")
print("Moto:", moto1.mostrar_atributos())
print("Carro:", carro1.mostrar_atributos())
