'''
Created on 2017年4月27日

@author: I314070
'''

str = "pageit('111');"
a = str.find("('")
b=str.find("')")

print(a)
print(b)
print(str[a+2:b])
r = range(1,6)
