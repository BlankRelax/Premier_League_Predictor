import pandas as pd

df = pd.read_csv('Performance_Data_Football_Teams.csv')

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


df = df[all_key_attributes]
TSPGGT = 0
for i in range(0,len(df)):
    if df['TotalShotsPerGame'][i]>20:
        #print(df['TotalShotsPerGame'][i])
        TSPGGT+=1
print(TSPGGT)
