import requests

'''
Created on 2017年4月25日

@author: I314070
'''
'''
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

r = requests.post('http://httpbin.org/post', data={'key':'value'} ,params=payload)
print(r.status_code == requests.codes.get('ok') )

jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
#print(jar)
url = 'http://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
print(r.text[-1:1])



import json
dict_ = {1:2, 3:4, "55":"66"}  
  
# test json.dumps  
print (type(dict_), dict_  )
json_str = json.dumps(dict_)  
print ("json.dumps(dict) return:" ) 
print( type(json_str), json_str  )
  
# test json.loads  
print ("\njson.loads(str) return" ) 
dict_2 = json.loads(json_str)  
print (type(dict_2), dict_2 ) 

'''
sequence = [(12, 34),(11,12)]
for x,y in sequence:
    print(x,y)