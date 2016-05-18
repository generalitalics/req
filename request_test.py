# req
# Python34

import requests

city = str(input('Name? '))
print(city)
url = 'http://httpbin.org/get'
'''
param = { "q":city,
          "appid":"11c0d3dc6093f7442898ee49d2430d20",
          "units":"metric"
}
'''
req = requests.get(url)
data = req.json()
print(req.headers['content-type'])

template = 'Test template Name>>{a}<< and >>{b}<<'
print(template.format(b=city, a=data['headers']['Host']))
