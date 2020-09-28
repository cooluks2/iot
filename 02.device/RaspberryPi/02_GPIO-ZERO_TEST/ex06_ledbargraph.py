from gpiozero import LEDBarGraph
from time import sleep

graph = LEDBarGraph(18, 23, 24, pwm=True)

graph.value = 1/10 # (0.5, 0, 0)
sleep(1)
graph.value = 3/10 # (1, 0.5, 0)
sleep(1)
# 음수 뒤에서 해석
graph.value = -3/10 # (0, 0, 0)
sleep(1)
graph.value = 9/10 # (1, 1, 1)
sleep(1)
graph.value = 95/100 # (1, 1, 1)
sleep(1)