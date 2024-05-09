# showInfo function diplays shape, # of duplicated, # of unique values, # of nan values, info of the dataframe.
def showInfo(df):
    ''' input a dataframe '''
    print('shape : ', df.shape)
    print()
    print('# of duplicated rows : ', df.duplicated().sum())
    print()
    print('# of unique values in each column : ')
    print(df.nunique())
    print()
    print('# of missing/nan values in each column : ')
    print(df.isna().sum())
    print()
    print('Calling info method : ')
    print(df.info())