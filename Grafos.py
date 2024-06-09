class Grafos:
    # Constructor
    def __init__(self):
        # Inicia el grafo de hospitales creando una instancia
        self.Grafo = self.Red_Hospitales()
    
    # Define el grafo representando la red de hospitales y la distancia entre ellos
    def Red_Hospitales(self):
        Grafo = {
            "Hospital 1": {"Hospital 2": 3, "Hospital 3": 7},
            "Hospital 2": {"Hospital 1": 3, "Hospital 3": 6, "Hospital 4": 2},
            "Hospital 3": {"Hospital 1": 7, "Hospital 2": 6, "Hospital 4": 3},
            "Hospital 4": {"Hospital 2": 2, "Hospital 3": 3},
            "Hospital 5": {"Hospital 1": 4, "Hospital 3": 8, "Hospital 4": 7},
        }
        # Retorna el grafo
        return Grafo
    
    def Dijkstra(self, Inicio):
        # Inicia las distancias, todas son infinitas menos la de inicio
        Distancia = {Nodo: float("inf") for Nodo in self.Grafo}
        # Distancia al nodo de inicio es cero
        Distancia[Inicio] = 0
        # Inicia los predecesores de cada noso, inicialmente ninguno
        Previo = {Nodo: None for Nodo in self.Grafo}
        # Conjunto que lleva la cuenta de nodos visitados
        Visitados = set()
        # Lista de nodos del grafo
        Nodos = list(self.Grafo.keys())
        
        # Mientras no hayan nodos
        while Nodos:
            Nodo_Minimo = None
            Distancia_Minima = float("inf")
            
            # Encuentra el nodo con menor distancia que la actual
            for Nodo in Nodos:
                if Distancia[Nodo] < Distancia_Minima:
                    # Actualiza el nodo minimo y su distancia
                    Distancia_Minima = Distancia[Nodo]
                    Nodo_Minimo = Nodo
            
            # Si no encuentra un nodo minimo termina el bucle
            if Nodo_Minimo is None:
                break
            
            # Remueve el nodo minimo de la lista de nodos
            Nodos.remove(Nodo_Minimo)
            # Marca el nodo como visitado
            Visitados.add(Nodo_Minimo)
            
            # Actualiza las distancias a los vecinos del nodo minimo
            for Vecino, Peso in self.Grafo[Nodo_Minimo].items():
                # Salta los nodos que ya fueron visitados
                if Vecino in Visitados:
                    continue
                
                Nueva_Distancia = Distancia[Nodo_Minimo] + Peso
                
                if Nueva_Distancia < Distancia[Vecino]:
                    # Actualiza la distancia del vecino
                    Distancia[Vecino] = Nueva_Distancia
                    # Registra el predecesor del nodo
                    Previo[Vecino] = Nodo_Minimo
        
        # Retorna la distancia y los predecesores
        return Distancia, Previo

    def Recontruir_Camino(self, Previo, Inicio, Fin):
        # Lista que almacena el camino
        Camino = []
        # Comienza desde el nodo de destino
        Nodo_Actual = Fin
        
        # Recontruye el camino desde el nodo de destino
        while Nodo_Actual is not None:
            Camino.append(Nodo_Actual)
            # Mueve al predecesor del nodo actual
            Nodo_Actual = Previo[Nodo_Actual]
        
        # Invierte el camino para que vaya del inicio al destino
        Camino.reverse()
        # Retorna el camino reconstruido
        return Camino

    def Ruta_Mas_Corta(self, Origen, Destino):
        # Obtiene las distancias y los predecesores utilizando Dijkstra
        Distancia, Previo = self.Dijkstra(Origen)
        
        # Si la distancia es inficina no hay ruta disponible
        if Distancia[Destino] == float("inf"):
            return None, float("inf")
        
        # Reconstruye el camino desde el origen hasta el destino
        Camino = self.Recontruir_Camino(Previo, Origen, Destino)
        # Devuelve el camino y la distancia total
        return Camino, Distancia[Destino]

    def Transferencia(self, Origen, Destino):
        # Obtiene la ruta mas corta y la distancia
        Ruta, Distancia = self.Ruta_Mas_Corta(Origen, Destino)
        
        print(f"----- Solicitud de transferencia -----")
        print(f"Origen: {Origen}")
        print(f"Destino: {Destino}")

        # Imprime la ruta y distancia total
        if Ruta:
            print(f"Ruta: {' -> '.join(Ruta)}")
            print(f"Distancia total: {Distancia} unidades")
        # Imprime que no hay ruta disponible
        else:
            print(f"No hay una ruta disponible para esta transferencia")
        print()

# Ejemplo de uso
#if __name__ == "__main__":
#    grafo = Grafos()
#    grafo.Transferencia("Hospital 1", "Hospital 4")
#    grafo.Transferencia("Hospital 2", "Hospital 5")
