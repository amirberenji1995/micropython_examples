from machine import Pin,I2C
import ADXL345
import time

i2c = I2C(scl=Pin(22),sda=Pin(21), freq=10000)
adx = ADXL345.ADXL345(i2c)

while True:
    x=adx.xValue
    y=adx.yValue
    z=adx.zValue
    #print('The acceleration info of x, y, z are:%d,%d,%d'%(x,y,z))
    roll,pitch = adx.RP_calculate(x,y,z)
    #print('roll=',roll)
    #print('pitch=',pitch)
    measurement = str('\n') + str(x) + str(',') + str(y) + str(',') + str (z) +str(',') + str(roll) + str(',') + str(pitch)
    with open('log.txt', 'a') as f:
        f.write(measurement)
    print(measurement)
    time.sleep_ms(50)