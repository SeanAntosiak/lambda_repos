import pandas as pd
import numpy as np


class dataframe:

    def __init__(self, df):
        self.df = df

    def nullDF(self):
        dfnull = pd.DataFrame(self.df.isnull().sum()).reset_index()
        dfnull.columns = ['features', 'NullCount']
        dfnull = dfnull[dfnull['NullCount'] != 0].reset_index(drop=True)
        return(dfnull)

    def addListAsCol(self, theList, name):
        df = self.df
        nansNum = len(df) - len(theList)
        nans = np.full(nansNum, np.NaN)
        newCol = np.append(theList, nans)
        df[name] = newCol
        return(df)
