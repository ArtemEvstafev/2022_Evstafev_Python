import pandas as pd

df = pd.read_csv("transactions.csv")
print('Три наибольших платежа:\n', df[df['STATUS'] == 'OK'].sort_values(by='SUM', ascending=False).loc[:, 'SUM'].head(3))
print("\n")
print("Общая сумма для Umbrella, Inc: ",df[df['STATUS'] == 'OK'].groupby('CONTRACTOR').sum().loc['Umbrella, Inc','SUM'])


