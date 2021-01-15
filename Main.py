import requests

id = 'michael'
url = 'http://localhost/Pervasive_php_api/api/user/read_single.php?username=' + id
print (url)
# headers = {'Content-type': 'application/Json'}
myobj = """{
    "id":"5"
}"""

# x = requests.get(url, headers=headers, data = myobj)
x = requests.get(url)
data = x.json()
print(data['id'])