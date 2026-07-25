import pandas as pd
import numpy as np

print("\n#SERIES")

my_dict = {'Elif': 19, 'Ayşe': 16, 'Musa': 50, 'Fatma': 49}
names = ['Elif', 'Ayşe', 'Musa', 'Fatma']
ages = [19, 16, 50, 49]

print("\nmy_dict:\n",my_dict)
print("names:\n",names)
print("ages:\n",ages)
print("\npd.Series(my_dict):\n", pd.Series(my_dict))
print("\npd.Series(ages, index=names):\n", pd.Series(ages, index=names))
print("\npd.Series(ages, index=ages):\n", pd.Series(ages, index=ages))
print("\npd.Series(np.array(ages)):\n", pd.Series(np.array(ages)))

my_series = pd.Series([19, 16, 50, 49], ['Elif', 'Ayşe', 'Musa', 'Fatma'])

print("\nmy_series:\n", my_series)
print("\nmy_series['Elif']:", my_series['Elif'])