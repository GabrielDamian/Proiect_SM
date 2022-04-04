import RPi.GPIO as GPIO
import time
import smtplib
from w1thermsensor import W1ThermSensor
from threading import RLock, Thread
from modules.toggle import is_on, lock
sensor=W1ThermSensor()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.output(8,1) # initializare

user_name = 'petrusistememicroprocesor'
password = 'sistememicroprocesor2022'
sleep_time = 1

siri_control = Control(user_name, password)
Thread(target = siri_control.handle).start()
while 1:
    lock.acquire()
    on = is_on
    lock.release()
    if on:
        t=sensor.get_temperature()
        minT = ? # fetc minTemp from server
        maxT = ? # fetc maxTemp from server
        if minT <= t <= maxT:
            GPIO.output(8,1) # stingere LED semnalizare
            print('Temperatura este %2.2f '%(t)+"grade Celsius")
        else:
            GPIO.output(8,0) # aprind LED semnalizare
            server=smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(user_name, password)
               
            msg = f'Temperatura {t} a iesit din intervalul setat [{minT}, {maxT}]'
            server.sendmail(user_name + '@gmail.com', user_name + '@gmail.com', msg)
            server.quit()

            print("S-a trimis mail, la  %2.2f" %(t)+"grade")
	time.sleep(sleep_time)

		