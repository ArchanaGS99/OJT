import pandas as pd

#read the csv file into the dataframe

df = pd.read_csv('data.csv',
                 dtype={'Age':int,'Salary':float},
                 usecols= ['Name','Age','place'])
print (df)