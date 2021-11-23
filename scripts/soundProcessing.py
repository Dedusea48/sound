import math as mt
import matplotlib.pyplot as plt
import numpy as np
import soundFunctions as SF

T = 297.15
R = 8314.5
m1 = 28.97
m2 = 18.01
m3 = 44.01
cp1 = 1.0036
cp2 = 1.863
cp3 = 0.838
cv1 = 0.7166
cv2 = 1.403
cv3 = 0.649
x1 = 0.9927
xvp = 0.01
x3 = 0.0003

eps1 = (m1*cp1*x1 + m2*cp2*xvp + m3*cp3*x3)/(m1*cv1*x1 + m2*cv2*xvp + m3*cv3*x3)
mi = m1*x1 + m2*xvp + m3*x3

V1 = mt.sqrt((eps1*R*T)/mi)
print(V1)

x33 = 0.043

eps2 = (m1*cp1*(1-xvp-x33) + m2*cp2*xvp + m3*cp3*x33)/(m1*cv1*(1-xvp-x33) + m2*cv2*xvp + m3*cv3*x33)
mi2 = m1*(1-xvp-x33) + m2*xvp + m3*x33
V2 = mt.sqrt((eps2*R*T)/mi2)
print(V2)

a = (V2 - V1)/(x33 - x3)/100
b = V1 - a*x3
x = np.linspace(0,5,100)
plt.ylabel('Скорость звука [м/с]')
plt.xlabel('Концентрация CO2 [%]')
y = a*x + b


plt.plot(x,y, label = 'Аналитическая зависимость')
plt.grid(True)
plt.scatter(x3*100,V1, label = 'Значение в воздухе: 345.59 [м/с], 0.03 [%] ' )
plt.scatter(x33*100,V2, label = 'Значение в выдохе: 341.56 [м/с], 4.3 [%]')
plt.legend()
plt.show()
