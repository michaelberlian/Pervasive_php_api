import requests

id = '1'
url = 'http://18.140.7.137/Pervasive_php_api/api/setting/read_single.php?id=' + id
print (url)

x = requests.get(url)
data = x.json()

if int(data['switch']):
    print ('int')
print(data['switch'])