# Exercise 1: HELLO
# Lei Wang


from math import *
from swampy.TurtleWorld import *

def polygon(t, length, n):
	angle = 360.0/n
	for i in range(n):
		fd(t, length)
		lt(t, angle)

def circle(t, r):
	t.delay = 0.01
	length = 2* pi * r / 360
	polygon(t, length, 360)

def flip(t):
	lt(t)
	lt(t)

def move (t, size):
	pu(t)
	fd(t, size)
	pd(t)

def HELLO(size):
	bob = Turtle()
	bob.delay = 0.1
	print bob

	flip(bob)
	move(bob, size * 2)
	rt(bob) 	#turn turtle to face up, draw first line upward
	
	#HHHHH
	fd(bob, 2 * size)
	flip(bob)
	move (bob, size)
	lt(bob)
	fd(bob, size)
	lt(bob)
	move(bob, size)  # start from top to bottom for second vreticle line of H
	flip(bob)
	fd(bob,2 * size)

	#EEEEEE
	lt(bob)
	move(bob, size/2)
	fd(bob, size)
	flip(bob)
	move(bob, size)
	rt(bob)
	fd(bob, size)
	rt(bob)
	fd(bob, size)
	flip(bob)
	move(bob, size)
	rt(bob)
	fd(bob, size)
	rt(bob)
	fd(bob, size)

	#LLLLLL, start from top down
	move(bob, size/2)
	rt(bob)
	fd(bob, size * 2)
	lt(bob)
	fd(bob, size)

	#LLLLLLL, start from bottom
	move(bob, size/2) 
	fd(bob, size)
	flip(bob)
	move(bob, size)
	rt(bob)
	fd(bob, size * 2)

	#OOOOOO
	rt(bob)
	move(bob, size * 1.5)
	rt(bob)
	move(bob, size * 2)
	lt(bob)
	move(bob, size)
	circle(bob, size)

	bob.die()


world = TurtleWorld()

HELLO(50)
wait_for_user()