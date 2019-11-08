#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_num_products(self):
        '''
        Checks that number of default products created is 30
        '''

        prods = generate_products()
        self.assertEqual(len(prods), 30)

    def test_legal_names(self):
        '''
        Checks that the product names are named correctly
        '''

        prods = generate_products()

        adjs = []
        nouns = []

        for i in range(len(prods)):
            '''
            Creates a list of all nouns and adjectives used
            '''
            nameList = prods[i].name.split(' ')
            adjs.append(nameList[0])
            nouns.append(nameList[1])

        for i in range(len(adjs)):
            self.assertIn(adjs[i], ADJECTIVES)

        for i in range(len(nouns)):
            self.assertIn(nouns[i], NOUNS)


if __name__ == '__main__':
    unittest.main()
