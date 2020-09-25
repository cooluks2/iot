# MCP3008

###  MCP3008

-   ADC: Analog to Digital Converter

![image-20200925160905253](04_MCP3008(ADC),_SPI_통신.assets/image-20200925160905253.png)

<br>

### MCP3008 통신

-   SPI 통신으로 데이터 전송, MCP3008 IC는 slave로 동작
-   신호 타이밍 : 8비트로 세번 나누어져 있음
    -   첫 바이트 : 라즈베리파이로 MOSI(DIN)을 통해 0x01을 보내서 start를 알림 
    -   두 번째 바이트 : 상위 4비트를 통해 ADC값을 얻고자 하는 채널을 선택 
    -   세번째 바이트 : MISO(DOUT)핀을 통해 null 비트로 시작하는 ADC값 전송

![image-20200925161020063](04_MCP3008(ADC),_SPI_통신.assets/image-20200925161020063.png)

>   timig diag.

<br>

### 채널 선택

![image-20200925161045210](04_MCP3008(ADC),_SPI_통신.assets/image-20200925161045210.png)

<br>

### SPI 라이브러리

-   $ `sudo pip3 install --upgrade spidev`

-   라즈베리파이

    -   2개의 SPI 장치

    -   `ls /dev/spi*`

        -   /dev/spidev0.0 
        -   /dev/spidev0.1 
        -   bus 값은 0이고 각각 device 값이 0와 1인 2개의 SPI 장치

        >   Raspberry Pi Configuration > Interfaces > 맨 아래 제외 Enable

<br>

### 핀이름

-   MOSI : Master Out Slave In 
-   MISO : Master In Slave Out 
-   CE : Chip Enable( CE0 : 0번 디바이스 선택, CE1: 1번 디바이스 지정)

![image-20200925161326066](04_MCP3008(ADC),_SPI_통신.assets/image-20200925161326066.png)

![image-20200925161339890](04_MCP3008(ADC),_SPI_통신.assets/image-20200925161339890.png)

<br>

**01_GPIO-TEST/gpioapp.py**

```python
from piapp import *
import RPi.GPIO as GPIO

from ledex import LedEx
from btnex import BtnEx
from btneventex import BtnEventEx
from pwmex import PwmEx
from pwmservoex import PwmServoEx
from ultraex import UltraEx
from mcpex import McpEx

class GpioApp(PiApplication):
    def __init__(self):
        super().__init__()

    def create_menu(self, menu):	
        menu.add_menu(MenuItem("종료", self.exit))
        menu.add_menu(MenuItem("LED", LedEx()))
        menu.add_menu(MenuItem("Button", BtnEx()))
        menu.add_menu(MenuItem("Button Event", BtnEventEx()))
        menu.add_menu(MenuItem("PWM LED", PwmEx()))
        menu.add_menu(MenuItem("Servo", PwmServoEx()))
        menu.add_menu(MenuItem("Distance", UltraEx()))
        menu.add_menu(MenuItem("Mcp", McpEx()))

if __name__ == "__main__":
    app = GpioApp()
    app.run()
```



<br>

**01_GPIO-TEST/mcpex.py**

```python
import spidev, time

class McpEx:
    def __init__(self):
            # 디바이스 초기화
            self.spi = spidev.SpiDev()
            self.spi.open(0,0) # (버스, 디바이스)
            self.spi.mode = 3
            self.spi.max_speed_hz = 1000000

    def analog_read(self, channel):
        # 매개변수 (시작비트, 채널, 자릿수 맞춤 위치), 리턴값 : 아날로그 값
        r = self.spi.xfer2([1, (0x08+channel)<<4, 0])  # Pi -> MCP, MCP -> Pi
        adc_out = ((r[1]&0x03)<<8) + r[2] # 수신 데이터 결합
        return adc_out

    def __call__(self):
        while True:
            adc = self.analog_read(0)
            voltage = adc*5/1023
            print("ADC = %s(%d) Voltage = %.3fV" % (hex(adc), adc, voltage))
            time.sleep(0.5)
```

ADC = **0x117(279)** Voltage = **1.364V**

:

---

>   adc_out 바이트를 SPI 통신과 연관지어 생각해보자.
>
>   **r[1]&0x03** : 상위 6bits 0 → 000000**xx**
>
>   **(r[1]&0x03)<<8** : left shift 8bits → 000000**xx00000000**
>
>   **((r[1]&0x03)<<8) + r[2]** → r[1] 2bits + r[2] 8bits 결합 총 10bits

<br>