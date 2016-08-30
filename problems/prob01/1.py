# Generate two random integers and print their mean, variance, and standard deviation.

# Generate two random integers
from random import randint
import math

lowerBound = -100
upperBound = 100
n1 = randint(lowerBound, upperBound)
n2 = randint(lowerBound, upperBound)

def mean(n1, n2):
	return (n1 + n2)/2

def variance(n1, n2):
	avg = mean(n1, n2)
	return ((n1 - avg)**2 + (n2 - avg)**2)/2

def stddev(n1, n2):
	return math.sqrt(variance(n1, n2))

meanN = mean(n1, n2)
varianceN = variance(n1, n2)
stddevN = stddev(n1, n2)

# Output
print("first number: " + str(n1))
print("second number: " + str(n2))
print("mean: " + str(meanN))
print("variance: " + str(varianceN))
print("standard deviation: " + str(stddevN))

