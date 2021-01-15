import requests

url = 'http://18.140.7.137/Pervasive_php_api/api/user/update.php'
print (url)
headers = {'Content-type': 'application/Json'}
user_id = '1'
username = 'kevin'
new_password = "678"
myobj = """{{
    "id":"{}",
    "username":"{}",
    "password":"{}"
}}""".format(user_id, username, new_password)

x = requests.post(url, headers=headers, data = myobj)
data = x.json()
print(data)