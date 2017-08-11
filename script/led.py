import webiopi
webiopi.setDebug()
GPIO = webiopi.GPIO

LED1PIN = 23
def setup():
	GPIO.setFunction(LED1PIN, GPIO.OUT)

@webiopi.macro
def up():
	GPIO.output(LED1PIN,True)
	webiopi.sleep(5)
	GPIO.output(LED1PIN,False)