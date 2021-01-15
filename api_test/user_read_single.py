import requests

username = 'marcell'
url = 'http://18.140.7.137/Pervasive_php_api/api/user/read_single.php?username=' + username
print (url)

x = requests.get(url)
data = x.json()
print(data['id'])
# print(x.json()['password'])