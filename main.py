# Se crea una clase Nodo para representar cada elemento
class Nodo:
    def __init__(self, Expediente, Nombre):
        self.Expediente = Expediente
        self.Nombre = Nombre
        self.Izquierda = None # Hijo izquierdo del nodo
        self.Derecha = None # Hijo derecho del nodo

# Gestionar los registros de pacientes por número de expediente, permitiendo agregar, buscar y eliminar registros.
# Crear una interfaz para que los usuarios puedan agregar, buscar y eliminar registros de pacientes.
class BST:
    def __init__(self):
        self.Raiz = None # Inicia un arbol vacio
    
    # Encuentra el valor minimo en un subarbol
    def ValorMin(self, nodo):
        Actual = nodo # Asigna el nodo pasado a la variable
        # While funciona mientras haya un nodo a la izquierda
        while Actual.Izquierda is not None:
            # Mueve el nodo hacia su subnodo de menor valor, que corresponde al hijo izquierdo
            Actual = Actual.Izquierda
        # Devuelve el nodo con el valor minimo
        return Actual
    
    # Permite agregar pacientes tomando el expediente y nombre de estos
    def Agregar(self, Expediente, Nombre):
        # Crea un nuevo nodo con los valores de los parametros
        NuevoNodo = Nodo(Expediente, Nombre)
        
        # Comprueba si la raiz del nodo esta vacia
        if self.Raiz is None:
            # Si esta vacia establece el nuevo nodo como la raiz
            self.Raiz = NuevoNodo
        # Si no, se inserta el nuevo nodo en la posicion correcta
        else:
            # Inicia un puntero al nodo actual como la raiz del arbol
            NodoActual = self.Raiz
            # Funciona hasta encontrar la posicion correcta para insertar el nuevo nodo
            while True:
                # Confirma si el valor del nuevo nodo es menor que el valor del nodo actual
                if Expediente < NodoActual.Expediente:
                    # Si el nodo actual no tiene un hijo izquierdo:
                    if NodoActual.Izquierda is None:
                        # Coloca el nuevo nodo como el primer hijo del nodo actual
                        NodoActual.Izquierda = NuevoNodo
                        # Sale del bucle
                        break
                    # Si existe un hijo izquierdo:
                    else:
                        # Mueve el puntero al hijo izquierdo del nodo actual
                        NodoActual = NodoActual.Izquierda
                # Si el valor del nuevo nodo es mayor que el actual
                else:
                    # Si el nodo actual no tiene un hijo derecho
                    if NodoActual.Derecha is None:
                        # Coloca el nuevo nodo como el primer hijo del nodo actual
                        NodoActual.Derecha = NuevoNodo
                        # Sale del bucle
                        break
                    # Si exsite un hijo derecho:
                    else:
                        # Mueve el puntero al hijo derecho del nodo actual
                        NodoActual = NodoActual.Derecha
    
    # Busca el registro del paciente basado en el expediente
    def Buscar(self, Expediente):
        # Inicia una variable con la raiz del arbol
        Actual = self.Raiz
        # Mientras actual no sea none, quedan nodos por revisar
        while Actual is not None:
            # Si el expediente buscado coincide con el actual
            if Expediente == Actual.Expediente:
                # Retorna el nombre de ese nodo
                return Actual.Nombre
            # Su el ecpediente buscado es mejor al actual
            elif Expediente < Actual.Expediente:
                # Avanza al hijo izquierdo del actual
                Actual = Actual.Izquierda
            # Si el expediente buscado es mayor al actual
            else:
                # Avanza al hijo derecho del actual
                Actual = Actual.Derecha
        # Si no encuentra el expediente retorna none
        return None
    
    # Permite eliminar pacientes tomando el expediente
    def Eliminar(self, Expediente):
        # Inicia una variable Padre como none y Actual como la raiz del arbol
        Padre = None
        Actual = self.Raiz
        
        # Mientras actual no sea none y el expediente actual distinto al buscado
        while (Actual is not None) and (Actual.Expediente != Expediente):
            # Guarda el nodo actual como padre del nodo actual
            Padre = Actual
            # Si el expediente buscado es menor que el actual
            if Expediente < Actual.Expediente:
                # Avanza al hijo izquierdo del nodo actual
                Actual = Actual.Izquierda
            # Si el expediente buscado es mayor o igual que el actual
            else:
                # Avanza al hijo derecho del nodo actual
                Actual = Actual.Derecha
        
        # Si el nodo actual es None, el expediente buscado no se encontro
        if Actual is None:
            # Termina sin hacer nada mas
            return
        
        # Comprueba si el nodo actual no tiene hijos
        if (Actual.Izquierda is None) and (Actual.Derecha is None):
            # Si el nodo actual es la raiz del arbol
            if Actual == self.Raiz:
                # Cambia la raiz del arbol a none eliminando el nodo
                self.Raiz = None
            # Si el nodo actual es hijo izquierdo del padre
            elif Actual == Padre.Izquierda:
                # Cambia el hijo izquierdo a none eliminando el nodo
                Padre.Izquierda = None
            # Si el nodo actual es hijo derecho del padre
            else:
                # Cambia el hijo derecho a none eliminando el nodo
                Padre.Derecha = None
        
        # Si el nodo actual no tiene hijo izquierdo
        elif Actual.Izquierda is None:
            # Si el nodo actual es la raiz
            if Actual == self.Raiz:
                # Reemplaza la raiz con su hijo derecho
                self.Raiz = Actual.Derecha
            # Si el nodo actual es hijo izquierdo
            elif Actual == Padre.Izquierda:
                # Reemplaza el hijo izquierdo con el hijo derecho del nodo actual
                Padre.Izquierda = Actual.Derecha
            # Si el nodo actual es hijo derecho
            else:
                # Reemplaza al hijo derecho con el hijo derecho del nodo actual
                Padre.Derecha = Actual.Derecha
        
        # Si el nodo actual no tiene hijo derecho
        elif Actual.Derecha is None:
            # Si el nodo actual es la raiz
            if Actual == self.Raiz:
                # Reemplaza la raiz con su hijo izquierdo
                self.Raiz = Actual.Izquierda
            # Si el nodo actual es hijo izquierdo
            elif Actual == Padre.Izquierda:
                # Reemplaza el hijo izquierdo con el hijo izquierdo del nodo actual
                Padre.Izquierda = Actual.Izquierda
            # Si el nodo actual es hijo derecho
            else:
                # Reemplaza al hijo derecho con el hijo izquierdo del nodo actual
                Padre.Derecha = Actual.Izquierda
        
        # Si el nodo actual tiene hijo izquierdo y derecho
        else:
            # Encuentra al sucesor del nodo actual con valor minimo del subarbol derecho
            Sucesor = self.ValorMin(Actual.Derecha)
            # Almacena temporalmente el expediente del sucesor
            Temp_Expediente = Sucesor.Expediente
            # Almacena temporalmente el nombre del sucesor
            Temp_Nombre = Sucesor.Nombre
            # Elimina al sucesor del arbol
            self.Eliminar(Sucesor.Expediente)
            # Reemplaza el expediente del nodo actual con el del sucesor
            Actual.Expediente = Temp_Expediente
            # Reemplaza el nombre del nodo actual con el del sucesor
            Actual.Nombre = Temp_Nombre

# Uso
Bst = BST()
Bst.Agregar(1, "Paciente 1")
Bst.Agregar(2, "Paciente 2")
Bst.Agregar(3, "Paciente 3")

print(Bst.Buscar(2))
Bst.Eliminar(2)
print(Bst.Buscar(2))