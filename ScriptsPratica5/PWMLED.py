from gpiozero import PWMLED
from time import sleep

led = PWMLED(15)

contador = 0

while contador < 3:
	led.value= 0
	sleep(1)
	led.value = 0.35
	sleep(1)
	led.value = 1
	sleep(1)
	contador = contador +1
