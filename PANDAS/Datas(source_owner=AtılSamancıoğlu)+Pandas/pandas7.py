import pandas as pd
import inspect

df = pd.read_csv("8-apply_function_data.csv")
print("df=pd.read_csv('8-apply_function_data.csv')\ndf.head():\n", df.head())
print("\ndf.tail():\n", df.tail())
print("\ndf.columns:\n", df.columns)


def performance_catergory(score):
    if score > 3:
        return "Excellent "
    elif score < 3:
        return "Good"
    else:
        return "Bad"


print("\n#FUNCTION: performance_catergory\n", inspect.getsource(performance_catergory))
print("df['Performance_Score'].apply(performance_catergory).head():\n",
      df['Performance_Score'].apply(performance_catergory).head())

df['Performance_Category'] = df['Performance_Score'].apply(performance_catergory)
print("\ndf['Performance_Category']=df['Performance_Score'].apply(performance_catergory)\ndf[['Performance_Score','Performance_Category']].head():\n",
      df[['Performance_Score', 'Performance_Category']].head())


def new_score1(experience):
    if experience >= 10:
        return 1
    else:
        return 0


print("\n#FUNCTION: new_score1\n", inspect.getsource(new_score1))
df['Returns'] = df['Experience'].apply(new_score1)
print("df['Returns']=df['Experience'].apply(new_score1)\ndf[['Experience','Returns']].head():\n",
      df[['Experience', 'Returns']].head())

df['New_Score1'] = df['Returns'] + df['Performance_Score']
print("\ndf['New_Score1']=df['Returns']+df['Performance_Score']\ndf[['Performance_Score','Returns','New_Score1']].head():\n",
      df[['Performance_Score', 'Returns', 'New_Score1']].head())

df.drop('Returns', axis=1, inplace=True)
print("\ndf.drop('Returns',axis=1,inplace=True)\ndf[['Performance_Score','New_Score1']].head():\n",
      df[['Performance_Score', 'New_Score1']].head())


def new_score2(row):
    if row['Experience'] >= 10:
        return row['Performance_Score'] + 1
    else:
        return row['Performance_Score']


print("\n#FUNCTION: new_score2\n", inspect.getsource(new_score2))
df['New_Score2'] = df.apply(new_score2, axis=1)
print("df['New_Score2']=df.apply(new_score2,axis=1)\ndf[['Performance_Score','New_Score2']].head():\n",
      df[['Performance_Score', 'New_Score2']].head())

df['New_Name'] = df['Name'].apply(lambda x: x.replace("_", " "))
print("\ndf['New_Name']=df['Name'].apply(lambda x : x.replace('_',' '))\ndf[['Name','New_Name']].head():\n",
      df[['Name', 'New_Name']].head())