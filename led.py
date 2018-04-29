import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
while True:
   x = str(input())
   if(x == "AC"):
      GPIO.output(pin,GPIO.HIGH)
      print("Acildi !!! )
      time.sleep(3)
   if(x == "KAPA"):
      GPIO.output(pin,GPIO.LOW)
      print("Kapandi !!!")
      time.sleep(1)
 GPIO.cleanup()
