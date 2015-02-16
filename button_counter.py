import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
time_pressed = 0
counter = 0

def clear_counter():
    global counter
    if time_pressed > 15:
        counter = 0
        print "Clearing counter" 
        return counter
    else:
        return counter
    
while True:
    input_value=GPIO.input(12)
    if input_value==False:
        counter +=1
        time_pressed = 0
        while input_value== False:
            
            time_pressed= time_pressed+1
            input_value=GPIO.input(12)
            time.sleep(0.05)
            counter = clear_counter()
    elif input_value==True:
        
        print "counter =", counter
        while input_value== True:
            input_value=GPIO.input(12)
GPIO.cleanup()    


