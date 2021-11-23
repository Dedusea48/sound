import numpy as np

def speedOfSound(temperature, h2oX, co2Max):
    T = temperature - 273.15
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
    if h2oX > 1:
        xvp = h2oX/100
    else:
        xvp = h2oX
    x3 = 0.0003
    eps1 = (m1 * cp1 * x1 + m2 * cp2 * xvp + m3 * cp3 * x3) / (m1 * cv1 * x1 + m2 * cv2 * xvp + m3 * cv3 * x3)
    mi = m1 * x1 + m2 * xvp + m3 * x3

    V1 = ((eps1 * R * T) / mi)**0.5

    if co2Max> 1:
        x33 = co2Max/100
    else:
        x33 = co2Max

    eps2 = (m1 * cp1 * (1 - xvp - x33) + m2 * cp2 * xvp + m3 * cp3 * x33) / (
                m1 * cv1 * (1 - xvp - x33) + m2 * cv2 * xvp + m3 * cv3 * x33)
    mi2 = m1 * (1 - xvp - x33) + m2 * xvp + m3 * x33
    V2 = ((eps2 * R * T) / mi2)**0.5

    a = (V2 - V1) / (x33 - x3) / 100
    b = V1 - a * x3
    x = np.linspace(0, 5, 100)
    y = a * x + b

    co2X = [0]*101
    soundSpeed = [0]*101
    
    for i in range(101):
        co2X[i] = i
        soundSpeed[i] =  a * i + b
   
    
    return(co2X, soundSpeed)