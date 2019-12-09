import unittest
import pandas as pd
import numpy as np
import sys
sys.path.append("../code/htmlserver")
import datahandle as dh

class TestDataHandle(unittest.TestCase):
    
    def test_get_raw_useful_listing_df(self):
        self.assertEqual(dh.get_raw_useful_listing_df().shape[1], 39)

    def test_primary_search_limit(self):
        self.assertEqual(len(dh.primary_recommend_search("98105", None, None, \
        None, None, None, None, None, None, None, None, None, None, \
        None, None, 10)), 10)

    def test_basic_search_limit(self):
        self.assertEqual(len(dh.basic_recommend_search("98105", None, None,\
        None, 20)), 20)

    def test_primary_search_zipcode(self):
        df = dh.primary_recommend_search("98105", None, None, \
        None, None, None, None, None, None, None, None, None, None, \
        None, None, 10)
        for index, row in df.iterrows():
            self.assertEqual(row['zipcode'], "98105")
    
    def test_primary_search_accommodates(self):
        df = dh.primary_recommend_search("98105", 2, None, \
        None, None, None, None, None, None, None, None, None, None, \
        None, None, 10)
        for index, row in df.iterrows():
            self.assertGreaterEqual(row['accommodates'], 2)
        
    def test_primary_search_price(self):
        df = dh.primary_recommend_search("98105", None, "$100", \
        None, None, None, None, None, None, None, None, None, None, \
        None, None, 10)
        for index, row in df.iterrows():
            self.assertLessEqual(row['price'], "$100")
    
    def test_primary_search_rating(self):
        df = dh.primary_recommend_search("98105", None, None, \
        80, None, None, None, None, None, None, None, None, None, \
        None, None, 10)
        for index, row in df.iterrows():
            self.assertGreaterEqual(row['review_scores_rating'], 80)

    def test_primary_search_super_host(self):
        df = dh.primary_recommend_search("98105", None, None, \
        None, True, None, None, None, None, None, None, None, None, \
        None, None, 10)
        for index, row in df.iterrows():
            self.assertTrue(row['host_is_superhost'])

if __name__ == '__main__':
    unittest.main()