#Open times.csv and plot the number of nodes vs months 
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import matplotlib.dates as mdates

#Open the file. The file has the following format:
#NodeID, TimeID
#1, 1
#2, 1
#3, 2

#Open the file
df = pd.read_csv('times.csv')

new_df = df['Months'].value_counts().reset_index()

# Rename the columns
new_df.columns = ['Month', 'No. of Papers Published']
sorted_df = new_df.sort_values(by='Month')
print(sorted_df)
# Plot the data. Months are in the x-axis and the number of papers published are in the y-axis. Plot a cummulative graph in a logarthimic scale
plt.plot(sorted_df['Month'], sorted_df['No. of Papers Published'])
# plt.yscale('log')
plt.xlabel('Months')
plt.ylabel('No. of Papers Published')
plt.title('Number of Papers Published vs Months')
plt.show()
plt.savefig('Number of Papers Published vs Months.png')
cumulative_papers = sorted_df['No. of Papers Published'].cumsum()

# Plot cumulative graph
plt.plot(sorted_df['Month'], cumulative_papers)
# plt.yscale('log')
plt.xlabel('Months')
plt.ylabel('Cumulative No. of Papers Published')
plt.title('Cumulative Number of Papers Published vs Months')
plt.show()
plt.savefig('Cumulative Number of Papers Published vs Months.png')
plt.close()
