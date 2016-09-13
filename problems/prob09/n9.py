# generate n random integers from 0 to 100, then output them in ascending order.

from random import sample

# number of integers
n = 10

# range
r = 10
lower = 0
upper = 100
list = sample(range(lower, upper), n)

print(sorted(list)) 
