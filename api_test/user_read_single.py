import requests

username = 'kevin'
url = 'http://18.140.7.137/Pervasive_php_api/api/user/read_single.php?username=' + username
print (url)


user_id = requests.get(url).json()
x = requests.get(url)
data = x.json()
print(user_id)
# print(x.json()['password'])