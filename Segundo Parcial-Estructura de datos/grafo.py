from heap import HeapMin

class Graph:
    def __init__(self):
        self.personajes = []  

    def agregar_personaje(self, nombre):
        if not any(c['value'] == nombre for c in self.personajes):
            self.personajes.append({'value': nombre, 'aristas': []})

    def agregar_conexion(self, personaje1, personaje2, episodios_compartidos):
        node1 = next((c for c in self.personajes if c['value'] == personaje1), None)
        node2 = next((c for c in self.personajes if c['value'] == personaje2), None)
        
        if node1 and node2:
            node1['aristas'].append({'value': personaje2, 'peso': episodios_compartidos})
            node2['aristas'].append({'value': personaje1, 'peso': episodios_compartidos})

    def buscar_en_bosque(self, bosque, buscado):
        for index, arbol in enumerate(bosque):
            if buscado in arbol:
                return index
        return None

    def kruskal(self):
        bosque = []
        aristas = HeapMin()
        
        for nodo in self.personajes:
            bosque.append([nodo['value']])
            adjacentes = nodo['aristas']
            for adjacente in adjacentes:
                aristas.arrive([nodo['value'], adjacente['value']], adjacente['peso'])

        arbol_expansion = []

        while len(bosque) > 1 and aristas.elements:
            arista = aristas.atention()
            origen = self.buscar_en_bosque(bosque, arista[1][0])
            destino = self.buscar_en_bosque(bosque, arista[1][1])

            if origen is not None and destino is not None and origen != destino:
                arbol_expansion.append((arista[1][0], arista[1][1], arista[0]))

                bosque[origen].extend(bosque.pop(destino))

        
        contains_yoda = any("Yoda" in tree for tree in bosque)
        return arbol_expansion, contains_yoda

    def max_episodios_compartidos(self):
        max_episodios = 0
        max_par = None
        for personaje in self.personajes:
            for conexion in personaje['aristas']:
                if conexion['peso'] > max_episodios:
                    max_episodios = conexion['peso']
                    max_par = (personaje['value'], conexion['value'])
        return max_par, max_episodios

    def mostrar_grafo(self):
        for personaje in self.personajes:
            print(f"{personaje['value']} contectado con:")
            for conexion in personaje['aristas']:
                print(f" - {conexion['value']} ({conexion['peso']} episodios compartidos)")
