# Python3 program to find Minkowski distance

# import math library
from math import *
from decimal import Decimal

# Function distance between two points
# and calculate distance value to given
# root value(p is root value)
def p_root(value, root):
	
	root_value = 1 / float(root)
	return round (Decimal(value) **
			Decimal(root_value), 3)

def minkowski_distance(x, y, p_value):
	
	# pass the p_root function to calculate
	# all the value of vector parallelly
	return (p_root(sum(pow(abs(a-b), p_value)
			for a, b in zip(x, y)), p_value))

# Driver Code
vector1 = [22, 2, 42, 11]
vector2 = [20, 1, 36, 9]
p = 3
print(minkowski_distance(vector1, vector2, p))
