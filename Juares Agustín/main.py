from machine import ADC, Pin
from math import log
import time
pin = Pin(4, Pin.OUT) 
pin2 = Pin(6, Pin.OUT)
pot = machine.ADC(26)
adc = machine.ADC(27)
buzzer = Pin(14, Pin.OUT)
buzzer.off
B = 3900 
T0 = 298 
R = 10000 
conversion_factor = 3.3 / 65535

while (1):
  pot_value = (pot.read_u16()*35) / 65535
  Recter = adc.read_u16() * conversion_factor  
  Resis = (Recter*10000)/(3.3-Recter)
  Temp = ((T0*B)/(T0*log(Resis/R)+B)) -273.15
  print("Potenciometro : {} Temperatura : {}".format(pot_value, Temp))
  if (Temp < pot_value):
    pin.value(1)
    pin2.value(0)  
    buzzer.off () 
  elif (Temp > pot_value) :
      pin.value(0)
      pin2.value(1)
      buzzer.on ()

