import requests

url = 'http://18.140.7.137/Pervasive_php_api/api/setting/update.php'
print (url)
headers = {'Content-type': 'application/Json'}
myobj = """{
    "id":"1",
    "brightness":"128",
    "switch":"1"
}"""

x = requests.post(url, headers=headers, data = myobj)
data = x.json()
print(data)