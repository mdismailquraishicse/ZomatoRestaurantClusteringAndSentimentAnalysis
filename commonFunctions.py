# showInfo function diplays shape, # of duplicated, # of unique values, # of nan values, info of the dataframe.
import string
import nltk
from nltk.stem.snowball import SnowballStemmer

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
# This function takse a string and return in lower case
def lower_casing(string_):
    ''' input a string and return in lowercase '''
    if len(string_.split())==1:
        return string_
    string_ = [s.lower() for s in string_.split()]
    return ' '.join(string_)
# This function takes a string and removes numeric values
def remove_numeric(string_):
    ''' input a string and returns a string without numeric '''
    text = []
    if len(string_.split())==1:
        if string_.isnumeric()==False:
            return string_
    # for s in string_.split():
    #     if s.isnumeric() == False:
    #         text.append(s)
    text = [s for s in string_.split() if s.isnumeric()==False]
    return ' '.join(text)
# This function takes a string and removes punctuations
def remove_punctuations(string_):
    text = [s for s in string_ if s not in string.punctuation]
    return ''.join(text)
# Stemming
def stemming(string_):
    stemmer = SnowballStemmer(language='english')
    stemmed_text = [stemmer.stem(s) for s in string_.split()]
    return ' '.join(stemmed_text)