import csv
import networkx as nx
import matplotlib.pyplot as plt
from concurrent.futures import ProcessPoolExecutor
# Function to read node data from CSV file
Density = []
def read_nodes(filename):
    nodes = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # node, value = row[0].split(',')
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
def create_graph(timestep, nodes, edges):
    G = nx.DiGraph()
    for node, value in nodes.items():
        G.add_node(node, value=value)
    for edge in edges:
        if edge[2] <= timestep:
            G.add_edge(edge[0], edge[1])
    density = nx.density(G)
    print(density)
    return density
# Read node and edge data
if __name__ == '__main__':
    # Read node and edge data
    nodes = read_nodes('final_nodes_time.csv')
    edges = read_edges('final_edges_time.csv')
    densities = []
    
    # Create a pool of processes
    with ProcessPoolExecutor() as executor:
        # Generate graphs for each time step in parallel
        density_results = [executor.submit(create_graph, timestep, nodes, edges) for timestep in range(1, max(edge[2] for edge in edges) + 1)]

        # Retrieve the generated densities
        densities = [future.result() for future in density_results]
    plt.plot(range(1, len(densities) + 1), densities)
    plt.xlabel('Time Step')
    plt.ylabel('Density of the Graph')
    plt.yscale('log')
    plt.xscale('log')
    plt.title('Density of the Graph Over Time')
    plt.show()
    # Plot the time-dependent graph
    