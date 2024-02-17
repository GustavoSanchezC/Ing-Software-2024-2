#Gustavo Sanchez Castro
# Arbol

# Nodo del arbol
class Nodo:
    def __init__(self, val):
        self.valor = val
        self.izq= None
        self.der = None

class ArbolBinario:
    def __init__(self):
        self.root = None

    def insertar(self, val):
        if self.root is None:
            self.root = Nodo(val)
        else:
            self._insertar(val, self.root)

    def _insertar(self, val, nodo):
        if val < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(val)
            else:
                self._insertar(val, nodo.izq)
        else:
            if nodo.der is None:
                nodo.der = Nodo(val)
            else:
                self._insertar(val, nodo.der)

    def preorden(self):
        return self._preorden(self.root)

    def _preorden(self, nodo):
        if nodo is None:
            return []
        return [nodo.valor] + self._preorden(nodo.izq) + self._preorden(nodo.der)

    def inorden(self):
        return self._inorden(self.root)

    def _inorden(self, nodo):
        if nodo is None:
            return []
        return self._inorden(nodo.izq) + [nodo.valor] + self._inorden(nodo.der)

    def postorden(self):
        return self._postorden(self.root)

    def _postorden(self, nodo):
        if nodo is None:
            return []
        return self._postorden(nodo.izq) + self._postorden(nodo.der) + [nodo.valor]





def contar_valles(recorrido):
    if not set(recorrido).issubset({'D', 'U'}):
        raise ValueError("\nError, la cadena solo debe contener 'D' y 'U'.")

    valles = 0
    nivel = 0

    for paso in recorrido:
        nivel_previo = nivel
        nivel = nivel - 1 if paso == 'D' else nivel + 1

        if nivel_previo < 0 and nivel == 0:
            valles += 1

    return valles


if __name__ == "__main__":
    

    print("\nIngrese los valores para el arbol binario (separelos por ','):")
    tree_data = list(map(int, input().split(',')))
    tree = ArbolBinario()
    for valor in tree_data:
        tree.insertar(valor)
        
    
    
    print("Preorden:", tree.preorden())
    print("Inorden:", tree.inorden())
    print("Postorden:", tree.postorden())
    
    
    

    
    # Ingresar recorrido
    print("\nIngrese el recorrido (U arriba, D abajo),sin espacios:")
    recorrido = input()

    # Ejemplo de contar valles en la recorrido ingresada
    print("N° de valles:", contar_valles(recorrido))
    

