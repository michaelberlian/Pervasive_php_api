import requests

url = 'http://18.140.7.137/Pervasive_php_api/api/user/create.php'
print (url)
headers = {'Content-type': 'application/Json'}
myobj = """{
    "username":"michael",
    "password":"michael123"
}"""

x = requests.get(url, headers=headers, data = myobj)
data = x.json()
print(data)