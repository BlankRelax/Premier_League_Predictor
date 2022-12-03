import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Premier_League_Stats.csv')
all_key_attributes = ['Key','Team','League','Season','Rank','PassSuccess','ShortPassesPerGame',
                  'TotalShotsPerGame',
                  'CrossesPerGame','LongBallsPerGame', 'ThroughBallsPerGame',
                  'ShotsOnTargetPer90','ShotsOnTargetAgainstPer90','AerialDuelsWonPerGame',
                  'SuccessfulDribblesPerGame', 'OffsidesPerGame','InterceptionsPerGame',
                  'FoulsPerGame','FouledPerGame', 'TotalTacklesPerGame']

passing_attributes = ['Key','Team','League','Season','Rank','Possession','PassSuccess','ShortPassesPerGame',
                  'CrossesPerGame','LongBallsPerGame', 'ThroughBallsPerGame','TotalPassesPerGame',
                  'SuccessfulDribblesPerGame','TotalDribblesPerGame','TotalKeyPassesPerGame',
                  'LongKeyPassesPerGame','ShortKeyPassesPerGame']
Max_tot_shots = max(df['TotalShotsPerGame'])
Min_tot_shots = min(df['TotalShotsPerGame'])
print(Max_tot_shots)
print(Min_tot_shots)

avg_AerialDuelsWonPerGame_all_ranks = []
Ranks = range(1,21)
Rank1 = [1]
Rank1_df = df[df['Rank'].isin(Rank1)]
avg_AerialDuelsWonPerGame1 = np.mean(Rank1_df['AerialDuelsWonPerGame'])
print(avg_AerialDuelsWonPerGame1)

for i in range(1,21):
    Rank1 = [i]
    Rank1_df = df[df['Rank'].isin(Rank1)]
    avg_AerialDuelsWonPerGame1 = np.mean(Rank1_df['Possession'])
    avg_AerialDuelsWonPerGame_all_ranks.append(avg_AerialDuelsWonPerGame1)
print(avg_AerialDuelsWonPerGame_all_ranks)

plt.scatter(Ranks, avg_AerialDuelsWonPerGame_all_ranks)
plt.show()