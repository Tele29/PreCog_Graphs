import csv
import networkx as nx
import matplotlib.pyplot as plt
from concurrent.futures import ProcessPoolExecutor
import numpy as np
from cdlib import algorithms
# Function to read node data from CSV file
def read_nodes(filename):
    nodes = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            nodes[int(row[0])] = int(row[1])
    return nodes

# Function to read edge data from CSV file
def read_edges(filename):
    edges = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            source, target, timestep = map(int, row)
            edges.append((source, target, timestep))
    return edges

# Function to create a graph for a specific time step
def create_graph(timestep, nodes, edges):
    G = nx.DiGraph()
    for node, value in nodes.items():
        if value <= timestep:  # Add nodes based on the timestep
            G.add_node(node, value=value)
    for edge in edges:
        if edge[2] <= timestep:
            G.add_edge(edge[0], edge[1])
    giant_component_size = len(max(nx.weakly_connected_components(G), key=len))
    d = nx.average_clustering(G)
    print(d)
    return d

if __name__ == '__main__':
    # Read node and edge data
    nodes = read_nodes('final_nodes_time.csv')
    edges = read_edges('final_edges_time.csv')
    clustering_coefficients = []
    
    # Create a pool of processes
    with ProcessPoolExecutor() as executor:
        # Generate clustering coefficients for each time step in parallel
        clustering_results = [executor.submit(create_graph, timestep, nodes, edges) for timestep in range(1, max(edge[2] for edge in edges) + 1)]

        # Retrieve the generated clustering coefficients
        clustering_coefficients = [future.result() for future in clustering_results]
    clustering_coefficients = clustering_coefficients[40:]
    # Plot the clustering coefficient over time
    plt.plot(range(41, len(clustering_coefficients) + 41), clustering_coefficients)
    plt.xlabel('Time Step')
    plt.ylabel('Average Clustering Coefficient')
    plt.title('Averge Clustering Coefficient over Time')
    plt.show()
