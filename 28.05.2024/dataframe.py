# dataframe is two dimentional which is in a tabular format.

import pandas as pd

#dataframe with a dictionary

data = {
    'Name': ['kingini', 'tuttu', 'ikka'],
    'Age' : [24,23,24],
    'place' : ['koovode', 'mavoor', 'punuoor']
}

# convert the data  into dataframe

df = pd.DataFrame(data)
# print (df)

# print name
# print (df['Name'])

# print name and place 
# print (df[['Name','place']])

# accessing each row rom the dataframe we need to use the inbuild function in pandas
# print (df.iloc[2])

#print (df [df['Age']>23])

# add a new column into the dataset
df['stipend'] = [15000,5000,5000]
#print(df)


# remove a column
df = df.drop(columns=['stipend'])
#print (df)

# statical function
# describe () help get the summary of statics of your dataframe
print(df.describe())


