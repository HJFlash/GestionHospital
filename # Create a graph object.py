from grafo import grafo
# Create a graph object
g = grafo()

# Add vertices
g.agregar_vertice("A")
g.agregar_vertice("B")
g.agregar_vertice("C")
g.agregar_vertice("D")

# Add edges
g.agregar_arista("A", "B", 5)
g.agregar_arista("B", "C", 3)
g.agregar_arista("C", "D", 2)
g.agregar_arista("A", "D", 10)

# Print the graph
g.imprimir_grafo()

# Run Dijkstra's algorithm
distancias = g.dijsktra("A")

# Print the distances from the initial vertex
print("Distancias from vertex A:")
for vertice, distancia in distancias.items():
    print(f"{vertice}: {distancia}")