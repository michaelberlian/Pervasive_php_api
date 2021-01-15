import requests

url = 'http://18.140.7.137/Pervasive_php_api/api/setting/create.php'
print (url)
headers = {'Content-type': 'application/Json'}
myobj = """{
    "brightness":"255",
    "switch":"on"
}"""

x = requests.get(url, headers=headers, data = myobj)
data = x.json()
print(data)