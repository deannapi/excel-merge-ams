import pandas as pd

col_1 = ['Route', 'API', 'Owner']
data_1 = [['', '123456', ''],
          ['', '789123', ''],
          ['', '456789', ''],
          ['', '256709', '']
         ]
df1 = pd.DataFrame(data=data_1, columns=col_1)

col_2 = ['Name', 'Route', 'API', 'Owner']
data_2 = [['Hay', 'Route 12', '789123', 'Jon Doe'],
          ['Pirate', 'Route 03', '123456', 'Mary Smith'],
          ['Oat', 'Route 01', '256709', 'Jane Vick'],
          ['Pop', 'Route 04', '456789', 'Jack Roe']
         ]
df2 = pd.DataFrame(data=data_2, columns=col_2)

df2[df1['API'].isin(df2['API'])]
df2.head()