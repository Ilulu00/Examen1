class Carrito:
    
    def __init__(self):
        self.productos = []
        self.total = 0
    
    def agregar_producto(self, producto: Producto) -> None: #temporalmente dara error, porque ni e importado la clase producto
        self.Producto.append(producto)
        self.total += producto.precio
        print(f"Se agrego el producto {producto.nombre}, de la categoria {producto.categoria} al carrito.")
    
    def quitar_producto(self, producto: Producto) -> None: #temporalmente dara error, porque ni e importado la clase producto
        if producto in self.Productos:
            self.Productos.remove(producto)
            self.total -= producto.precio
            print(f"Se quito el producto {producto.nombre} del carrito.")
        else:
            print(f"El producto {producto.nombre} no existe en el carrito.")
    
    def mostrar_carrito(self) -> None:
        print("====Carrito de Compras====")
        if not self.productos:
            print("Lo siento, no hay nada en tu carrito de compras.")
        else:
            for p in self.productos:  #For para iterar sobre los productos y mostrarlos
                print(f"- {p.nombre} -> ${p.precio}")
            print(f"Total: ${self.total}")
            