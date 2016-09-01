# Generate twenty random integers from 0 to 100 and print the largest and smallest integers.

from random import randint
#Set environment variables
lowerBound = 0
upperBound = 100
number = 20

# Create Random Integers
def create_random_array(lowerBound, upperBound, number):
	list = [randint(lowerBound, upperBound) for i in xrange(number)]
	return list

list = create_random_array(lowerBound, upperBound, number)		

# Find Largest and smallest integers
max = max(list)
min = min(list)

print('The list is: ')
print(list)
print('The minimum is:')
print(min)
print('The maximum is: ')
print(max)

