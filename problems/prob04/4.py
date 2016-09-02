# Generate a single random number, from 0 to 100, then output all the even integers from 0 to the random number.

from random import randint

# Create a single random number between 0 and 100

print('Generate a single random number, from 0 to 100, \nthen output all the even integers from 0 to the random number')

number = randint(0,100)
print('The random number is: ' + str(number))
for num in range(number + 1):
	if num % 2 == 0:
		print(num)


