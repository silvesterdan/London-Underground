from adjacency_list_graph import *
from dijkstra import *
from bellman_ford import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from bellman_ford import *



stations_to_int = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

""" Connected  stations and their wight """
int_to_stations = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"}

connections = [
    ("A", "C", 7),
    ("A", "D", 10),
    ("C", "D", 9),
    ("D", "B", 2),
    ("B", "E", 5),
    #("E", "D", 7)
]


""" Loading  the graph and creating the edges """
graph1 = AdjacencyListGraph(len(stations_to_int), directed=False, weighted=True)
for i in range(len(connections)):
    station = stations_to_int[connections[i][0]]
    connected_st = stations_to_int[connections[i][1]]
    time = connections[i][2]
    try:
        graph1.insert_edge(station, connected_st, time)
    except RuntimeError as e:
        continue
print(graph1)

starting_point = input("Please enter your first station:").upper()
starting_point = stations_to_int[starting_point]
destination = input("Please enter your destination station:").upper()
destination = stations_to_int[destination]
print("")  # console space

d, pi, cycle = bellman_ford(graph1, starting_point)

def backtracking(starting_point, destination, pi, cycle):
    shortest_route = []    # list for storing shortest-route
    if cycle == False:
        print("false")
        i = 0
        while i <= len(pi):
            shortest_route.append(destination)
            destination = pi[destination]
            i+= 1
    else:
        print("else")
        while True:
            if pi[destination] is not None:
                shortest_route.append(destination)
                destination = pi[destination]
            else:
                shortest_route.append(starting_point)
                break
    shortest_route = shortest_route[::-1]
    return shortest_route

""" 
Calling Bellman ford and printing shortest route
And if there is a cycle printing the the cycle location
"""

shortest_rt = backtracking(starting_point, destination, pi, cycle)
if cycle is True:
    print(shortest_rt)
else:
    print("Can't find shortest route, graph has a negative cycle")
    print("the cycle is:", shortest_rt)


