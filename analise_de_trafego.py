#!/usr/bin/python
#coding: utf-8

import osmnx as ox
import networkx as nx

# define os pontos de origem e destino
origin = ox.distance.distance((45.5, -122.6), (45.5, -122.6))
destination = ox.distance.distance((45.51, -122.68), (45.51, -122.68))

# obtenha a rede de ruas
G = ox.graph_from_point(origin, distance=500, network_type='drive')

# calcule a rota mais curta entre os dois pontos
route = nx.shortest_path(G, origin, destination, weight='length')

# visualize a rota
ox.plot_graph_route(G, route, node_size=0, bgcolor='k')
