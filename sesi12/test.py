#for init.py

from fractions import Fraction
# import my_app
import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
    
    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)
    
    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)
    

# class MyTestCase(unittest.TestCase):

#     def setUp(self):
#         my_app.app.testing = True
#         self.app = my_app.app.test_client()

    # def test_home(self):
    #     result = self.app.get('/')
    #     # Make your assertions

if __name__ == '__main__':
    unittest.main()




# # def test_sum():
# #     assert sum([1, 2, 3]) == 6, "Should be 6"

# # def test_sum_tuple():
# #     assert sum((1, 2, 3)) == 6, "Should be 6"

# # if __name__ == "__main__":
# #     test_sum()
# #     test_sum_tuple()
# #     print("Everything passed")

# #-------------------------------------------

# import unittest


# class TestSum(unittest.TestCase):

#     # def test_sum(self):
#     #     self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

#     # def test_sum_tuple(self):
#     #     self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

#     #pytest
#     def test_sum(self):
#         assert sum([1, 2, 3]) == 6, "Should be 6"

#     def test_sum_tuple(self):
#         assert sum((1, 2, 2)) == 6, "Should be 6"

# if __name__ == '__main__':
#     unittest.main()