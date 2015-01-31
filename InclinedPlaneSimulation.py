from visual import *
scene.autoscale = False
scene.range = 4
scene.center = (5, -2, 0)

ramp = box(pos = vector(0, 0, 0), size = (20, 0.5, 5), color = color.white)
cart = box(pos = vector(0, 0.55, 0), size = (2, 1, 1), color = color.blue)

ramp.rotate(angle=-pi/12, axis=(0, 0, 1))
cart.rotate(angle=-pi/12, axis=(0, 0, 1))

mcart = 0.80
vcart = vector(0, 0, 0)

vvector = arrow(pos = cart.pos, axis= vcart * 0.01, color=color.green)

deltat = 0.01
t = 0
Fgandf = vector(cos(-pi/12), -sin(pi/12), 0)

while True:
   rate(100)
   Fnet = Fgandf
   vcart += (Fnet/mcart) * deltat
   cart.pos = cart.pos + (vcart)*deltat
   vvector.pos = cart.pos
   vvector.axis = vcart

