from visual import *
scene.autoscale = False


ramp = box(pos=vector(0, -0.025, 0), size=(20, 0.05, 0.10), color=color.white)
cart = box(pos = ramp.pos, size = (0.1, 0.04, 0.06), color = color.blue)
ramp.rotate(angle=-pi/12, axis=(0, 0, 1))
cart.rotate(angle=-pi/12, axis=(0, 0, 1))
mcart = 0.80
vcart = vector(0, 0, 0)
vvector = arrow(pos = cart.pos,axis= vcart, color=cart.color)

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
