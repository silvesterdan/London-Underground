The software is located in the library directory of clrsPython.

 * And the main Python file is called 'aaaMain.py'.
 And the Excel file containing the London Underground data that is loaded in the aaaMain is in london_underground_data.xlsx file.

Installation:
    This project requires Python 3.x and several Python packages listed in 'requirements.txt'.

London Underground Network Analysis

Overview
This script provides a comprehensive analysis of the London Underground network, focusing on calculating the shortest paths between stations, analyzing travel times and number of stops,
and applying graph algorithms to optimize the network. It uses data from an Excel file containing information about stations, lines, and connections.

Key Features

1. Shortest Path Analysis: Calculates the shortest paths between any two stations based on travel time and number of stops using Dijkstra's algorithm.

2. Graph Optimization: Applies Bellman-Ford and Kruskal's algorithms to identify negative cycles and to optimize the network by finding the Minimum Spanning Tree (MST).

3. Data Visualization: Generates histograms to visualize the distribution of travel times and number of stops across all station pairs.

4. Impact Analysis Post-Optimization: Analyzes the impact on travel times and stops after applying MST closure using Kruskal's algorithm.

How to Use

1. Prepare the Data: Ensure you have an Excel file named 'london_underground_data.xlsx' with columns for 'Line', 'Station', 'Connection', and 'Time'.

2. Run the Script: Execute the script in a Python environment. The script will automatically load and process the data from the Excel file.

3. Input Queries: The script will prompt you to enter starting and destination stations for various tasks. Input the station names as requested.
For Example:
    Please enter your first station:Victoria
    Please enter your destination station:bank

4. View Results: The script outputs the results directly in the console, including the shortest routes, journey times, stops, and histograms for travel time and stop distributions.

5. Graph Analysis: Observe the output related to graph optimization and the effects of applying Kruskal's algorithm on the network.
