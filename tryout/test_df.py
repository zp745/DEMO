'''
Created on 2017年8月2日

@author: I314070
'''
from pandas.core.series import Series
impimport trynumpy as nprom pandas.core.frame import DataFrame
import statsmodels.api as sm



if __name__ == '__main__':
    obj = Series([4,7,-5,3])
    frame = DataFrame(np.arange(9).reshape(3,3),index = ['a','c','d'],columns=['Ohio','Texas','California'])
    
    print(sm.add_constant(frame['Ohio'].values))
#    frame.ix[(frame['Ohio']>2),'CHECK'] = 1
#    print(frame.ix[(frame['Ohio']>2)])

    
#    obj=Series(np.arange(2,6),index = ['a','b','c','d'])
    