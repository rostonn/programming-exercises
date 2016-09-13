# Discount Percentage: Write a function that takes a dollar amount and a discount
#  percentage and returns the total discount amount. Return a warning if the discount
#  amount is greater than 100 or less that 0 percent. Test the results.

def discount(amount, discount_percentage):
	if discount_percentage > 100 or discount_percentage < 0:
		return "Discount percentage cannot be less than 0 or greater than 100"
	
	print("Amount = " + str(amount))
	print(discount_percentage)
	print(discount_percentage * 0.01)	
	return amount*(discount_percentage * 0.01)

# Add unittest

print("Expect 100, 10 to be 10")
print(discount(100, 10))
