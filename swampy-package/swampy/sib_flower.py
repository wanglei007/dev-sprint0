# Flower excercise (4.2) from Week 0

# Name: Lei Wang


from TurtleWorld import * 	
from math import *


# This is where you put code to move bob


def polyline(t, step, angle, n):
	for i in range (n):
		fd(t, step)
		lt(t, angle)

def mv (t, step):
	pu(t)
	fd(t, step)
	pd(t)

def flower(t, n, angle, size = 55):

	x, y = t.x, t.y
	p0 = [x,y]
	heading = t.heading

	theta = 360.0/n
	for i in range (n):
		polyline(t, 1, angle, size)
		t.x, t.y = p0
		t.heading = heading  - theta * i
		polyline(t, 1, -angle, size)
		t.x, t.y = p0
		t.heading = heading + theta * (i+1)

	t.x, t.y = p0
	t.heading = heading




world = TurtleWorld()			
bob = Turtle()				
bob.delay = 0.01

mv(bob, -50)
flower(bob, 7, 1, 55)

mv(bob, 150)
bob.heading = 0
flower(bob, 10, 1, 74)

mv(bob, 150)
bob.heading = 0
flower(bob, 20, 0.3, 63)

bob.die()

wait_for_user()					

