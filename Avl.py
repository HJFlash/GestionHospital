# Representa un nodo en el arbol
class Nodo:
    def __init__(self, Clave, Valor):
        self.Clave = Clave # Clave para ordenar el nodo
        self.Valor = Valor # Valor asociado a la clave
        self.Izquierdo = None # Hijo izquierdo del nodo
        self.Derecho = None # Hijo derecho del nodo
        self.Altura = 1 # Altura del nodo

# Clase del arbol AVL
class Avl:
    def __init__(self):
        self.Raiz = None # Raiz del arbol
        
    # Funcion para obtener altura del nodo
    def Obtener_Altura(self, nodo):
        if not nodo:
            return 0
        return nodo.Altura
    
    # Funcion para obtener factor de balance del nodo
    def Obtener_Balance(self, nodo):
        if not nodo:
            return 0
        return self.Obtener_Altura(nodo.Izquierda) - self.Obtener_Altura(nodo.Derecho)
    
    # Rotacion Derecha
    def Rotacion_Derecha(self, y):
        x = y.Izquierdo
        T2 = x.Derecho
        x.Derecho = y
        y.Izquierdo = T2
        y.Altura = max(self.Obtener_Altura(y.Izquierdo), self.Obtener_Altura(y.Derecho)) + 1
        x.Altura = max(self.Obtener_Altura(x.Izquierdo), self.Obtener_Altura(x.Derecho)) + 1
        return x
    
    # Rotacion Izquierda
    def Rotacion_Izquierda(self, x):
        y = x.Izquierdo
        T2 = y.Derecho
        y.Izquierdo = x
        x.Derecho = T2
        x.Altura = max(self.Obtener_Altura(x.Izquierdo), self.Obtener_Altura(x.Derecho)) + 1
        y.Altura = max(self.Obtener_Altura(y.Izquierdo), self.Obtener_Altura(y.Derecho)) + 1
        return y
    
    # Funcion para insertar un nodo
    def Insertar(self, nodo, Clave, Valor):
        if not nodo:
            return Nodo(Clave, Valor)
        elif Clave < nodo.Clave:
            nodo.Izquierdo = self.Insertar(nodo.Izquierdo, Clave, Valor)
        else:
            nodo.Derecho = self.Insertar(nodo.Derecho, Clave, Valor)
        
        # Actualiza la altura del nodo ancestro
        nodo.Altura = max(self.Obtener_Altura(nodo.Izquierdo), self.Obtener_Altura(nodo.Derecho)) +1
        # Obtiene el factor de balance del nodo ancestro
        Balance = self.Obtener_Balance(nodo)
        
        # Rotaciones para balancear el arbol
        # Rotacion derecha
        if (Balance > 1) and (Clave < nodo.Izquierdo.Clave):
            return self.Rotacion_Derecha(nodo)
        # Rotacion izquierda
        if (Balance < -1) and (Clave > nodo.Derecho.Clave):
            return self.Rotacion_Izquierda(nodo)
        # Rotacion izquierda - derecha
        if (Balance > 1) and (Clave > nodo.Izquierdo.Clave):
            nodo.Izquierdo = self.Rotacion_Izquierda(nodo.Izquierdo)
            return self.Rotacion_Derecha(nodo)
        # Rotacion derecha - izquierda
        if (Balance < -1) and (Clave < nodo.Derecho.Clave):
            nodo.Derecho = self.Rotacion_Derecha(nodo.Derecho)
            return self.Rotacion_Izquierda(nodo)
        
        return nodo
    
    # Funcion para buscar nodo
    def Buscar(self, nodo, Clave):
        if not nodo or (nodo.Clave == Clave):
            return nodo
        elif (Clave < nodo.Clave):
            return self.Buscar(nodo.Izquierdo, Clave)
        return self.Buscar(nodo.Derecho, Clave)
    
    # Funcion para recorrer el arbol en orden
    def Recorrer(self, nodo, Resultado):
        if nodo:
            self.Recorrer(nodo.Izquierdo, Resultado)
            Resultado.append(nodo.Valor)
            self.Recorrer(nodo.Derecho, Resultado)
            
# Inicia el arbol AVL
#Arbol = Avl()

# Funcion para ver lista de doctores
#def Ver_Doctores():
#    Resultado = []
#    Arbol.Recorrer(Arbol.Raiz, Resultado)
#    return Resultado

# Funcion para agregar doctores
#def Agregar_Doctor(Id, Datos):
#    Datos["id"] = Id
#    Arbol.Raiz = Arbol.Insertar(Arbol.Raiz, Id, Datos)

# Funcion para buscar doctores
#def Buscar_Doctor(Id):
#    nodo = Arbol.Buscar(Arbol.Raiz, Id)
#    if nodo:
#        return nodo.Valor
#    else: 
#        return "No se encontro el doctor"
    
# Ejemplo de uso
#Agregar_Doctor(2, {"nombre": "Juan", "area": "Cardiologia"})
#Agregar_Doctor(1, {"nombre": "Maria", "area": "neurologia"})

# Ver lista
#print("----- Lista de doctores -----")
#Doc = Ver_Doctores()
#for Doctor in Doc:
#    print(f"- Id: {Doctor['Id']}, Nombre: {Doctor['nombre']}, Area: {Doctor['area']}")

## Buscar
#Id_Buscado = 1
#print(f"Id bucado: {Id_Buscado}")
#Res = Buscar_Doctor(Id_Buscado)
#if isinstance(Res, dict):
#   print(f"Nombre: {Doctor['nombre']}, Area: {Doctor['area']}")
#else:
#    print(Res)
