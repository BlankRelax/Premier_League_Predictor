import pandas as pd
from pathlib import Path

df = pd.read_csv('Performance_Data_Football_Teams.csv')
Leagues = ['Premier League']
df = df[df['League'].isin(Leagues)]
print(len(df))
filepath = Path('Premier_League_Stats.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath)






