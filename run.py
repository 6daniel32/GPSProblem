# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())
print(search.cost_first_graph_search(ab).path())
print(search.heuristic_cost_first_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

# hay que buscar en función de menor path cost acumulado. Crear un metodo que reordene la lista abierta, poniendo delante los de
#menor path cost. en el codigo ya esta implementado el path cost en la clase node del archivo search. Lo pasa la clase problem. GPSProblem tiene la funcion path_cost
#La funcion expand del nodo tambien tiene cosas. Suma el path cost actual al de los hijos.
#En este fichero crear un nuevo print con parametro ab pero otra funcion de busqueda
#En Graph_search añadir una nueva funcion de busqueda que no sea anchura ni profundidad con otro gestor de colas (ni fifo ni nada) -> en util crear una nueva estructura de datos que
#implemente busqueda con menor coste. En el extend tiene que tener también la reordenaciön de la lista
#del enunciado de la practica solo hacer lo primero