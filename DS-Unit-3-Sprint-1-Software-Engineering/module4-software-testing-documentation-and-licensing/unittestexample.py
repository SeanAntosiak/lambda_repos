import numpy as np
import pandas as pd
import unittest


def addListAsCol(df, theList, name):
    '''
    takes a list and extends it to the length of a dataframe with null values
    then appends the list as a column with the given name
    if the list is longer than the dataframe this returns an error
    '''
    nansNum = len(df) - len(theList)
    nans = np.full(nansNum, np.NaN)
    newCol = np.append(theList, nans)
    df[name] = newCol
    return(df)


df = pd.DataFrame([1, 2, 3, 4], [6, 5, 3, 2]).reset_index()
df.columns = ['a', 'b']
mylist = [1, 2, 3]


class testlist(unittest.TestCase):

    def test1(self):
        dfnew = addListAsCol(df, mylist, 'test')
        self.assertEqual(dfnew['test'][2], 3)


if __name__ == '__main__':
    unittest.main()
