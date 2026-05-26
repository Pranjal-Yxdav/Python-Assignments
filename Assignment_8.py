import pandas as pd

date_series = pd.Series(['2024-01-01', '2024-02-15', '2024-03-10'])

time_series = pd.to_datetime(date_series)

print(time_series)

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['A', 'B', 'C']
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Marks': [80, 90, 70]
})

inner_merge = pd.merge(df1, df2, on='ID', how='inner')
print(inner_merge)

left_join = pd.merge(df1, df2, on='ID', how='left')
print(left_join)

right_join = pd.merge(df1, df2, on='ID', how='right')
print(right_join)

df1_index = df1.set_index('ID')
df2_index = df2.set_index('ID')

join_result = df1_index.join(df2_index, how='inner')
print(join_result)

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Dept': ['IT', 'HR', 'IT'],
    'Name': ['A', 'B', 'C']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Dept': ['IT', 'HR', 'Finance'],
    'Salary': [50000, 60000, 70000]
})

multi_merge = pd.merge(df1, df2, on=['ID', 'Dept'], how='inner')
print(multi_merge)

df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['A', 'B']})
df2 = pd.DataFrame({'ID': [3, 4], 'Name': ['C', 'D']})
df3 = pd.DataFrame({'ID': [1, 2, 3, 4], 'Marks': [50, 60, 70, 80]})

concat_df = pd.concat([df1, df2])
print(concat_df)

final_df = pd.merge(concat_df, df3, on='ID')
print(final_df)