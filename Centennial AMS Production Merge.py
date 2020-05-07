import pandas as pd

# Production Data
prod = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/03 March/Centennial Production March 2020.xlsx')

# Empty AMS
cont_tx = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/03 March/AMS Report March 2020 - Empty.xlsx', sheet_name='Continuous TX', header=3)
cont_nm = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/03 March/AMS Report March 2020 - Empty.xlsx', sheet_name='Continuous NM', header=3)
h2s_tx = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/03 March/AMS Report March 2020 - Empty.xlsx', sheet_name='H2S TX', header=3)
h2s_nm = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/03 March/AMS Report March 2020 - Empty.xlsx', sheet_name='H2S NM', header=3)
meth_tx = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/03 March/AMS Report March 2020 - Empty.xlsx', sheet_name='Methanol TX', header=3)
meth_nm = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/03 March/AMS Report March 2020 - Empty.xlsx', sheet_name='Methanol NM', header=3)
spec_tx = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/03 March/AMS Report March 2020 - Empty.xlsx', sheet_name='Special Treatments TX', header=3)
spec_nm = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/03 March/AMS Report March 2020 - Empty.xlsx', sheet_name='Special Treatments NM', header=3)
batch_tx = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/03 March/AMS Report March 2020 - Empty.xlsx', sheet_name='Batch TX', header=3)
batch_nm = pd.read_excel('C:/Users/math_/OneDrive/Innospec/AMS/Centennial/2020/03 March/AMS Report March 2020 - Empty.xlsx', sheet_name='Batch NM', header=3)

# Print tab names
