from cola import Queue

class PokemonTree:

    class __Node:
        def __init__(self, value, left=None, right=None, other_value=None):
            self.value = value
            self.left = left
            self.right = right
            self.other_value = other_value  # Almacena (numero, tipos)

    def __init__(self, key):
        self.root = None
        self.key = key  

    def insertar(self, nombre, numero, tipos):
        def __insertar(root, nombre, numero, tipos):
            if root is None:
                return PokemonTree.__Node(nombre, left=None, right=None, other_value=(numero, tipos))
            
            if self.key == "nombre":
                if nombre < root.value:
                    root.left = __insertar(root.left, nombre, numero, tipos)
                else:
                    root.right = __insertar(root.right, nombre, numero, tipos)
            elif self.key == "numero":
                if numero < root.other_value[0]:  # Comparar por el número almacenado en other_value
                    root.left = __insertar(root.left, nombre, numero, tipos)
                else:
                    root.right = __insertar(root.right, nombre, numero, tipos)
            elif self.key == "tipo":
                if tipos[0] < root.other_value[1][0]:  # Comparar por el primer tipo
                    root.left = __insertar(root.left, nombre, numero, tipos)
                else:
                    root.right = __insertar(root.right, nombre, numero, tipos)
            return root

        self.root = __insertar(self.root, nombre, numero, tipos)

    def buscar_por_nombre(self, nombre_parcial):
        resultado = []

        def __buscar(root, nombre_parcial):
            if root:
                if nombre_parcial.lower() in root.value.lower():
                    resultado.append((root.value, root.other_value[0], root.other_value[1]))
                __buscar(root.left, nombre_parcial)
                __buscar(root.right, nombre_parcial)

        __buscar(self.root, nombre_parcial)
        return resultado

    def buscar_por_numero(self, numero):
        def __buscar(root, numero):
            if root:
                if root.other_value[0] == numero:
                    return (root.value, root.other_value[0], root.other_value[1])
                elif numero < root.other_value[0]:
                    return __buscar(root.left, numero)
                else:
                    return __buscar(root.right, numero)
            return None

        return __buscar(self.root, numero)

    def lista_por_tipo(self, tipo):
        resultado = []

        def __lista_tipo(root, tipo):
            if root:
                if tipo in root.other_value[1]:  # Comprobar en other_value
                    resultado.append((root.value, root.other_value[0], root.other_value[1]))
                __lista_tipo(root.left, tipo)
                __lista_tipo(root.right, tipo)

        __lista_tipo(self.root, tipo)
        return resultado

    def in_order(self):
        resultado = []

        def __in_order(root):
            if root:
                __in_order(root.left)
                resultado.append((root.value, root.other_value[0], root.other_value[1]))
                __in_order(root.right)

        __in_order(self.root)
        return resultado

    def by_level(self):
        queue = Queue()
        resultado = []

        if self.root:
            queue.arrive(self.root)

        while queue.size() > 0:
            node = queue.attention()
            if node:
                resultado.append((node.value, node.other_value[0], node.other_value[1]))
                if node.left:
                    queue.arrive(node.left)
                if node.right:
                    queue.arrive(node.right)

        return resultado