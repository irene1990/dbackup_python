import sys
sys.path.append(r'/home/irene/Documents/python/Class')
from Circle import Circle
import time
print(time.strftime('%H:%M:%S',time.localtime(time.time())))
c = Circle(5)
print("Radius:",c.radius)
print("Perimeter:",c.getPerimeter())
print("Area:",c.getArea())
