import webiopi
import os
webiopi.setDebug()
GPIO = webiopi.GPIO

#実行ピン(mbed1、mbed2共通)
RUN1 = 2		#True:実行 False：しない(mbedへ)
RUN2 = 17
#動作終了
EndCallBack = 23	#mbed1から受け取る終了シグナル入力ピン
#Raspi→5V反転スイッチ回路→12V反転スイッチ回路→リレー→電磁弁
#つまりRaspiの信号とリレーから出力される信号は同じ
Relay = 14		#電磁弁の開閉タイミングは1秒以上にすること（間隔が小さいと電磁弁が破損する）

#水平
ini_position1 = 3	#True:初期化 False:しない(mbedへ)
PLS1 = 15		#送ったパルスの数だけ回転させる(mbedへ)
DIR1 = 4		#True:CW False:CCW(mbedへ)

#垂直
ini_position2 = 27		#True:初期化 False:しない(mbedへ)
PLS2 = 18		#送ったパルスの数だけ回転させる(mbedへ)
DIR2 = 22		#True:CW False:CCW(mbedへ)

Total1 = 0
Total2 = 0
step_t = 0.01

#GPIOの設定
def setup():
	webiopi.debug("Webiopi起動...GPIOを設定しています\n")
	#import
	GPIO.setFunction(EndCallBack, GPIO.IN)
	#output
	GPIO.setFunction(RUN1, GPIO.OUT)
	GPIO.setFunction(RUN2, GPIO.OUT)
	GPIO.setFunction(Relay, GPIO.OUT)
	GPIO.setFunction(ini_position1, GPIO.OUT)
	GPIO.setFunction(PLS1, GPIO.OUT)
	GPIO.setFunction(DIR1, GPIO.OUT)
	GPIO.setFunction(ini_position2, GPIO.OUT)
	GPIO.setFunction(PLS2, GPIO.OUT)
	GPIO.setFunction(DIR2, GPIO.OUT)

def loop():
	#終了シグナルの実行(RUN1=0など初期状態にする)
	if(GPIO.input(EndCallBack)==1):
		webiopi.debug("動作終了です\n")
		GPIO.output(RUN1,False)
		GPIO.output(RUN2,False)
		GPIO.output(ini_position1,True)
		GPIO.output(ini_position2,True)
		GPIO.output(Relay,False)
		webiopi.sleep(1)
		webiopi.debug("待機中\n")

#mbedに実行シグナル
#mbedとリレーには入力と出力が反転
@webiopi.macro
def Do():
	webiopi.debug("実行中")
	GPIO.output(ini_position1,False)
	GPIO.output(ini_position2,False)
	GPIO.output(RUN1,True)
	GPIO.output(RUN2,True)
	GPIO.output(Relay,True)
	webiopi.sleep(1)

@webiopi.macro
def Pause():
	webiopi.debug("一時停止")
	GPIO.output(ini_position1,False)
	GPIO.output(ini_position2,False)
	GPIO.output(RUN1,False)
	GPIO.output(RUN2,False)
	GPIO.output(Relay,False)
	webiopi.sleep(1)
	
@webiopi.macro
def End():
	webiopi.debug("終了しました")
	GPIO.output(ini_position1,True)
	GPIO.output(ini_position2,True)
	GPIO.output(RUN1,False)
	GPIO.output(RUN2,False)
	GPIO.output(Relay,False)
	webiopi.sleep(1)

#水平
@webiopi.macro
def onChangeAnglePan(angle1):
	Hightime = 0.02
	Lowtime = 0.005
	global Total1
	Total1 += int(angle1)
	s = Total1
	webiopi.debug("水平")
	"""
	if(angle1=="0"):
		webiopi.debug("原点")
		Total1 = 0
		s = 0
		GPIO.output(ini_position1,True)
		webiopi.sleep(0.1)
		GPIO.output(ini_position1,False)
		webiopi.sleep(0.1)
	"""
	#-45°以下は首ふりできないようにする
	if(Total1<-40):
		Total1 = -40
		webiopi.debug("LimitMin=="+str(Total1))
	#45°以上は首ふりできないようにする
	elif(Total1>40):
		Total1 = 40
		webiopi.debug("LimitMax=="+str(Total1))

	else:
		#ハーフステップ（0.9°）駆動
		if(angle1=="-10"):
			GPIO.output(DIR1,False)
			webiopi.sleep(0.01)
			webiopi.debug("-10°")
			for n in range(0,100,1):
				GPIO.output(PLS1,True)
				webiopi.debug("1")
				webiopi.sleep(Hightime)
				GPIO.output(PLS1,False)
				webiopi.debug("0")
				webiopi.sleep(Lowtime)

		elif(angle1=="-5"):
			GPIO.output(DIR1,False)
			webiopi.sleep(0.01)
			webiopi.debug("-5°")
			for n in range(0,50,1):
				GPIO.output(PLS1,True)
				webiopi.debug("1")
				webiopi.sleep(Hightime)
				GPIO.output(PLS1,False)
				webiopi.debug("0")
				webiopi.sleep(Lowtime)

		elif(angle1=="-1"):
			webiopi.debug("-1°")
			GPIO.output(DIR1,False)
			webiopi.sleep(0.01)
			for n in range(0,10,1):
				GPIO.output(PLS1,True)
				webiopi.debug("1")
				webiopi.sleep(Hightime)
				GPIO.output(PLS1,False)
				webiopi.debug("0")
				webiopi.sleep(Lowtime)

		elif(angle1=="1"):
			webiopi.debug("1°")
			GPIO.output(DIR1,True)
			webiopi.sleep(0.01)
			for n in range(0,10,1):
				GPIO.output(PLS1,True)
				webiopi.debug("1")
				webiopi.sleep(Hightime)
				GPIO.output(PLS1,False)
				webiopi.debug("0")
				webiopi.sleep(Lowtime)

		elif(angle1=="5"):
			webiopi.debug("5°")
			GPIO.output(DIR1,True)
			webiopi.sleep(0.01)
			for n in range(0,50,1):
				GPIO.output(PLS1,True)
				webiopi.debug("1")
				webiopi.sleep(Hightime)
				GPIO.output(PLS1,False)
				webiopi.debug("0")
				webiopi.sleep(Lowtime)

		elif(angle1=="10"):
			webiopi.debug("10°")
			GPIO.output(DIR1,True)
			webiopi.sleep(0.01)
			for n in range(0,100,1):
				GPIO.output(PLS1,True)
				webiopi.debug("1")
				webiopi.sleep(Hightime)
				GPIO.output(PLS1,False)
				webiopi.debug("0")
				webiopi.sleep(Lowtime)
				
		webiopi.debug("LastValue:"+str(Total1))
#垂直
@webiopi.macro
def onChangeAngleTilt(angle2):
	Hightime = 0.02
	Lowtime = 0.005
	global Total2
	Total2 += int(angle2)
	s = Total2
	webiopi.debug("垂直")
	"""
	if(angle1=="0"):
		webiopi.debug("原点")
		Total2 = 0
		s = 0
		GPIO.output(ini_position1,True)
		webiopi.sleep(0.1)
		GPIO.output(ini_position1,False)
		webiopi.sleep(0.1)
	"""
	#-45°以下は首ふりできないようにする
	if(Total2<-40):
		Total2 = -40
		webiopi.debug("LimitMin=="+str(Total2))
	#45°以上は首ふりできないようにする
	elif(Total2>40):
		Total2 = 40
		webiopi.debug("LimitMax=="+str(Total2))

	else:
		#ハーフステップ（0.9°）駆動
		if(angle2=="-10"):
			GPIO.output(DIR2,False)
			webiopi.sleep(0.01)
			webiopi.debug("-10°")
			for n in range(0,10,1):
				GPIO.output(PLS2,True)
				webiopi.debug("1")
				webiopi.sleep(Hightime)
				GPIO.output(PLS2,False)
				webiopi.debug("0")
				webiopi.sleep(Lowtime)

		elif(angle2=="-5"):
			GPIO.output(DIR2,False)
			webiopi.sleep(0.01)
			webiopi.debug("-5°")
			for n in range(0,5,1):
				GPIO.output(PLS2,True)
				webiopi.debug("1")
				webiopi.sleep(Hightime)
				GPIO.output(PLS2,False)
				webiopi.debug("0")
				webiopi.sleep(Lowtime)

		elif(angle2=="-1"):
			webiopi.debug("-1°")
			GPIO.output(DIR2,False)
			webiopi.sleep(0.05)
			GPIO.output(PLS2,True)
			webiopi.debug("1")
			webiopi.sleep(Hightime)
			GPIO.output(PLS2,False)
			webiopi.debug("0")
			webiopi.sleep(Lowtime)

		elif(angle2=="1"):
			webiopi.debug("1°")
			GPIO.output(DIR2,True)
			webiopi.sleep(0.05)
			GPIO.output(PLS2,True)
			webiopi.debug("1")
			webiopi.sleep(Hightime)
			GPIO.output(PLS2,False)
			webiopi.debug("0")
			webiopi.sleep(Lowtime)

		elif(angle2=="5"):
			webiopi.debug("5°")
			GPIO.output(DIR2,True)
			webiopi.sleep(0.01)
			for n in range(0,5,1):
				GPIO.output(PLS2,True)
				webiopi.debug("1")
				webiopi.sleep(Hightime)
				GPIO.output(PLS2,False)
				webiopi.debug("0")
				webiopi.sleep(Lowtime)

		elif(angle2=="10"):
			webiopi.debug("10°")
			GPIO.output(DIR2,True)
			webiopi.sleep(0.01)
			for n in range(0,10,1):
				GPIO.output(PLS2,True)
				webiopi.debug("1")
				webiopi.sleep(Hightime)
				GPIO.output(PLS2,False)
				webiopi.debug("0")
				webiopi.sleep(Lowtime)
				
		webiopi.debug("LastValue:"+str(Total2))
		
def destroy():
	GPIO.output(RUN1,False)
	GPIO.output(RUN2,False)
	GPIO.output(Relay,False)
	GPIO.output(ini_position1, False)
	GPIO.output(PLS1, False)
	GPIO.output(DIR1, False)
	GPIO.output(ini_position2, False)
	GPIO.output(PLS2, False)
	GPIO.output(DIR2, False)
	webiopi.debug("webiopiを終了します\n")