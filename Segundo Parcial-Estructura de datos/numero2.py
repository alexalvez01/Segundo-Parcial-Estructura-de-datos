from grafo import Graph

grafo = Graph()

personajes = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO", 
    "Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]
for personaje in personajes:
    grafo.agregar_personaje(personaje)

grafo.agregar_conexion("Luke Skywalker", "Darth Vader", 5)
grafo.agregar_conexion("Luke Skywalker", "Yoda", 3)
grafo.agregar_conexion("Luke Skywalker", "Leia", 4)
grafo.agregar_conexion("Darth Vader", "Leia", 2)
grafo.agregar_conexion("Leia", "Han Solo", 3)
grafo.agregar_conexion("Chewbacca", "Han Solo", 5)
grafo.agregar_conexion("Rey", "Kylo Ren", 4)
grafo.agregar_conexion("R2-D2", "C-3PO", 6)
grafo.agregar_conexion("BB-8", "Rey", 3)
grafo.agregar_conexion("Yoda", "R2-D2", 2)


print("---Grafo de personajes de Star Wars:")
grafo.mostrar_grafo()


arbol_expansion, contiene_yoda =grafo.kruskal()
print("---Árbol de expansión mínima:")
print(arbol_expansion)

if contiene_yoda:
    print("---El arbol de expansión minima contiene a Yoda")
else:
    print("---El arbol de expansión minima no contiene a Yoda")

max_par, max_episodios =grafo.max_episodios_compartidos()
print("---Personajes con el máximo número de episodios compartidos:")
print(f"{max_par[0]} y {max_par[1]} ({max_episodios} episodios compartidos)")