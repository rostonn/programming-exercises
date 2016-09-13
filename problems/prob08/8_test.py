from n8 import Discount
import unittest


d = Discount(100, 10)
print(d.discount_calc())

class DiscountTest(unittest.TestCase):

    def test_discount(self):
        discount = Discount(100, 10)
        self.assertEqual(discount.discount_calc(), 10)

    def test_discount_fail(self):
        discount = Discount(100, -100)
        self.assertEqual(discount.discount_calc(), "Discount percentage cannot be less than 0 or greater than 100")


if __name__ == '__main__':
    unittest.main()
