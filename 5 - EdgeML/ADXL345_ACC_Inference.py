from machine import Pin,I2C
import ADXL345
import time
from regressor import score

i2c = I2C(scl=Pin(22),sda=Pin(21), freq=10000)
adx = ADXL345.ADXL345(i2c)

x=adx.xValue
y=adx.yValue
z=adx.zValue
print('The acceleration info of x, y, z are:%d,%d,%d'%(x,y,z))
_, pitch = adx.RP_calculate(x,y,z)

pitch_pred = score([x, y, z])

print('pitch_actual: ', pitch, '\n',
      'pitch_pred: ', pitch_pred, '\n',)