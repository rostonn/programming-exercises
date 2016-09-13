from random import randint

# Random number between 1000 and 9999

num = randint(1000, 9999)

numString = str(num)
sum = 0
for i in numString:
	sum += int(i)


print(num)
print(sum)
