curr_state = False
state_change = False
while True:
    global curr_state
    global state_change
    if (GPIO.input(buttonpin) == False):
        if (curr_state == False):
            curr_state = True
        else :
            curr_state = False
        state_change = True
        time.sleep(0.5)
    
    if (state_change):
        if (curr_state):
            await light.turn_on(PilotBuilder(rgb = 255,0,255))
            await light.turn_on(PilotBuilder(rgb = 255,0,255))
        else :
            await light.turn_off()
            await light.turn_off()
        state_change = False


Import RPi.GPIO as GPIO
From time import sleep                  #LED
State = 0
While True:
	Input = GPIO.input(13)
	If (input == False):                    #have to press button to work
		If (state == 1):             #this is on so led will start in off
			GPIO.output(22, True)
			State = 0
		elif (state == 0):            #led will start at this position which is off
			GPIO.output(22, False)
			
			State  = 1
		Sleep(1)