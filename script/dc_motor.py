# -*- coding: utf-8 -*-
# webiopiモジュールインポートが必要
import webiopi

GPIO = webiopi.GPIO
LED1 = 25
LED2 = 18
IN1 = 17
IN2 = 27

# スクリプトがロードされるときにWebIOPiサーバから呼ばれる
# 処理をsetup()関数、WebIOPiサーバが起動中に繰り返し呼
# ばれる処理をloop()関数、WebIOPiサーバのシャットダウン
# 時に呼ばれる処理をdestroy()関数へ記述する必要がある
# ので、これらの3つの関数は必ず用意すること

def setup():
    # LED1、LED2、IN2、IN2のGPIOを出力モードへ設定
    GPIO.setFunction(LED1, GPIO.OUT)
    GPIO.setFunction(LED2, GPIO.OUT)
    GPIO.setFunction(IN1, GPIO.OUT)
    GPIO.setFunction(IN2, GPIO.OUT)

def loop():
    # LED1、LED2の値に応じて、呼び出す処理を変更
    led1 = GPIO.digitalRead(LED1)
    led2 = GPIO.digitalRead(LED2)
    if led1 == GPIO.HIGH and led2 == GPIO.LOW:
        forward()
    if led1 == GPIO.LOW and led2 == GPIO.HIGH:
        back()
    if led1 == GPIO.LOW and led2 == GPIO.LOW:
        stop()
    # 1.0秒間処理を停止
    webiopi.sleep(1.0)

def destroy():
    # モーターを停止してから、各GPIOを入力モードへ設定
    stop()
    GPIO.setFunction(LED1, GPIO.IN)
    GPIO.setFunction(LED2, GPIO.IN)
    GPIO.setFunction(IN1, GPIO.IN)
    GPIO.setFunction(IN2, GPIO.IN)

# 前進
def forward():
    GPIO.digitalWrite(IN1, GPIO.HIGH)
    GPIO.digitalWrite(IN2, GPIO.LOW)

# 後退
def back():
    GPIO.digitalWrite(IN1, GPIO.LOW)
    GPIO.digitalWrite(IN2, GPIO.HIGH)

# 前進開始、マクロで提供
@webiopi.macro
def begin_forwoard():
    # 反転時の場合にモーターが壊れないようにstopを入れる
    stop()
    GPIO.digitalWrite(LED1, GPIO.HIGH)

# 後退開始、マクロで提供
@webiopi.macro
def begin_back():
    # 反転時の場合にモーターが壊れないようにstopを入れる
    stop()
    GPIO.digitalWrite(LED2, GPIO.HIGH)

@webiopi.macro
def stop():
    # 各GPIOをLOWにしてから1ミリ秒停止
    GPIO.digitalWrite(LED1, GPIO.LOW)
    GPIO.digitalWrite(LED2, GPIO.LOW)
    GPIO.digitalWrite(IN1, GPIO.LOW)
    GPIO.digitalWrite(IN2, GPIO.LOW)
    webiopi.sleep(0.001)

