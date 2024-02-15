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

df['Line'] = df['Line'].str.strip()
df['Station'] = df['Station'].str.strip()
df['Connection'] = df['Connection'].str.strip()
filtered_dataset = df[df["Connection"].isna() & df['Time'].isna()]  # filtering for the stations without connections



for column, row in filtered_dataset.iterrows():
    print(type(row))
    print(len(row))
    print("Column: \n",column)
    print("Row \n", row)
    break


print("\n test 2 \n")


filtered_dataset = df[df["Connection"].notna() & df['Time'].notna()]

for column, row in filtered_dataset.iterrows():
    print("Column 2", column)
    print("row 2:", row)
    print( row.iloc[2] == "Kenton")
    break


