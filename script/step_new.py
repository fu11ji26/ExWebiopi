import webiopi
import os
webiopi.setDebug()
GPIO = webiopi.GPIO

#mbed1に送る信号（予定）
#mbedはプルアップモードで信号入力待ち状態にする（立下りを割り込む）
RUN = 17 #実行するかどうか True:する False:しない
ini_position = 4 #原点復帰用ピン True:する False:しない
FeedRatePin = 18 #送ったパルスの数だけ回転速度を決める
ENBL = 23 #True:常時励磁 False:無励磁
PLS = 24 #立ち上がりエッジで駆動（送ったパルスの数だけモータを回す）
DIR = 25 #True:CW False:CCW

#GPIOの設定
def setup():
	GPIO.setFunction(ir_rx, GPIO.IN)
	GPIO.setFunction(IN_A, GPIO.OUT)
	GPIO.setFunction(IN_B, GPIO.OUT)
	GPIO.setFunction(LED_RED, GPIO.OUT)
	GPIO.output(LED_RED,True)

#webiopi終了時に呼び出す関数
def destroy():
	GPIO.cleanup()

@webiopi.macro
def run():
#散水開始マクロ
#【重要】この中にループ関数を書かない（ブラウザで制御不能になる）
	GPIO.output(LED_RED,True)

@webiopi.macro
def stop():
#電磁弁とモータを止める信号を出すマクロ
#【重要】この中にループ関数を書かない(ブラウザで制御不能になる)
	GPIO.output(LED_RED,True)

@webiopi.macro
def onChangeAngle(angle):
	webiopi.debug("ChangeAngle : %s" % (angle))
	step_t = 0.01
	#ハーフステップ（0.9°）駆動
	if(angle==-10):
		GPIO.output(DIR,False)
		for n in range(1,10,1):
			GPIO.output(PLS,True)
			webiopi.sleep(0.01)
			GPIO.output(PLS,False)
			webiopi.sleep(0.01)
			
	elif(angle==-5):
		GPIO.output(DIR,False)
		for n in range(1,5,1):
			GPIO.output(PLS,True)
			webiopi.sleep(0.01)
			GPIO.output(PLS,False)
			webiopi.sleep(0.01)
	elif(angle==-1):
		GPIO.output(DIR,False)
		GPIO.output(PLS,True)
		webiopi.sleep(0.01)
		GPIO.output(PLS,False)
		
	elif(angle==0):
		GPIO.output(ini_position,True)
		webiopi.sleep(1)
		GPIO.output(ini_position,False)
		
	elif(angle==1):
		GPIO.output(DIR,True)
		GPIO.output(PLS,True)
		webiopi.sleep(0.01)
		GPIO.output(PLS,False)
		
	elif(angle==5):
		GPIO.output(DIR,True)
		for n in range(1,5,1):
			GPIO.output(PLS,True)
			webiopi.sleep(0.01)
			GPIO.output(PLS,False)
			webiopi.sleep(0.01)
			
	elif(angle==10):
			GPIO.output(DIR,True)
		for n in range(1,10,1):
			GPIO.output(PLS,True)
			webiopi.sleep(0.01)
			GPIO.output(PLS,False)
			webiopi.sleep(0.01)
