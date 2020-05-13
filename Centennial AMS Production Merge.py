import pandas as pd
import numpy as np

# Production Data
prod = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/04 April/Production April 2020.xlsx')
# make all text Uppercase
prod['Wellname'] = prod['Wellname'].str.upper()
prod['Route (2)'] = prod['Route (2)'].str.upper()
prod['FOREMAN'] = prod['FOREMAN'].str.upper()
prod['CurrentStatus'] = prod['CurrentStatus'].str.upper()
# Export Production 
# prod.to_excel(r'C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/04 April/Production April 2020.xlsx')

# Empty AMS
cont_tx = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/04 April/AMS Report April 2020.xlsx', sheet_name='Continuous TX', header=3)
cont_nm = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/04 April/AMS Report April 2020.xlsx', sheet_name='Continuous NM', header=3)
h2s_tx = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/04 April/AMS Report April 2020.xlsx', sheet_name='H2S TX', header=3)
h2s_nm = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/04 April/AMS Report April 2020.xlsx', sheet_name='H2S NM', header=3)
meth_tx = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/04 April/AMS Report April 2020.xlsx', sheet_name='Methanol TX', header=3)
meth_nm = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/04 April/AMS Report April 2020.xlsx', sheet_name='Methanol NM', header=3)
spec_tx = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/04 April/AMS Report April 2020.xlsx', sheet_name='Special Treatments TX', header=3)
spec_nm = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/04 April/AMS Report April 2020.xlsx', sheet_name='Special Treatments NM', header=3)
batch_tx = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/04 April/AMS Report April 2020.xlsx', sheet_name='Batch TX', header=3)
batch_nm = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/04 April/AMS Report April 2020.xlsx', sheet_name='Batch NM', header=3)

# Change column name in AMS to 'API'
cont_tx.rename(columns={'Property Number': 'API'}, inplace=True)
cont_nm.rename(columns={'Property Number': 'API'}, inplace=True)
h2s_tx.rename(columns={'Property Number': 'API'}, inplace=True)
h2s_nm.rename(columns={'Property Number': 'API'}, inplace=True)
meth_tx.rename(columns={'Property Number': 'API'}, inplace=True)
meth_nm.rename(columns={'Property Number': 'API'}, inplace=True)

#Change column names in Production
prod.rename(columns={'Route (2)' : 'Route Number',
                     'AvgBOPD' : 'BOPD',
                     'AvgMCFPD' : 'MCFD',
                     'AvgBWPD' : 'BWPD'},
                     inplace=True)

# Change DataTypes of API
cont_tx['API'] = cont_tx['API'].fillna(0).astype(np.int64)
cont_nm['API'] = cont_nm['API'].fillna(0).astype(np.int64)
h2s_tx['API'] = h2s_tx['API'].fillna(0).astype(np.int64)
h2s_nm['API'] = h2s_nm['API'].fillna(0).astype(np.int64)
meth_tx['API'] = meth_tx['API'].fillna(0).astype(np.int64)
meth_nm['API'] = meth_nm['API'].fillna(0).astype(np.int64)
prod['API'] = prod['API'].astype(np.int64)

# Merge Data into AMS Sheets
############## CONTINUOUS TEXAS #############

# this merge method keeps all columns - too much crap
cont_tx = pd.merge(left=cont_tx, right=prod, left_on='API', right_on='API', how='left')
# show column names
for col in cont_tx.columns: print(col)
cont_tx.head(10)
# remove extra columns and join needed columns
cont_tx['MCFD_x'] = cont_tx['MCFD_y']
cont_tx['BOPD_x'] = cont_tx['BOPD_y']
cont_tx['BWPD_x'] = cont_tx['BWPD_y']
cont_tx.rename(columns={
    'MCFD_x' : 'MCFD',
    'BOPD_x' : 'BOPD',
    'BWPD_x' : 'BWPD'
}, inplace=True)

cont_tx.drop(columns=[
    'Wellname', 'Route Number_y', 'State', 'Area', 'FOREMAN', 'CurrentStatus', 'SurfaceLatitude',
    'SurfaceLongitude', 'Last(MOP)', 'MonthOil', 'MonthWater', 'MonthGas', 'AvgCasPress',
    'AvgTbgPress', 'AvgPIP', 'HoursDown', 'DaysOn', '#DaysInMonth', 'BOPD_y', 'MCFD_y',
    'BWPD_y', 'AvgH2S', 'Unnamed: 23', 'Unnamed: 24', 'Unnamed: 25', 'Unnamed: 26'
], inplace=True)

cont_tx.head(10)

# Merge but only keep necessary columns
# cont_tx_new = pd.merge(left=cont_tx, right=prod, on='API')[['Route Number_y', 'Lease/Location Name', 'API', 'MCFD_y', 'BOPD_y', 'BWPD_y']].rename(columns={'Route Number_y':'Route Number', 'MCFD_y':'MCFD', 'BOPD_y':'BOPD', 'BWPD_y':'BWPD'})
# cont_tx_new.head(10)

# Get Production Data for joined wells

chknight = cont_tx.loc[cont_tx['Lease/Location Name'] == 'C.H. KNIGHT 2&3H WATERLINE']
chknight2 = prod.loc[prod['Wellname'] == 'C.H. KNIGHT 2H']
chknight3 = prod.loc[prod['Wellname'] == 'C.H. KNIGHT 3H']
chknight_prod = chknight2.sum() + chknight3.sum()
chknight['BOPD'] = chknight_prod['BOPD']
chknight['MCFD'] = chknight_prod['MCFD']
chknight['BWPD'] = chknight_prod['BWPD']
chknight

carpenter = cont_tx.loc[cont_tx['Lease/Location Name'] == 'CARPENTER 9, 16, 23']
carpenter9 = prod.loc[prod['Wellname'] ==  'CARPENTER STATE C U09H']
carpenter16= prod.loc[prod['Wellname'] ==  'CARPENTER STATE D U16H']
carpenter23 = prod.loc[prod['Wellname'] ==  'CARPENTER STATE E U23H']
carpenter_prod = carpenter9.sum() + carpenter16.sum() + carpenter23.sum()
carpenter['BOPD'] = carpenter_prod['BOPD']
carpenter['MCFD'] = carpenter_prod['MCFD']
carpenter['BWPD'] = carpenter_prod['BWPD']
carpenter

layden = cont_tx.loc[cont_tx['Lease/Location Name'] == 'LAYDEN WATERLINE']
redrock = cont_tx.loc[cont_tx['Lease/Location Name'] == 'RED ROCK WATERLINE']
redrock04 = prod.loc[prod['Wellname'] == 'RED ROCK A UNIT U04H']
redrock13 = prod.loc[prod['Wellname'] == 'RED ROCK A UNIT U13H']
redrock09 = prod.loc[prod['Wellname'] == 'RED ROCK B T09H']
redrock30 = prod.loc[prod['Wellname'] == 'RED ROCK M U30H']
redrock34 = prod.loc[prod['Wellname'] == 'RED ROCK N T34H']
sieber05 = prod.loc[prod['Wellname'] ==  'SIEBER TRUST B05H']
sieber13 = prod.loc[prod['Wellname'] ==  'SIEBER TRUST B13H']
sieber21 = prod.loc[prod['Wellname'] ==  'SIEBER TRUST B21H']
sieber09 = prod.loc[prod['Wellname'] ==  'SIEBER TRUST C09H']
sieber17 = prod.loc[prod['Wellname'] ==  'SIEBER TRUST C17H']
sieber13 = prod.loc[prod['Wellname'] ==  'SIEBER TRUST U13H']
layden_prod = redrock04.sum() + redrock09.sum() + redrock13.sum() + redrock30.sum() + redrock34.sum() + sieber05.sum() + sieber09.sum() + sieber13.sum() + sieber17.sum() + sieber21.sum()
redrock_prod = redrock04.sum() + redrock09.sum() + redrock13.sum() + redrock30.sum() + redrock34.sum() + sieber05.sum() + sieber09.sum() + sieber13.sum() + sieber17.sum() + sieber21.sum()
layden['BOPD'] = layden_prod['BOPD']
layden['BWPD'] = layden_prod['BWPD']
layden['MCFD'] = layden_prod['MCFD']
redrock['BOPD'] = redrock_prod['BOPD']
redrock['BWPD'] = redrock_prod['BWPD']
redrock['MCFD'] = redrock_prod['MCFD']
layden
redrock

oatman3_4 = cont_tx.loc[cont_tx['Lease/Location Name'] == 'OATMAN C19-4A 3&4H']
oatman3 = prod.loc[prod['Wellname'] == 'OATMAN C19-4A 3H']
oatman4 = prod.loc[prod['Wellname'] == 'OATMAN C19-4A 4H']
oatman3_4_prod = oatman3.sum() + oatman4.sum()
oatman3_4['BOPD'] = oatman3_4_prod['BOPD']
oatman3_4['MCFD'] = oatman3_4_prod['MCFD']
oatman3_4['BWPD'] = oatman3_4_prod['BWPD'] 
oatman3_4

peregrine = cont_tx.loc[cont_tx['Lease/Location Name'] == 'PEREGRINE BTY']
peregrine1 = prod.loc[prod['Wellname'] == 'PEREGRINE 27 1']
peregrine2 = prod.loc[prod['Wellname'] == 'PEREGRINE 27 2']
peregrine3 = prod.loc[prod['Wellname'] == 'PEREGRINE 27 3']
peregrine4 = prod.loc[prod['Wellname'] == 'PEREGRINE 27 4']
peregrine5 = prod.loc[prod['Wellname'] == 'PEREGRINE 27 5H']
peregrine6 = prod.loc[prod['Wellname'] == 'PEREGRINE 27 6H']
peregrine7 = prod.loc[prod['Wellname'] == 'PEREGRINE 27 7H']
peregrine8 = prod.loc[prod['Wellname'] == 'PEREGRINE 27 8H']
peregrine9 = prod.loc[prod['Wellname'] == 'PEREGRINE 27 9H']
peregrine_prod = peregrine1.sum() + peregrine2.sum() + peregrine3.sum() + peregrine4.sum() + peregrine5.sum() + peregrine6.sum() + peregrine7.sum() + peregrine8.sum() + peregrine9.sum()
peregrine['BOPD'] = peregrine_prod['BOPD']
peregrine['MCFD'] = peregrine_prod['MCFD']
peregrine['BWPD'] = peregrine_prod['BWPD']
peregrine

predatorW = cont_tx.loc[cont_tx['Lease/Location Name'] == 'PREDATOR WEST WATERLINE']
predW04 = prod.loc[prod['Wellname'] ==  'PREDATOR WEST U04H']
predW18 = prod.loc[prod['Wellname'] ==  'PREDATOR WEST U18H']
predator_prod = predW04.sum() + predW18.sum()
predator_prod
predatorW['BOPD'] = predator_prod['BOPD']
predatorW['MCFD'] = predator_prod['MCFD']
predatorW['BWPD'] = predator_prod['BWPD']
predatorW

# Add 'joined wells' into cont_tx_new


# Export Final AMS's