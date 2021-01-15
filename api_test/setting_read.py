import requests

url = 'http://18.140.7.137/Pervasive_php_api/api/setting/read.php'
print (url)

x = requests.get(url)
data = x.json()
print(data)