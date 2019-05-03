import sys

# function to flip a number to + or -
def flip(n):
	if n > 0: # positive
		negate = 0-n
		return negate
	elif n < 0: # negative
		negate = abs(n)
		return negate
	elif n == 0: # zero
		return 0	

# circle sizes : this only works with odd numbers
circles = [
	[], [0], #1
	[], [-1], #3
	[], [-2,-1], #5
	[], [-3,-2,-1], #7
	[], [-4,-3,-2], #9
	[], [-5,-4,-3,-2], #11
	[], [-6,-5,-4,-2], #13
	[], [-7,-6,-5,-4,-2], #15
	[], [-8,-7,-6,-4,-2], #17
	[], [-9,-8,-7,-6,-5,-3], #19
	[], [-10,-9,-8,-7,-6,-5,-3], #21
	[], [-11,-10,-9,-8,-7,-5,-3], #23
	[], [-12,-11,-10,-9,-8,-7,-5,-3], #25
	[], [-13,-12,-11,-10,-9,-7,-6,-3], #27
	[], [-14,-13,-12,-11,-10,-9,-8,-6,-3], #29
	[], [-15,-14,-13,-12,-11,-10,-9,-8,-6,-3], #31
	[], [-16,-15,-14,-13,-12,-11,-10,-8,-6,-4], #33
	[], [-17,-16,-15,-14,-13,-12,-11,-10,-9,-7,-4], #35
	[], [-18,-17,-16,-15,-14,-13,-12,-10,-9,-7,-4], #37
	[], [-19,-18,-17,-16,-15,-14,-13,-12,-11,-9,-7,-4], #39
	[], [-20,-19,-18,-17,-16,-15,-14,-12,-11,-9,-7,-4], #41
	[], [-21,-20,-19,-18,-17,-16,-15,-14,-13,-11,-10,-7,-4], #43
	[], [-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-10,-8,-4], #45
]
#23 length
####################################################################################

# get type of block to place as argument 1
block = "sandstone"

# get size of circle as argument 2
circle_size = 45
y = 23


ahk = "^r::\n"
while circle_size > 0: 
# check argument retraints - (must be an odd number [1 - 45])
#if int(circle_size)%2 != 0 and int(circle_size) > 0 and int(circle_size) <= 45:

	# get selected circle points from cirlce array
	circle = circles[int(circle_size)]

	# start AHK script - call by pushing Control+R
	#print("Making a Cirle with a diameter of: "+str(circle_size)+"\nOutput: circle.ahk")

	print("y_max:",y,"circle_size:", circle_size)

	# create negative axis
	ni = len(circle)-1

	# for each point in selected circle
	for i in range(0,len(circle)):

		# specify coords
		x1 = circle[i]
		z1 = flip(circle[ni])

		x2 = flip(circle[i])
		z2 = circle[ni]

		# de-increment negative index
		ni -= 1

		# build AHK command
		ahk += """
	;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
	Send, /
	Sleep 250
	Send, fill ~"""+str(x1)+""" ~-"""+str(y)+""" ~"""+str(z1)+""" ~"""+str(x2)+""" ~-"""+str(y)+""" ~"""+str(z2)+""" minecraft:"""+block+"""
	Send, {Enter}\n
	"""

	circle_size -= 2
	y -=1



# write to circle.ahk
f = open("circle.ahk", "w")
f.write(ahk)
f.close()



