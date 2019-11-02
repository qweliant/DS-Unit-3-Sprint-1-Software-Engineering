import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_functions(self):
        """Test default product functions."""
        prod = Product('Test Product')
        prod.weight = 25
        prod.price = 34
        prod.flammability = 160
        self.assertEqual(prod.stealability(), 'very stealable.')
        self.assertEqual(prod.explode(), '...DOOOOOOM!!')


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        test_list = generate_products()
        self.assertEqual(len(test_list), 30)
        pass

    def test_legal_names(self):
        test_list = generate_products()
        # self.assertIn()
        pass


if __name__ == '__main__':
    unittest.main()
