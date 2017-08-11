import webiopi
import os
webiopi.setDebug()
GPIO = webiopi.GPIO

sleeptime = 0.05

IN_A = 23
IN_B = 24
LED_RED = 25
ir_rx = 17

#GPIOの設定
def setup():
	GPIO.setFunction(ir_rx, GPIO.IN)
	GPIO.setFunction(IN_A, GPIO.OUT)
	GPIO.setFunction(IN_B, GPIO.OUT)
	GPIO.setFunction(LED_RED, GPIO.OUT)
	GPIO.output(LED_RED,True)

@webiopi.macro
def run():
#実行ファイルの作成マクロ
	#100 round trips
	for looptimes in range(0,10,1):
		GPIO.output(LED_RED,False)
		for x in range(0,4,1):
			GPIO.output(IN_A,True)
			GPIO.output(IN_B,True)
			webiopi.sleep(sleeptime)
			
			GPIO.output(IN_A,False)
			GPIO.output(IN_B,True)
			webiopi.sleep(sleeptime)
			
			GPIO.output(IN_A,False)
			GPIO.output(IN_B,False)
			webiopi.sleep(sleeptime)
			
			GPIO.output(IN_A,True)
			GPIO.output(IN_B,False)
			webiopi.sleep(sleeptime)
			
		webiopi.sleep(1)

		for x in range(0,4,1):
			GPIO.output(IN_A,True)
			GPIO.output(IN_B,False)
			webiopi.sleep(sleeptime)
			
			GPIO.output(IN_A,False)
			GPIO.output(IN_B,False)
			webiopi.sleep(sleeptime)
			
			GPIO.output(IN_A,False)
			GPIO.output(IN_B,True)
			webiopi.sleep(sleeptime)
			
			GPIO.output(IN_A,True)
			GPIO.output(IN_B,True)
			webiopi.sleep(sleeptime)
			
		webiopi.sleep(1)
	GPIO.output(LED_RED,True)

@webiopi.macro
def stop():
	GPIO.output(LED_RED,True)

@webiopi.macro
def up():
	#CW
	for x in range(0,2,1):
		GPIO.output(IN_A,True)
		GPIO.output(IN_B,True)
		webiopi.sleep(sleeptime)
		
		GPIO.output(IN_A,False)
		GPIO.output(IN_B,True)
		webiopi.sleep(sleeptime)
		
		GPIO.output(IN_A,False)
		GPIO.output(IN_B,False)
		webiopi.sleep(sleeptime)
		
		GPIO.output(IN_A,True)
		GPIO.output(IN_B,False)
		webiopi.sleep(sleeptime)

@webiopi.macro
def down():
	#CCW
	for x in range(0,2,1):
		GPIO.output(IN_A,True)
		GPIO.output(IN_B,False)
		webiopi.sleep(sleeptime)
		
		GPIO.output(IN_A,False)
		GPIO.output(IN_B,False)
		webiopi.sleep(sleeptime)
		
		GPIO.output(IN_A,False)
		GPIO.output(IN_B,True)
		webiopi.sleep(sleeptime)
		
		GPIO.output(IN_A,True)
		GPIO.output(IN_B,True)
		webiopi.sleep(sleeptime)