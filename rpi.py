import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import asyncio
from pywizlight.bulb import wizlight, PilotBuilder, discovery

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

#button GPIO
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#MC-38 GPIO
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Smart Lights local IP address
light = wizlight("192.168.100.10")
light2 = wizlight("192.168.100.11")

brightness = 255
lamp_state = False
function_state = True
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

    print('brightness = ', brightness)


def button2_callback(channel):
    global function_state
    if (function_state):
        function_state = False
        print('function = off')
    else :
        function_state = True
        print('function = on')

def button3_callback(channel):
    global turn
    turn = True
    print("button 3 turn true")


#set button state
button_state = False
async def turnOnLights(light, light2, brightness_input):
    #mode
#    await light.turn_on(PilotBuilder(rgb = color))
#    await light2.turn_on(PilotBuilder(rgb = color))
    
    #brightness
    await light.turn_on(PilotBuilder(brightness = brightness_input))
    await light2.turn_on(PilotBuilder(brightness = brightness_input))
    
async def turnOffLights(light,light2):
    await light.turn_off()
    await light2.turn_off()
    
async def main():
    #global button_state
    #while True:# Run forever
        #if GPIO.input(10) == GPIO.HIGH:
           # print("Button was pushed!")
          #  if button_state == False:
         #       print("ON")
        #        button_state = True
       #         await light.turn_on(PilotBuilder(cold_white = (200)))
      #          await light2.turn_on(PilotBuilder(cold_white = (200)))
     #       else:
    #            button_state = False
   #             print("OFF")
  #              await light.turn_off()
 #               await light2.turn_off()
#            print("Action done")
    global brightness
    global lamp_state
    global function_state
    global turn
    prev_state = False
    while True:
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

        if (prev_state != GPIO.input(7) and GPIO.input(7) == True and function_state == True):
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