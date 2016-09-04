# Generate a single random number, from 0 to 100. If the number is greater than 40 then output all the odd integers
# from 40 to the random number. If the number is less than 40, output all the odd integers from 0 to 40.

# Define class

from random import randint

class Odd:
    def __init__(self, number):
        if number < 40:
            self.arr = [i for i in range(1, 40, 2)]
        else:
            self.arr = [i for i in range(41, number, 2)]

    def get_num(self):
        return self.arr

    def print_num(self):
        for num in self.arr:
            print(num)

# Generate Random Number
num = randint(0, 100)
print('The number is: ' +  str(num))

# Make object of Odd class based on the random number
ans = Odd(num)

# Print object array
print(ans.get_num())
# Call object print method
ans.print_num()

if 5 > 4:
	print('The tab spaces work now!')
	print('Now do they work?')
