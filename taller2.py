class InventarioTienda:
    def __init__(self):
        self.categorias = {
            "legumbres": ["chochos", "frejol", "arvejas", "habas", "lenteja", "choclos", "tamarindo", "frejolNegro", "quinoa", "mani"]
        }
        self.inventario = {}
        self.asignarCostos()

    def asignarCostos(self):
        
        for categoria, productos in self.categorias.items():
            self.inventario[categoria] = {}
            for i, producto in enumerate(productos):
                self.inventario[categoria][producto] = (i + 1) * 1.0  

        
        for categoria, productos in self.inventario.items():
            print(f"Categoría: {categoria}")
            for producto, costo in productos.items():
                print(f"{producto}: ${costo:.2f}")
            print()

    def categorizarProductosPorPrecio(self):
        categoriasPorPrecio = {}
        for categoria, productos in self.inventario.items():
            for producto, costo in productos.items():
                if costo not in categoriasPorPrecio:
                    categoriasPorPrecio[costo] = []
                categoriasPorPrecio[costo].append(producto)

        
        for precio, productos in categoriasPorPrecio.items():
            print(f"Productos que cuestan ${precio:.2f}: {productos}")

    def calcularCostoTotalEnStock(self):
        costoTotal = 0.0
        for categoria, productos in self.inventario.items():
            for producto, costo in productos.items():
                costoTotal += costo

        return costoTotal



inventarioTienda = InventarioTienda()


inventarioTienda.asignarCostos()


inventarioTienda.categorizarProductosPorPrecio()


costoTotal = inventarioTienda.calcularCostoTotalEnStock()
print(f"El costo total en stock disponible es: ${costoTotal:.2f}")
