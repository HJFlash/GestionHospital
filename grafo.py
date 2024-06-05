class grafo():
    def __init__(self):
        self.vertices = {}
        self.aristas = []
        self.cantidad_vertices = 0
        self.cantidad_aristas = 0

    def agregar_vertice(self, vertice):
        self.vertices[vertice] = self.cantidad_vertices
        self.cantidad_vertices += 1

    def agregar_arista(self, vertice1, vertice2, peso):
        self.aristas.append((vertice1, vertice2, peso))
        self.cantidad_aristas += 1

    def imprimir_grafo(self):
        print("Vertices: ")
        for vertice in self.vertices:
            print(vertice)
        print("Aristas: ")
        for arista in self.aristas:
            print(arista)