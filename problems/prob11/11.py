# Generate a random number from 1000 to 9999 and output the sum of its digits
# repeatedly, dropping the left-most digit after each iteration, until there is only one digit only.
# For example, if the number is 1049, then the output should be 14, 13, 13, 9.

from random import randint

# Generate random number

num = randint(1000, 9999)

num_array = [int(i) for i in str(num)]

print(num)
print(num_array)


for idx, val in enumerate(num_array):
	sum = 0
	for i in range(len(num_array) - idx):
		sum += num_array[i]
	print(sum)

