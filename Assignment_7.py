import pandas as pd

#data = {'a': 10, 'b': 20, 'c': 30}
#s = pd.Series(data)
#print(s)

#data = [1, 2, 3, 4, 5]
#s = pd.Series(data)
#print(s)

#print(s[0])       
#print(s[1:4])     

#data = [[1, 'A'], [2, 'B'], [3, 'C']]
#df = pd.DataFrame(data, columns=['ID', 'Name'])
#print(df)

#data = {'Name': ['A', 'B', 'C'], 'Age': [20, 21, 22]}
#df = pd.DataFrame(data)
#print(df)

#data = [['A', 20], ['B', 21], ['C', 22]]
#df = pd.DataFrame(data, columns=['Name', 'Age'])
#print(df)

data = [
    {'Name': 'A', 'Age': 20},
    {'Name': 'B', 'Age': 21},
    {'Name': 'C', 'Age': 22}
]
df = pd.DataFrame(data)
print(df)

for index, row in df.iterrows():
    print(index, row['Name'], row['Age'])

for row in df.itertuples():
    print(row.Name, row.Age)

print(df[df['Age'] > 20])

print(df.iloc[1])     

print(df.loc[0:1, ['Name']])

df = df[df['Age'] > 20]
print(df)

new_row = {'Name': 'D', 'Age': 23}

df1 = df.iloc[:1]
df2 = df.iloc[1:]

df = pd.concat([df1, pd.DataFrame([new_row]), df2]).reset_index(drop=True)
print(df)

row_list = df.values.tolist()
print(row_list)