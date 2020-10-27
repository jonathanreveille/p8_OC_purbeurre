from django.test import TestCase

from products.forms import SearchedProductForm

class SearchedProductFormTest(TestCase):

    def setUp(self):
        self.query = SearchedProductForm()

    def test_unvalid_data(self):
        self.assertFalse(self.query.is_valid())
    
    def test_valid_data(self):
        self.query.query_search = "pizza"
        self.assertEquals(self.query.query_search, "pizza")







    # def test_false_is_false(self):
    #     print("Method: test_false_is_false.")
    #     self.assertFalse(False)

    # def test_false_is_true(self):
    #     print("Method: test_false_is_true.")
    #     self.assertTrue(True)

    # def test_one_plus_one_equals_two(self):
    #     print("Method: test_one_plus_one_equals_two.")
    #     self.assertEqual(1 + 1, 2)