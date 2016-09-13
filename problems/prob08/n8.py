# Discount Percentage: Write a function that takes a dollar amount and a
# discount percentage and returns the total discount amount. Return a warning if
#the discount amount is greater than 100 or less that 0 percent. Test the results.

# Class it up. Wrap a class around the last function. Instantiate the class and
# call the function. Then use unittests and rspec to test.

class Discount:
    def __init__(self, amount, discount_percentage):
        self.amount = amount
        self.discount_percentage = discount_percentage

    def discount_calc(self):
        if self.discount_percentage < 0 or self.discount_percentage > 100:
            return "Discount percentage cannot be less than 0 or greater than 100"
        return (self.discount_percentage * 0.01) * self.amount
