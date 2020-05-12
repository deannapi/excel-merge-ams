import pandas as pd
import numpy as np

# Production Data
prod = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/04 April/Production April 2020.xlsx')
# make all text Uppercase
prod['Wellname'] = prod['Wellname'].str.upper()
prod['Route (2)'] = prod['Route (2)'].str.upper()
prod['FOREMAN'] = prod['FOREMAN'].str.upper()
prod['CurrentStatus'] = prod['CurrentStatus'].str.upper()
prod.head()
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
cont_tx.dtypes
prod.dtypes

# Merge Data into AMS Sheets
# cont_tx = pd.merge(left=cont_tx, right=prod, left_on='API', right_on='API', how='left')
# show column names

cont_tx = pd.merge(cont_tx, prod, on='API')[['Route Number_y', 'BOPD_y', 'MCFD_y', 'BWPD_y']].rename(columns={'Route Number_y':'Route Number', 'BOPD_y':'BOPD', 'MCFD_y':'MCFD', 'BWPD_y':'BWPD'})
for col in cont_tx.columns: print(col)
cont_tx.head(10)

# cont_tx = prod[cont_tx['API'].isin(prod['API'])]