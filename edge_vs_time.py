import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
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
plt.plot(np.arange(len(cumulative_edges)), cumulative_edges, marker='o')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Cummulative number of citations vs. Time')
plt.grid(True)
plt.show()

plt.plot(np.arange(len(edges_vs_time)), edges_vs_time)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('No of Citations Vs Time')
plt.grid(True)
plt.show()

x = []
for i in range(60, 122):
    x.append(i)
y = cumulative_edges[60:122]
x = np.array(x)
y = np.array(y)
model = LinearRegression()
model.fit(x.reshape(-1, 1), y)
y_pred = model.predict(x.reshape(-1, 1))
plt.scatter(x, y, label='Original Points')
plt.plot(x, y_pred, color='red', label='Approximating Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression on cumulative number of edges vs. time')
plt.legend()
plt.grid(True)
plt.show()