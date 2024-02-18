import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Load edges with time from CSV
edges_with_time = []
with open('final_edges_time.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        edges_with_time.append((int(row[0]), int(row[1]), int(row[2])))

# Load dictionary from CSV
mapping = {}
with open('final_nodes_time.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        mapping[int(row[0])] = int(row[1])
edges_vs_time = []
for i in range(0, 200):
    edges_vs_time.append(0)
for edge in edges_with_time:
    edges_vs_time[edge[2]]+=1
edges_vs_time = np.array(edges_vs_time)
edges_vs_time = edges_vs_time[0:122]
cumulative_edges = np.cumsum(edges_vs_time)
cumulative_edges = cumulative_edges[0:122]
df = pd.read_csv('final_nodes_time.csv', header=None, names=['ID', 'Months'])
new_df = df['Months'].value_counts().reset_index()

# Rename the columns
new_df.columns = ['Month', 'No. of Papers Published']
sorted_df = new_df.sort_values(by='Month')
sorted_df = sorted_df.values.tolist()
nodes = []
for i in sorted_df:
    nodes.append(i[1])
cum_node = []
for i in range(0, len(nodes)):
    cum_node.append(sum(nodes[0:i]))
#Change the scale of the plot to log
    
plt.plot(cum_node[20:], cumulative_edges[20:], marker='o')
plt.xlabel('Nodes Axis')
plt.xscale('log')
plt.ylabel('Citations Axis')
plt.yscale('log')
plt.title('Plot of number of papers vs. number of citations')
plt.grid(True)
plt.show()
