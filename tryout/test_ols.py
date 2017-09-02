'''
Created on 2017年8月3日

@author: I314070
'''
impimport trynumpy as npmport statsmodels.api as sm
import matplotlib.pyplot as plt

nsample = 100
x=np.linspace(0,10,nsample)
x=sm.add_constant(x)
beta = np.array([1,10])
e=np.random.normal(size=nsample)
z = np.dot(x,beta)
y= z + e

model = sm.OLS(y,x)
results = model.fit()
'''
print( y)
print(results.params)
print(results.summary())
'''


