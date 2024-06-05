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
            
    def minimo_vertice(self, distancias, visitados):
        min_distancia = float('inf')
        min_vertice = None
        for vertice in self.vertices:
            if not visitados[self.vertices[vertice]] and distancias[vertice] < min_distancia:
                min_distancia = distancias[vertice]
                min_vertice = vertice
        return min_vertice
    def dijsktra(self, vertice_inicial):
        distancias = {vertice: float('inf') for vertice in self.vertices}
        distancias[vertice_inicial] = 0
        visitados = [False] * self.cantidad_vertices
        for _ in range(self.cantidad_vertices):
            vertice = self.minimo_vertice(distancias, visitados)
            visitados[self.vertices[vertice]] = True
            for arista in self.aristas:
                if arista[0] == vertice:
                    distancias[arista[1]] = min(distancias[arista[1]], distancias[vertice] + arista[2])
        return distancias