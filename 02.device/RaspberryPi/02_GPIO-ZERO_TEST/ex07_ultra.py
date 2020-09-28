from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(23, 24) # echo, trig

while True:
    print('Distance to nearest object is', sensor.distance, 'm')
    sleep(1)