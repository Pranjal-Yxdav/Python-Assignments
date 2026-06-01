import pandas as pd

df = pd.read_csv("Assignment_9.csv")
print(df)

print(df.isnull().sum())

df['Marks'].fillna(df['Marks'].mean(), inplace=True)
print(df)

print("Average Marks:", df['Marks'].mean())

print("Highest Marks:", df['Marks'].max())

print("Lowest Marks:", df['Marks'].min())

mumbai_students = df[df['City'] == 'Mumbai']
print(mumbai_students)

city_avg = df.groupby('City')['Marks'].mean()
print(city_avg)

topper = df[df['Marks'] == df['Marks'].max()]
print("Top Performer:")
print(topper[['Name','Marks']])