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


print(df[passing_attributes])