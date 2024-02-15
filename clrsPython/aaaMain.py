from adjacency_list_graph import *
from dijkstra import *
from bellman_ford import *
import matplotlib.pyplot as plt
import pandas as pd
from mst import *
import time as tm


""" Loading the data """
# Read the Excel file
df = pd.read_excel("london_underground_data.xlsx")

""" Stripping empty spaces before and after the strings from the excel file"""
df['Line'] = df['Line'].str.strip()
df['Station'] = df['Station'].str.strip()
df['Connection'] = df['Connection'].str.strip()

filtered_dataset = df[df["Connection"].isna() & df['Time'].isna()]  # filtering for the stations without connections

i = 0
stations_to_int = {} # mapping station names to int
int_to_stations ={}  # mapping int to station names
connections = []  # list to store all the connected stations and their time
vertices = []


""" mapping stations to int  """
for column, row in filtered_dataset.iterrows():
    if row.iloc[1].upper() in stations_to_int:
        continue
    if row.iloc[1].upper() not in stations_to_int:
        stations_to_int[row.iloc[1].upper()] = i
        vertices.append(row.iloc[1])
        i += 1

""" mapping the int to station names """
for key in stations_to_int:
    int_to_stations[stations_to_int[key]] = key
    # vertices.append(stations_to_int[key])



filtered_dataset = df[df["Connection"].notna() & df['Time'].notna()]

for column, row in filtered_dataset.iterrows():
    connections.append((row.iloc[1].upper(), row.iloc[2].upper(), int(row.iloc[3]))) # Loading the connections for the graph

""" Intitializing a set for each line to use in task 4 when displaying closed down edges"""
bakerloo = set()
central = set()
circle = set()
district = set()
hammersmith_and_city = set()
jubilee = set()
metropolitan = set()
northern = set()
piccadilly = set()
victoria = set()
waterloo_and_city = set()


for column, row in filtered_dataset.iterrows():
    connections.append((row.iloc[1].upper(), row.iloc[2].upper(), int(row.iloc[3]))) # Loading the connections for the graph

    line = ""
    if type(row.iloc[0]) == str:
        line = row.iloc[0].upper()


    """Loading the sets for each line """
    if line == "BAKERLOO":
        line1 = stations_to_int[row.iloc[1].upper()]
        line2 = stations_to_int[row.iloc[2].upper()]
        bakerloo.add((line1, line2))
    if line == "CENTRAL":
        line1 = stations_to_int[row.iloc[1].upper()]
        line2 = stations_to_int[row.iloc[2].upper()]
        central.add((line1, line2))
    if line == "CIRCLE":
        line1 = stations_to_int[row.iloc[1].upper()]
        line2 = stations_to_int[row.iloc[2].upper()]
        circle.add((line1, line2))
    if line == "DISTRICT":
        line1 = stations_to_int[row.iloc[1].upper()]
        line2 = stations_to_int[row.iloc[2].upper()]
        district.add((line1, line2))
    if line == "HAMMERSMITH & CITY":
        line1 = stations_to_int[row.iloc[1].upper()]
        line2 = stations_to_int[row.iloc[2].upper()]
        hammersmith_and_city.add((line1, line2))
    if line == "JUBILEE":
        line1 = stations_to_int[row.iloc[1].upper()]
        line2 = stations_to_int[row.iloc[2].upper()]
        jubilee.add((line1, line2))
    if line == "METROPOLITAN":
        line1 = stations_to_int[row.iloc[1].upper()]
        line2 = stations_to_int[row.iloc[2].upper()]
    metropolitan.add((line1, line2))
    if line == "NORTHERN":
        line1 = stations_to_int[row.iloc[1].upper()]
        line2 = stations_to_int[row.iloc[2].upper()]
        northern.add((line1, line2))
    if line == "PICCADILLY":
        line1 = stations_to_int[row.iloc[1].upper()]
        line2 = stations_to_int[row.iloc[2].upper()]
        piccadilly.add((line1, line2))
    if line == "VICTORIA":
        line1 = stations_to_int[row.iloc[1].upper()]
        line2 = stations_to_int[row.iloc[2].upper()]
        victoria.add((line1, line2))
    if line == "WATERLOO & CITY":
        line1 = stations_to_int[row.iloc[1].upper()]
        line2 = stations_to_int[row.iloc[2].upper()]
        waterloo_and_city.add((line1, line2))

""" Sorting the connections by their  travel time, this way the lowest time will be loaded."""
connections = sorted(connections, key= lambda conect: conect[2])


""" Loading  the graph and creating the edges """
graph1 = AdjacencyListGraph(len(stations_to_int), directed=False, weighted=True)  # edg weights as travel time
graph2 = AdjacencyListGraph(len(stations_to_int), directed=False, weighted=True)  # edge weigths as stops



for i in range(len(connections)):
    station = stations_to_int[connections[i][0]]
    connected_st = stations_to_int[connections[i][1]]
    time = connections[i][2]
    try:
        graph1.insert_edge(station, connected_st, time)
        graph2.insert_edge(station, connected_st, 1)
    except RuntimeError as e:
        continue


def backtracking(starting_point, destination, distance, pi):
    shortest_route = []  # list for storing shortest-route
    journey_time = distance[destination]
    while True:
        if pi[destination] is not None:
            shortest_route.append(destination)
            destination = pi[destination]
        else:
            shortest_route.append(starting_point)
            break
    shortest_route = shortest_route[::-1]
    return shortest_route, journey_time

"""" Computing all station pair combinations and storing a list with  all the station pairs, stops, travel times"""
def calculate_all_shortest_paths(graph, station_names_to_ids, station_ids_to_names, shortest_path_algo):
    all_paths = []
    all_stops = []
    total_time = []
    computed_paths = {}

    for starting_point_id, starting_point_name in station_ids_to_names.items():
        # run dijkstra with station id nr
        if shortest_path_algo == dijkstra:
            dist, pi = dijkstra(graph, starting_point_id)
        elif shortest_path_algo == bellman_ford:
            dist, pi, cycle = bellman_ford(graph, starting_point_id)

        for destination_point_id, destination_point_name in station_ids_to_names.items():
            if starting_point_id != destination_point_id:
                path_key = tuple(sorted((starting_point_id, destination_point_id)))
                if path_key not in computed_paths:
                    # backtracking all stations from this starting point
                    path_with_id, shortest_path_time = backtracking(starting_point_id, destination_point_id, dist, pi)
                    # Computing the path and storing it in a dictionary
                    computed_paths[path_key] = shortest_path_time
                    path_by_name = []
                    # Not using this loop, might delete!
                    for stop in path_with_id:
                        path_by_name.append(station_ids_to_names[stop])

                    all_paths.append((starting_point_name, destination_point_name))
                    all_stops.append(len(path_by_name) - 1)
                    # print(shortest_path_time)
                    total_time.append(shortest_path_time)
                    # print("start:", starting_point_name, "destination:",  destination_point_name,"time:", time)
    return all_paths, all_stops, total_time

def display_histogram(histogram_data, bins, title, xlabel):

    plt.hist(histogram_data, bins=bins, edgecolor='black')

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Frequency')
    plt.show()

def user_input_route():
    """ Collection user input """
    starting_point = input("Please enter your first station:").upper()
    starting_point = stations_to_int[starting_point]
    destination = input("Please enter your destination station:").upper()
    destination = stations_to_int[destination]
    print("")  # console space
    return starting_point, destination


""" Task 1"""
print("Task 1")
# Subtask 1a
starting_point, destination = user_input_route()
d, pi = dijkstra(graph1, starting_point)

user_shortest_rt, shortest_path_time = backtracking(starting_point, destination, d, pi)
print("Your shortest route is:")
for station in user_shortest_rt:
    print("->", int_to_stations[station])

print("")
print(f"You have {len(user_shortest_rt)-1} stops until you reach your destination")
print(f"Your expected journey time is {shortest_path_time} minutes")
print("")

# Subtask 1b
station_pairs, stops, total_travel_times = calculate_all_shortest_paths(graph1, stations_to_int, int_to_stations, dijkstra)


bins = []
for i in range(0, max(total_travel_times)+1, 2):
    bins.append(i)

display_histogram(total_travel_times, bins, 'Travel Time Between Each Station Pair (Dijkstra)', 'Travel Time Range')

""" Task 2 """
print("Task 2")
# Subtask 2a
# starting_point, destination = user_input_route()
"""Taking user input for Task 2 """
d, pi = dijkstra(graph2, starting_point)
user_shortest_rt, shortest_path_time = backtracking(starting_point, destination, d, pi)

print("Your shortest route with the least number of stops is:")
for station in user_shortest_rt:
    print("->", int_to_stations[station])

print("")
print(f"You have {len(user_shortest_rt)-1} stops until you reach your destination")
print("")

# Subtask 2a
station_pairs, stops, total_travel_times = calculate_all_shortest_paths(graph2, stations_to_int, int_to_stations, dijkstra)

# print("STOPS", max(stops))
# print("Time", max(total_travel_times))
bins = []
for i in range(max(stops)+1):
    bins.append(i)

display_histogram(stops, bins, 'Number Of Stops Between Each Station Pair (Dijkstra)', 'Nr of Stops range')


""" Task 3 """
print("Task 3")
# Subtask 3a
starting_point, destination = user_input_route()
d, pi, cycle = bellman_ford(graph2, starting_point)
user_shortest_rt, shortest_path_time = backtracking(starting_point, destination, d, pi)
shortest_rt = []  # list for storing shortest-route
if cycle is False:
    i = 0
    while i <= len(pi):
        shortest_rt.append(destination)
        destination = pi[destination]
        i += 1
    print("Can't find shortest route, graph has a negative cycle")
    print("the negative cycle is between:", int_to_stations[shortest_rt[-1]], "-", int_to_stations[shortest_rt[-2]])
else:
    user_shortest_rt, shortest_path_time = backtracking(starting_point, destination, d, pi)

print("Your shortest route with the least number of stops is:")
for station in user_shortest_rt:
    print("->", int_to_stations[station])

print("")
print(f"You have {len(user_shortest_rt)-1} stops until you reach your destination")
print("")

# Subtask 3b
bf_station_pairs, bf_stops, bf_total_travel_times = calculate_all_shortest_paths(graph2, stations_to_int, int_to_stations, bellman_ford)
bins = []
# print("STOPS", max(bf_stops))
# print("Time:", max(total_travel_times))
for i in range(max(bf_stops)+2):
    bins.append(i)

display_histogram(bf_stops, bins, 'Number Of Stops Between Each Station Pair (Bellman-Ford)', 'Nr Of Stops Range')

""" Task 4 """
print("Task 4")
# Subtask 4a
mst_travel_time = kruskal(graph1)
mst_nr_of_stops = kruskal(graph2)

full_edge_list = set(graph1.get_edge_list())
max_closure = set(mst_travel_time.get_edge_list())
deleted_edges = full_edge_list.difference(max_closure)

bakerloo = bakerloo.intersection(deleted_edges)
central = central.intersection(deleted_edges)
circle = circle.intersection(deleted_edges)
district = district.intersection(deleted_edges)
hammersmith_and_city = hammersmith_and_city.intersection(deleted_edges)
jubilee = jubilee.intersection(deleted_edges)
metropolitan = metropolitan.intersection(deleted_edges)
northern = northern.intersection(deleted_edges)
piccadilly = piccadilly.intersection(deleted_edges)
victoria = victoria.intersection(deleted_edges)
waterloo_and_city = waterloo_and_city.intersection(deleted_edges)


print("London Underground will have the following connections closed down:")
print("Bakerloo Line: \n")
for closed_edges in bakerloo:
    print(int_to_stations[closed_edges[0]], "<->", int_to_stations[closed_edges[1]])
print("")

print("Central Line:")
for closed_edges in central:
    print(int_to_stations[closed_edges[0]], "<->", int_to_stations[closed_edges[1]])
print("")

print("Circle Line:")
for closed_edges in circle:
    print(int_to_stations[closed_edges[0]], "<->", int_to_stations[closed_edges[1]])
print("")

print("District Line:")
for closed_edges in district:
    print(int_to_stations[closed_edges[0]], "<->", int_to_stations[closed_edges[1]])
print("")

print("Hammersmith & City Line:")
for closed_edges in hammersmith_and_city:
    print(int_to_stations[closed_edges[0]], "<->", int_to_stations[closed_edges[1]])
print("")

print("Jubilee Line:")
for closed_edges in jubilee:
    print(int_to_stations[closed_edges[0]], "<->", int_to_stations[closed_edges[1]])
print("")

print("Metropolitan Line:")
for closed_edges in metropolitan:
    print(int_to_stations[closed_edges[0]], "<->", int_to_stations[closed_edges[1]])
print("")

print("Northern Line:")
for closed_edges in northern:
    print(int_to_stations[closed_edges[0]], "<->", int_to_stations[closed_edges[1]])
print("")

print("Piccadilly Line:")
for closed_edges in piccadilly:
    print(int_to_stations[closed_edges[0]], "<->", int_to_stations[closed_edges[1]])
print("")

print("Victoria Line:")
for closed_edges in victoria:
    print(int_to_stations[closed_edges[0]], "<->", int_to_stations[closed_edges[1]])
print("")

print("Waterloo & City Line:")
for closed_edges in waterloo_and_city:
    print(int_to_stations[closed_edges[0]], "<->", int_to_stations[closed_edges[1]])
print("")





# Subtask 4b
station_pairs, stops, total_travel_times = calculate_all_shortest_paths(mst_travel_time, stations_to_int, int_to_stations, dijkstra)

# print(max(total_travel_times))
bins = []
for i in range(0, max(total_travel_times)+1, 2):
    bins.append(i)

display_histogram(total_travel_times,bins, "Travel Time Between Each Station Par After Closure", "Travel Time Range")


""" Computing all the shortest route by stops after the MST closure """

station_pairs, stops, total_travel_times = calculate_all_shortest_paths(mst_nr_of_stops, stations_to_int, int_to_stations, dijkstra)
# print(max(stops))
bins = []
for i in range(max(stops)+1):
    bins.append(i)

display_histogram(stops, bins, 'Number Of Stops Between Each Station Pair After Closure', 'Nr Of Stops Range')


print("Dijkstra shortest path after Kruskal: \n ")
starting_point, destination = user_input_route()
d, pi = dijkstra(mst_travel_time, starting_point)
user_shortest_rt, shortest_path_time = backtracking(starting_point, destination, d, pi)
print("Your shortest route is:")
for station in user_shortest_rt:
    print("->", int_to_stations[station])

print("")
print(f"You have {len(user_shortest_rt)-1} stops until you reach your destination")
print(f"Your expected journey time is {shortest_path_time} minutes")
print("")



print("Initial Underground graph vs After closing down the edges with Kruskal")
print(graph1.get_card_E())
mst_travel_time = kruskal(graph1)
print(mst_travel_time.get_card_E())

print("Nr of Stations initial vs MST")
print(graph1.get_card_V())
print(mst_travel_time.get_card_V())
print("Deleted connections")
print(graph1.get_card_E() - mst_travel_time.get_card_E())
print("")
