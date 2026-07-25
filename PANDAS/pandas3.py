import pandas as pd
import numpy as np

data = np.random.randint(1, 100, size=(4, 3))
print("data:\n", data)

data_frame = pd.DataFrame(
    data,
    index=['Person1', 'Person2', 'Person3', 'Person4'],
    columns=['Age', 'Weight', 'Height']
)
print("data_frame:\n", data_frame)

print("\n#COLUMN ADD")
data_frame['Extra'] = 10
print("data_frame['Extra'] = 10\ndata_frame:\n", data_frame)

print("\n#ROW COLUMN DELETE")
print("NOT: axis=0 -> row axis=1 -> column")
data_frame.drop('Extra', axis=1, inplace=True)
print("data_frame.drop('Extra',axis=1,inplace=True)\ndata_frame:\n", data_frame)

data_frame.drop('Person4', inplace=True)
print("\ndata_frame.drop('Person4',inplace=True)\ndata_frame:\n", data_frame)

print("\n#DATA CHANGING")
data_frame.loc['Person1', 'Age'] = 19  # Error: ['Person1'],['Age']
print("data_frame.loc['Person1','Age']=19\ndata_frame:\n", data_frame)

print("\n#DATAFRAME SELECT")
print("data_frame<20:\n", data_frame < 20)
print("\ndata_frame[data_frame<20]:\n", data_frame[data_frame < 20])
print("\ndata_frame[data_frame['Age']<20]:\n", data_frame[data_frame['Age'] < 20])

print("\n#RESET INDEX")
print("data_frame.reset_index():\n", data_frame.reset_index())

new_indexs = ['p1', 'p2', 'p3'] #unindexed
new_column = pd.Series([1, 2, 3]) #indexed

print("\n#COLUMN ADD")
print("new_column(indexed=Series):\n", new_column)
data_frame['New_Column'] = new_column.values  # no indexs!
print("data_frame['New_Column']=new_column.values\ndata_frame:\n", data_frame)

print("\n#INDEX CHANGING")
print("new_indexs(unindexed):\n", new_indexs)
data_frame.set_index(pd.Index(new_indexs), inplace=True)
print("data_frame.set_index(pd.Index(new_indexs),inplace=True)\ndata_frame:\n", data_frame)
