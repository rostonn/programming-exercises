# Calculate the mean, variance, and standard deviation for a list/array containing 10 random integers.
from random import randint
from math import sqrt
# Create list of 10 random integers

lowerBound = -100
upperBound = 100
arrayLength = 10
randomArray = []
for i in range(arrayLength):
	randomArray.append(randint(lowerBound, upperBound))

def sum(list):
	ans = 0
	for i in list:
		ans += i
	return ans

def avg(list):
	return sum(list)/len(list)

def variance(list):
	average = avg(list)
	diffSum = 0
	for i in list:
		diffSum += (i - average)**2
	return diffSum/len(list)

def standarDeviation(list):
    return sqrt(variance(list))

print('The array is: ')
print(randomArray)
print('The sum of the array is: ')
print(sum(randomArray))
print('The average is: ')
print(avg(randomArray))
print('The variance is: ')
print(variance(randomArray))
print('The standard deviation is: ')
print(standarDeviation(randomArray))
