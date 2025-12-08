from gpiozero import LED
from time import sleep
led = LED(14)
led.off()

contador = 0
while contador < 5:
	led.on()
	sleep(1)
	led.off()
	sleep(1)
	contador = contador+1
	

