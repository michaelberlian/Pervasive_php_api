import requests

url = 'http://18.140.7.137/Pervasive_php_api/api/setting/delete.php'
print (url)
headers = {'Content-type': 'application/Json'}
myobj = """{
    "id":"6"
}"""

x = requests.post(url, headers=headers, data = myobj)
data = x.json()
print(data)