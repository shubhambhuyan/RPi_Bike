# Imports
import webiopi
import time
import subprocess

# Enable debug output
webiopi.setDebug()

# Retrieve GPIO lib
GPIO = webiopi.GPIO

# Left motor GPIOs
L1=4  # H-Bridge 1
L2=17 # H-Bridge 2
#LS=25 # H-Bridge 1,2EN
servo = 18
# Called by WebIOPi at script loading
def setup():
    webiopi.debug("Script with macros - Setup")
    # Setup GPIOs
    GPIO.setFunction(L1, GPIO.OUT)
    GPIO.setFunction(L2, GPIO.OUT)
    GPIO.setFunction(servo, GPIO.PWM)
    #GPIO.pwmWrite(LED0, 0.5)        # set to 50% ratio
    #GPIO.pwmWriteAngle(SERVO, 0)    # set to 0 (neutral)
def loop():
    # Toggle LED each 5 seconds
    #value = not GPIO.digitalRead(LED1)
    #GPIO.digitalWrite(LED1, value)
    webiopi.sleep(1)

# Called by WebIOPi at server shutdown
def destroy():
    #webiopi.debug("Script with macros - Destroy")
    # Reset GPIO functions
    GPIO.setFunction(L1, GPIO.IN)
    GPIO.setFunction(L2, GPIO.IN)
    GPIO.setFunction(servo, GPIO.IN)
