import requests

url = 'http://18.140.7.137/Pervasive_php_api/api/user/read.php'
print (url)

x = requests.get(url)
data = x.json()
print(data)

username = "kevin"
if not any(uName['username'] == username for uName in data):
    print ("ga ada")
else :
    print ("ada")