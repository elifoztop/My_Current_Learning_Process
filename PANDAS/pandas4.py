import pandas as pd
import numpy as np

print("\n#MULTI INDEXS DATAFRAME")

index1 = ['Men', 'Men', 'Women', 'Women']
print("index1:\n", index1)

index2 = ['Ali', 'Veli', 'Elif', 'Gül']
print("index2:\n", index2)

zip_index = list(zip(index1, index2))
print("zip_index=list(zip(index1,index2))\nzip_index:\n", zip_index)

zip_index = pd.MultiIndex.from_tuples(zip_index)
print("\nzip_index=pd.MultiIndex.from_tuples(zip_index)\nzip_index:\n", zip_index)

big_df = pd.DataFrame(np.random.randn(4, 2), index=zip_index, columns=['A', 'B'])
print("\nbig_df=pd.DataFrame(np.random.randn(4,2),index=zip_index,columns=['A','B'])\nbig_df:\n", big_df)

print("\nbig_df.loc['Men']:\n", big_df.loc['Men'])
print("\nbig_df.loc['Men'].loc['Ali']:\n", big_df.loc['Men'].loc['Ali'])
