import requests

url = 'http://18.140.7.137/Pervasive_php_api/api/user/read.php'
print (url)

x = requests.get(url)
data = x.json()

username = "kevin"
if (data['message'] == "No Users Found") or not any(uName['username'] == username for uName in data) or (data['message'] == 'No Users Found'):
    print ("ga ada")
else :
    print ("ada")