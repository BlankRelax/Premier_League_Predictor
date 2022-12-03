import pandas as pd
from pathlib import Path

df = pd.read_csv('Performance_Data_Football_Teams.csv')
Leagues = ['Premier League']
df = df[df['League'].isin(Leagues)]
print(len(df))
filepath = Path('Premier_League_Stats.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath)


# TSPGGT = 0
# print(df.head())
# print(len(df))

# for i in range(0,len(df)):
#     if df['TotalShotsPerGame'][i]>20:
#         #print(df['TotalShotsPerGame'][i])
#         TSPGGT+=1
# print(TSPGGT)
