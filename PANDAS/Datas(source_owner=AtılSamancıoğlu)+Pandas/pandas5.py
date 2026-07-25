import pandas as pd

print("\n#STEP_1")
weather_df = pd.read_excel("6-weather.xlsx")
print("weather_df=pd.read_excel('6-weather.xlsx')\nweather_df:\n", weather_df)

print("\nweather_df.head():\n", weather_df.head())
print("\nweather_df.tail():\n", weather_df.tail())
print(f"\nweather_df.info():")
print(weather_df.info())
print("\nweather_df.describe():\n", weather_df.describe())
print("\nweather_df.count():\n", weather_df.count())
print("\nweather_df.isna():\n", weather_df.isna())
print("\nweather_df.mean():\n", weather_df.mean())
print("\nweather_df.median():\n", weather_df.median())
print("\nweather_df.min():\n", weather_df.min())
print("\nweather_df.max():\n", weather_df.max())

print("\n#STEP_2")
weatherna_df = pd.read_excel("6-weatherna.xlsx")
print("weatherna_df=pd.read_excel('6-weatherna.xlsx')\nweatherna_df:\n", weatherna_df)

print("\nweatherna_df.describe():\n", weatherna_df.describe())
print("\nweatherna_df.count():\n", weatherna_df.count())
print("\nweatherna_df.mean():\n", weatherna_df.mean())
print("\nweatherna_df.isna():\n", weatherna_df.isna())
print("\nweatherna_df['Paris'].isna():\n", weatherna_df['Paris'].isna())
print("\nweatherna_df.dropna():\n", weatherna_df.dropna())
print("\nweatherna_df.fillna(5):\n", weatherna_df.fillna(5))
print("\nweatherna_df.fillna(weatherna_df.mean()):\n", weatherna_df.fillna(weatherna_df.mean()))

print("\n#STEP_3")

employees_df = pd.read_csv("6-employee.csv")
print("employees_df=pd.read_csv('6-employee.csv')\nemployees_df.head():\n", employees_df.head())

print("\nemployees_df.describe():\n", employees_df.describe())

print("\nemployees_df['City'].value_counts():\n", employees_df['City'].value_counts())
print("\nemployees_df[employees_df['City']=='Chicago']:\n", employees_df[employees_df['City'] == 'Chicago'])
print(
    "\nemployees_df[(employees_df['City']=='Chicago') & (employees_df['Experience']>=10)]:\n",
    employees_df[(employees_df['City'] == 'Chicago') & (employees_df['Experience'] >= 10)]
)

df_groupby = employees_df.groupby('City')
print("\ndf_groupby=employees_df.groupby('City')\ndf_groupby:\n", df_groupby)

print("\ndf_groupby.describe():\n", df_groupby.describe())
print("\ndf_groupby['Salary'].mean():\n", df_groupby['Salary'].mean())
print("\ndf_groupby['Experience'].max():\n", df_groupby['Experience'].max())

