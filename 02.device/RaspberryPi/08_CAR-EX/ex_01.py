from gpiozero import Robot
from time import sleep

# left/right=(전진,후진,PWM)
robot = Robot(left=(17, 27, 22), right=(15, 18, 14), pwm=True)

for i in range(4):
    robot.forward(0.5)  # 0 ~ 1 사이
    sleep(1)
    robot.stop()
    sleep(1)
    robot.right(0.5)
    sleep(1)
    robot.stop()
    sleep(1)