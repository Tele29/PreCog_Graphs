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
#Save the sorted_df as a csv file
sorted_df.to_csv('times.csv', index=False)