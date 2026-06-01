import pandas as pd

dates = pd.Series(pd.date_range('2026-05-27', periods=5))

print(dates)

print(pd.Timestamp.now())

df = pd.DataFrame({
    'Date':['2026-05-27','2026-07-10','2026-08-15']
})
df['Date'] = pd.to_datetime(df['Date'])
print(df)

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
print(df)

df['Day_Name'] = df['Date'].dt.day_name()
print(df)

start = pd.Timestamp('2026-05-27')
end = pd.Timestamp('2026-06-27')
difference = end - start
print(difference.days)

filtered = df[df['Date'] > '2026-07-01']
print(filtered)