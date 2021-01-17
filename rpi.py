import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import asyncio
from pywizlight.bulb import wizlight, PilotBuilder, discovery
import requests

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

#button GPIO
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#MC-38 GPIO
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    #  landing page login
    print ("""
Sign in / Sign up:
    1. Sign in 
    2. Sign up
    3. Change password
    4. Delete account
    5. exit    
input:
    """)
    getInput = int(input())
    # sign in
    if (getInput == 1):
        #get input
        username = input("username: ")
        password = input("password: ")

        #compare to db
        url = 'http://18.140.7.137/Pervasive_php_api/api/user/read_single.php?username=' + username
        password_real = requests.get(url).json()['password']

        #verified
        if (password == password_real):
            user_id = requests.get(url).json()['id']
            print ('your id is ', user_id)

            #get settings
            url = 'http://18.140.7.137/Pervasive_php_api/api/setting/read_single.php?id=' + user_id
            data = requests.get(url).json()
            brightness = data['brightness']
            switch = data['switch']

            break
        else :
            print("wrong password")
    # sign up
    elif (getInput == 2):

        #get input
        username = input("username: ")

        #check if username has been used
        url = 'http://18.140.7.137/Pervasive_php_api/api/user/read.php'
        data = requests.get(url).json()

        #username is not used
        if not(isinstance(data,list)) or not any(uName['username'] == username for uName in data):
            password = input("password: ")

            #create the new user
            url = 'http://18.140.7.137/Pervasive_php_api/api/user/create.php'
            headers = {'Content-type': 'application/Json'}
            myobj = """{{
                            "username":"{}",
                            "password":"{}"
                        }}""".format(username,password)
            userCreateRequests = requests.get(url, headers=headers, data = myobj)

            print(userCreateRequests.json()['message'])

            url = 'http://18.140.7.137/Pervasive_php_api/api/user/read_single.php?username=' + username
            user_id = requests.get(url).json()['id']

            print ('your id is ', user_id)

            #create the setting for new user
            url = 'http://18.140.7.137/Pervasive_php_api/api/setting/create.php'
            headers = {'Content-type': 'application/Json'}
            myobj = """{{
                "brightness":"255",
                "switch":"1"
            }}""".format(user_id)
            data = requests.get(url, headers=headers, data = myobj).json()
            print (data['message'])

            break
        #username used
        else :
            print ("username has been used")
    #change password
    elif (getInput == 3):
        #get input
        username = input("username: ")
        password = input("password: ")

        #compare to db
        url = 'http://18.140.7.137/Pervasive_php_api/api/user/read_single.php?username=' + username
        password_real = requests.get(url).json()['password']

        #verification true
        if (password == password_real):
            user_id = requests.get(url).json()['id']

            #setup the update
            new_password = input("new password: ")
            url = 'http://18.140.7.137/Pervasive_php_api/api/user/update.php'
            headers = {'Content-type': 'application/Json'}
            myobj = """{{
                "id":"{}",
                "username":"{}",
                "password":"{}"
            }}""".format(user_id, username, new_password)
            x = requests.post(url, headers=headers, data = myobj)
            data = x.json()
            print (data['message'])
            break
        else :
            print ("verification failed")

    #delete accound
    elif (getInput == 4):
        #get input
        username = input("username: ")
        password = input("password: ")

        #compare to db
        url = 'http://18.140.7.137/Pervasive_php_api/api/user/read_single.php?username=' + username
        password_real = requests.get(url).json()['password']

        #verification true
        if (password == password_real):
            user_id = requests.get(url).json()['id']

            #delete the user
            url = 'http://18.140.7.137/Pervasive_php_api/api/user/delete.php'
            headers = {'Content-type': 'application/Json'}
            myobj = """{{
                "id":"{}"
            }}""".format(user_id)
            data = requests.post(url, headers=headers, data = myobj).json()
            print (data['message'])

            #delete setting
            url = 'http://18.140.7.137/Pervasive_php_api/api/setting/delete.php'
            headers = {'Content-type': 'application/Json'}
            myobj = """{{
                "id":"{}"
            }}""".format(user_id)
            data = requests.post(url, headers=headers, data = myobj).json()
            print (data['message'])

            break
        else :
            print ("verification failed")
    #exit
    elif (getInput == 5):
        exit()



url = 'http://18.140.7.137/Pervasive_php_api/api/setting/read_single.php?id=' + user_id
data = requests.get().json()
brightness = int(data['brightness'])
switch = int(data['switch'])

#get settings
print ("""current Setting :
Brightness: {}
switch: {}
""".format(brightness,switch))

#Smart Lights local IP address
light = wizlight("192.168.100.10")
light2 = wizlight("192.168.100.11")

lamp_state = False
turn = False

def button1_callback(channel):
    global brightness
    global lamp_state
    global light
    global light2

    if brightness == 1 :
        brightness = 128
    elif brightness == 128 :
        brightness = 255
    else :
        brightness = 1

    #update settings
    url = 'http://18.140.7.137/Pervasive_php_api/api/setting/update.php'
    headers = {'Content-type': 'application/Json'}
    myobj = """{{
        "id":"{}",
        "brightness":"{}",
        "switch":"{}"
    }}""".format(user_id,brightness,switch)
    data = requests.post(url, headers=headers, data = myobj).json()
    print(data['message'])

    print('brightness = ', brightness)


def button2_callback(channel):
    global switch
    if (switch):
        switch = False
        print('switch = off')
    else :
        switch = True
        print('switch = on')

    #update settings
    url = 'http://18.140.7.137/Pervasive_php_api/api/setting/update.php'
    headers = {'Content-type': 'application/Json'}
    myobj = """{{
        "id":"{}",
        "brightness":"{}",
        "switch":"{}"
    }}""".format(user_id,brightness,switch)
    data = requests.post(url, headers=headers, data = myobj).json()
    print(data['message'])

def button3_callback(channel):
    global turn
    turn = True
    print("button 3 turn true")


#turn the lights on
async def turnOnLights(light, light2, brightness_input):
    #brightness
    await light.turn_on(PilotBuilder(brightness = brightness_input))
    await light2.turn_on(PilotBuilder(brightness = brightness_input))
    
async def turnOffLights(light,light2):
    await light.turn_off()
    await light2.turn_off()
    
#turn the lights off
async def main():

    global brightness
    global lamp_state
    global function_state
    global turn

    prev_state = False

    while True:
        #for the third button
        if turn:
            if (lamp_state):
                print("turned off/turn")
                lamp_state = False
                await turnOffLights(light, light2)
            else :
                print("turned on/turn")
                lamp_state = True
                await turnOnLights(light, light2, brightness)
            turn = False

        #for the magnet sensor
        if (prev_state != GPIO.input(7) and GPIO.input(7) == True and switch == True):
            print("door opened")
            if (lamp_state):
                print("turned off")
                lamp_state = False
                await turnOffLights(light, light2)
            else :
                print("turned on")
                lamp_state = True
                await turnOnLights(light, light2, brightness)
            print("action done")
        prev_state = GPIO.input(7)
            
    GPIO.cleanup()
    
    
GPIO.add_event_detect(8,GPIO.RISING,callback=button1_callback)   
GPIO.add_event_detect(10,GPIO.RISING,callback=button2_callback)
GPIO.add_event_detect(12,GPIO.RISING,callback=button3_callback)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
