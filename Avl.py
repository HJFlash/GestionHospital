

class NodoAVL:
    def __init__(self, clave, nombre):
        self.clave = clave
        self.nombre = nombre
        self.altura = 1
        self.izquierda = None
        self.derecha = None

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    def rotacion_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha
        x.derecha = y
        y.izquierda = T2
        y.altura = max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha)) + 1
        x.altura = max(self.obtener_altura(x.izquierda), self.obtener_altura(x.derecha)) + 1
        return x

    def rotacion_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda
        y.izquierda = x
        x.derecha = T2
        x.altura = max(self.obtener_altura(x.izquierda), self.obtener_altura(x.derecha)) + 1
        y.altura = max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha)) + 1
        return y

    def insertar(self, raiz, clave, nombre):
        if not raiz:
            return NodoAVL(clave, nombre)
        elif clave < raiz.clave:
            raiz.izquierda = self.insertar(raiz.izquierda, clave, nombre)
        else:
            raiz.derecha = self.insertar(raiz.derecha, clave, nombre)

        raiz.altura = max(self.obtener_altura(raiz.izquierda), self.obtener_altura(raiz.derecha)) + 1

        balance = self.obtener_balance(raiz)

        # Rotaciones para mantener el árbol balanceado
        if balance > 1 and clave < raiz.izquierda.clave:
            return self.rotacion_derecha(raiz)
        if balance < -1 and clave > raiz.derecha.clave:
            return self.rotacion_izquierda(raiz)
        if balance > 1 and clave > raiz.izquierda.clave:
            raiz.izquierda = self.rotacion_izquierda(raiz.izquierda)
            return self.rotacion_derecha(raiz)
        if balance < -1 and clave < raiz.derecha.clave:
            raiz.derecha = self.rotacion_derecha(raiz.derecha)
            return self.rotacion_izquierda(raiz)

        return raiz

    def buscar(self, raiz, clave):
        if not raiz or raiz.clave == clave:
            return raiz
        elif clave < raiz.clave:
            return self.buscar(raiz.izquierda, clave)
        else:
            return self.buscar(raiz.derecha, clave)

    def eliminar(self, raiz, clave):
        if not raiz:
            return raiz
        
        if clave < raiz.clave:
            raiz.izquierda = self.eliminar(raiz.izquierda, clave)
        elif clave > raiz.clave:
            raiz.derecha = self.eliminar(raiz.derecha, clave)
        else:
            if raiz.izquierda is None:
                temp = raiz.derecha
                raiz = None
                return temp
            elif raiz.derecha is None:
                temp = raiz.izquierda
                raiz = None
                return temp

            temp = self.min_valor_nodo(raiz.derecha)
            raiz.clave = temp.clave
            raiz.derecha = self.eliminar(raiz.derecha, temp.clave)

        if raiz is None:
            return raiz

        raiz.altura = 1 + max(self.obtener_altura(raiz.izquierda), self.obtener_altura(raiz.derecha))
        balance = self.obtener_balance(raiz)

        # Rotaciones para mantener el árbol balanceado
        if balance > 1 and self.obtener_balance(raiz.izquierda) >= 0:
            return self.rotacion_derecha(raiz)
        if balance < -1 and self.obtener_balance(raiz.derecha) <= 0:
            return self.rotacion_izquierda(raiz)
        if balance > 1 and self.obtener_balance(raiz.izquierda) < 0:
            raiz.izquierda = self.rotacion_izquierda(raiz.izquierda)
            return self.rotacion_derecha(raiz)
        if balance < -1 and self.obtener_balance(raiz.derecha) > 0:
            raiz.derecha = self.rotacion_derecha(raiz.derecha)
            return self.rotacion_izquierda(raiz)

        return raiz

    def min_valor_nodo(self, nodo):
        actual = nodo

        while actual.izquierda is not None:
            actual = actual.izquierda

        return actual

    def imprimir_in_order(self, raiz):
        if raiz:
            self.imprimir_in_order(raiz.izquierda)
            print(f"Clave: {raiz.clave}, Nombre: {raiz.nombre}")
            self.imprimir_in_order(raiz.derecha)

    def obtener_lista_doctores(self):
        doctores = []
        self._in_order_traversal(self.raiz, doctores)
        return doctores

    def _in_order_traversal(self, nodo, doctores):
        if nodo is not None:
            self._in_order_traversal(nodo.izquierda, doctores)
            doctores.append(nodo)
            self._in_order_traversal(nodo.derecha, doctores)
