from visual import *
import time

scene = display(title='Simulation of block on inclined plane',
     x=0, y=0, width=1920, height=1036,
     center=(5,0,0), background=(0,0,0))

scene.autoscale = False
scene.range = 20
scene.center = (30, -2, 0)


ramp = box(pos = vector(0, 0, 0), size = (100, 0.5, 10), color = color.white)
cart = box(pos = vector(0, 0.55, 0), size = (2, 1, 1), color = color.blue)

ramp.rotate(angle=-pi/10, axis=(0, 0, 1))
cart.rotate(angle=-pi/10, axis=(0, 0, 1))

mcart = 0.80
vcart = vector(0, 0, 0)

vvector = arrow(pos = cart.pos, axis= vcart * 0.01, color=color.green)

deltat = 0.01
t = 0
Fgandf = vector(0.3828 * cos(-pi/10), -0.3828 * sin(pi/10), 0)

time.sleep(10)
while True:
   rate(500)
   Fnet = Fgandf
   vcart += (Fnet/mcart) * deltat
   cart.pos = cart.pos + (vcart)*deltat
   vvector.pos = cart.pos
   vvector.axis = vcart

