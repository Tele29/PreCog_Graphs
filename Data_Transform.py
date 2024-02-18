import csv
mapping = {}
with open('times.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # Iterate over each row in the CSV file
    for row in reader:
        # Convert ID and Months to integers
        id_value = int(row['ID'])
        months_value = int(row['Months'])
        # Add the mapping to the dictionary
        mapping[id_value] = months_value

edges = []
with open('Cit-HepPh.txt', 'r') as file:
    # Skip the first few lines that contain comments
    for _ in range(4):
        next(file)
    
    # Iterate over each line in the file
    for line in file:
        # Split the line into two parts using tab as the delimiter
        parts = line.split('\t')
        # Extract the node IDs and convert them to integers
        from_node = int(parts[0])
        to_node = int(parts[1])
        # Add the edge to the list of edges
        if(from_node in mapping and to_node in mapping):
            edges.append((from_node, to_node))
edges_with_time = []
for edge in edges:
    from_node = edge[0]
    to_node = edge[1]
    from_time = mapping[from_node]
    
    edges_with_time.append((from_node, to_node, from_time))
# Save list to CSV
edges_with_time = sorted(edges_with_time, key=lambda x: x[2])
with open('final_edges_time.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(edges_with_time)



# Save dictionary to CSV
with open('final_nodes_time.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for key, value in mapping.items():
        writer.writerow([key, value])

# Save list to CSV
with open('final_edges.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(edges)

