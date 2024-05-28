import pandas as pd

#read csv file into dataframe
df = pd.read_csv('data.csv')
#print(df)

# clean the row without emplty data
df_cleaned_row = df.dropna(how="all")
#print (df_cleaned_row)

df_cleaned_row = df_cleaned_row.dropna(axis=1, how="all")
#print(df_cleaned_row)


df_filled_data = df.fillna(0)
print(df_filled_data)