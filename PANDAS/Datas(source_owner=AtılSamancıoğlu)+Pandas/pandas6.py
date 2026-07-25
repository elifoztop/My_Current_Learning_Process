import pandas as pd

print("\n#CONCAT")

df1=pd.read_csv("7-concat_data1.csv")
df2=pd.read_csv("7-concat_data2.csv")

print(df1)
print(df2)

df_concat = pd.concat([df1,df2],ignore_index=True)
print(df_concat)

print("\n#MERGE")

df3=pd.read_csv("7-merge_data1.csv")
df4=pd.read_csv("7-merge_data2.csv")
print(df3)
print(df4)

df_outher=pd.merge(df3,df4,on="Employee_ID",how="outer")
print(df_outher)

df_inner=pd.merge(df3,df4,on="Employee_ID",how="inner")
print(df_inner)

df_left=pd.merge(df3,df4,on="Employee_ID",how="left") #first df
print(df_left)

df_right=pd.merge(df3,df4,on="Employee_ID",how="right") #second df
print(df_right)