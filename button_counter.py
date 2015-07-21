import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) #set gpio by board mode
GPIO.setup(12, GPIO.IN) #set pin 12 as input
time_pressed = 0
counter = 0

def clear_counter(): #function to clear counter if button pressed for 3 seconds
    global counter
    if time_pressed > 15:
        counter = 0
        print "Clearing counter" 
        return counter
    else:
        return counter
    
while True: #loop to keep reading input
    input_value=GPIO.input(12)#set variable with input value, FALSE = pressed
    if input_value==False:
        counter +=1
        time_pressed = 0
        while input_value== False: #loop to keep reading input to count how long the button is pressed
            
            time_pressed= time_pressed+1
            input_value=GPIO.input(12)
            time.sleep(0.05) #set time loop is repeated 
            counter = clear_counter() #run fun. clear_counter
    elif input_value==True: #run if button NOT pressed
        
        print "counter =", counter #print how many times button was pressed
        while input_value== True: #loop to keep reading input if button not pressed 
            input_value=GPIO.input(12)
GPIO.cleanup()    #clear GPIO


