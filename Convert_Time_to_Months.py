import pandas as pd

# Read the data from the text file
data = pd.read_csv('times.txt', delimiter='\t', header=None, names=['ID', 'Date'])

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])
data_sorted = data.sort_values(by='Date')
# Extract month from the datetime objects
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year
data['Months'] = (data['Year'] - 1992) * 12 + data['Month'] -2
# Replace the original values in the 'Date' column with the extracted month values
# data['ID']= str(data['ID'])

data.drop(['Date', 'Year','Month'], axis=1, inplace=True)
# Convert DataFrame to a nested Python list
data_list = data.values.tolist()

# Display the converted list
for d in data_list:
    n = d[0]
    no_digits = len(str(n))
    str_no = str(n)
    #check the number n starts with 11. 
    if(str_no[0] == '1' and str_no[1] == '1'):
        d[0] = int(str_no[2:])
    else:
        d[0] = int(str_no)

data = pd.DataFrame(data_list, columns=['ID', 'Months'])
data.to_csv('times.csv', index=False)
