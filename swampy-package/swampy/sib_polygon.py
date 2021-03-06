# Polygon excercise from Week 0 -- refactored

# Name: Lei Wang


from TurtleWorld import * 	
from math import *	

# This is where you put code to move bob

def square(t, size):
	polygon(t, size, 4)

def polyline(t, size, angle, n):
	for i in range (n):
		fd(t, size)
		lt(t, angle)

def polygon(t, size, n):
    angle = 360.0/n
    polyline(t, size, angle, n)

#move from center of circle to bottom
def md (t, size):
	pu(t)
	rt(t)
	fd(t, size)
	lt(t)
	pd(t)

def circle(t, r):
	md(t, r)
	t.delay = 0.01
	size = 2 * pi * r /360.0
	polyline(t, size, 1, 360)

def arc(t, r, theta):
	md(t, r)
	t.delay = 0.01
	size = 2 * pi * r /360.0
	polyline(t, size, 1, theta)

world = TurtleWorld()			
bob = Turtle()	
square(bob, 50)

world = TurtleWorld()			
bob = Turtle()	
circle(bob, 50)

world = TurtleWorld()			
bob = Turtle()	
arc(bob, 50, 180)

wait_for_user()		