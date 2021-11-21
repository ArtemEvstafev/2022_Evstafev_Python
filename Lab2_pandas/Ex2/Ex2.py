import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("flights.csv")
print(df.groupby('CARGO').sum())

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(9, 3))
fig.set_figheight(9)
fig.set_figwidth(18)
Names = ['Jumbo', 'Medium', 'Nimble']
Colors = ['RED', 'BLUE', 'YELLOW']
ax1.bar(Names, [int(i) for i in df.groupby('CARGO').sum().loc[:, ['PRICE']].to_numpy()], color = Colors)
ax2.bar(Names, [int(i) for i in df.groupby('CARGO').sum().loc[:, ['WEIGHT']].to_numpy()], color = Colors)
ax3.bar(Names, [int(i) for i in df.groupby('CARGO').sum().loc[:, ['Unnamed: 0']].apply(lambda x: (1+(1+8*x)**0.5)/2).to_numpy()],color = Colors)

ax1.set_title('Полная стоимость')
ax2.set_title('Полная масса грузов')
ax3.set_title('Количество полётов')

plt.savefig('Result.png')
plt.show()