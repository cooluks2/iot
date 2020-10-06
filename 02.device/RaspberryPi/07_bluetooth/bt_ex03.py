from btsocket import BtSocket
from bluetooth import * 
from gpiozero import AngularServo

servo = AngularServo(25, min_angle=-90, max_angle=90, 
                     min_pulse_width=0.0006, max_pulse_width=0.0024)

def control(tokens):
    command = int(tokens[0])
    if command == 0 : # 주행모드
        x = int(tokens[1])
        y = int(tokens[2])
    elif command == 1 : #카메라 모드
        angle = int(tokens[1])
        servo.angle = angle

RFADDR = "00:18:91:D7:67:13"
client_socket=BtSocket( RFCOMM ) 
client_socket.connect((RFADDR, 1)) 

try:
    while True:
        line = client_socket.readline()
        print(line)
        control(line.split(','))
except KeyboardInterrupt:
    print("Finished")

client_socket.close() 
