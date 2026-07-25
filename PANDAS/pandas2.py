import pandas as pd
import numpy as np

print("\n#DATAFRAME")

print("\n#INTEGER_FRAME")
data = np.random.randint(1, 100, size=(4, 3))  # important
print("data:\n", data)

data_frame = pd.DataFrame(data)
print("\ndata_frame:\n", data_frame)
print("\nColumns:")
print("\ndata_frame[[0,2]]:\n", data_frame[[0, 2]]) # double brackets
print("\ndata_frame[1]:\n", data_frame[1])  # columns
print("\nIndexs:")
print("\ndata_frame.loc[0]:\n", data_frame.loc[0])  # rows
print("\ndata_frame.loc[1:3]:\n", data_frame.loc[1:3])
print("\nIndex+Column:")
print("\ndata_frame.loc[0][0]:\n", data_frame.loc[0][0])  # [row][column]
print("\ndata_frame.loc[0,0]:\n", data_frame.loc[0, 0])  # [row,column]
print("\ntype(data_frame):\n", type(data_frame))
print("\ntype(data_frame[1]):\n", type(data_frame[1]))

print("\n#STRING_FRAME")
clean_data_frame = pd.DataFrame(
    data,
    index=['Elif', 'Ayşe', 'Musa', 'Fatma'],
    columns=['feature1', 'feature2', 'feature3']
)
print("\nclean_data_frame:\n", clean_data_frame)
print("\nColumns:")
print("\nclean_data_frame[['feature1','feature3']]:\n", clean_data_frame[['feature1', 'feature3']])
print("\nclean_data_frame['feature2']:\n", clean_data_frame['feature2'])
print("\nIndex:\n")
print("\nclean_data_frame.loc['Elif']:\n", clean_data_frame.loc['Elif'])
print("\nclean_data_frame.iloc[0]:\n", clean_data_frame.iloc[0])
print("\nclean_data_frame.loc['Ayşe':'Musa']:\n", clean_data_frame.loc['Ayşe':'Musa'])
print("\nclean_data_frame.iloc[1:3]:\n", clean_data_frame.iloc[1:3])
print("\nIndex+Column:")
print("\nclean_data_frame.loc['Elif']['feature1']:\n", clean_data_frame.loc['Elif']['feature1'])
print("\nclean_data_frame.loc['Elif','feature1']:\n", clean_data_frame.loc['Elif', 'feature1'])
print("\nclean_data_frame.iloc[0]['feature1']:\n", clean_data_frame.iloc[0]['feature1'])
