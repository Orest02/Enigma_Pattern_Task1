import pandas as pd
import numpy as np

if __name__ == '__main__':
    #the dataset consists of 3 columns: name, surname and date. I will read the csv to the pandas dataframe and attempt to read the dates at the same time
    df = pd.read_csv('test.csv', parse_dates=[2]) #dates are at the 3rd column
    #let's see if the data read correctly
    print('This is the datatype layout of the dataframe:\n', df.dtypes)
    #let's also list first 5 rows of the dataframe
    print('\nFirst 5 rows:\n',df.head(5))
    #2. List a number of people born after 1999-12-31
    Num = len(df['data_urodzenia'].loc['1999-12-31':].index) #I could get the number also using .shape and .count(), however this method proves to be more time efficient, source: https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe
    print('\nThere are {} people born after 1999-12-31\n'.format(Num))
    #3. Print all unique female names (end with a)
    f_names = df['imie'].drop_duplicates() #choose unique names to the new series variable
    regex = '[a-zA-Z]*a$' #any number of alphabetic characters that end with a
    Filter = f_names.str.match(regex) #make true-false filter for the series
    print('\nThe unique female names are:\n',f_names.where(Filter).dropna().tolist()) #find the values, get rid of nans and print them as a list
