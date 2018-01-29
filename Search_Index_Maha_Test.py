# -*- coding: utf-8 -*-
#Search_Index_test - Author Maha

import unittest
import os
from final_exam_Maha import SearchIndex

class ScanDirectoryTest(unittest.TestCase):
    """tests SearchIndex class"""
    search_index = SearchIndex('/Users/Mahalidrisi/Desktop/STEVENS/3- Fall 2017/SSW 810/Homework/final_exam/')

    def test_init(self):
        """test init function"""

        result = {'sherlock1.txt': {'this': {0, 4, 20, 7}, 'is': {0, 4}, 
                                    'an': {0}, 'extra': {0}, 'line': {0}, 'with': {0, 4, 7}, 
                                    'occurrence': {0}, 'of': {0, 2, 4, 6, 10, 20}, 
                                    'word.': {0}, 'project': {2, 20, 6}, 'gutenbergs': {2}, 
                                    'the': {2, 4, 6, 10, 20}, 'adventures': {2, 10, 20}, 
                                    'sherlock': {2, 10, 20}, 'holmes': {2, 10, 20}, 'by': {2}, 
                                    'arthur': {2, 12}, 'conan': {2, 12}, 'doyle': {2, 12}, 
                                    'ebook': {4, 20, 14, 7}, 'for': {4}, 'use': {4, 6}, 
                                    'anyone': {4}, 'anywhere': {4}, 'at': {4, 7}, 
                                    'no': {4, 5}, 'cost': {4}, 'and': {4}, 'almost': {5}, 
                                    'restrictions': {5}, 'whatsoever': {5}, 'you': {5}, 
                                    'may': {5}, 'copy': {5}, 'it': {5, 6}, 'give': {5}, 
                                    'away': {5}, 'or': {5, 7}, 're': {6}, 'under': {6}, 
                                    'terms': {6}, 'gutenberg': {20, 6}, 'license': {6}, 'included': {6}, 'online': {7}, 
                                    'wwwgutenbergnet': {7}, 'title': {10}, 'author': {12}, 'posting': {14}, 
                                    'date': {14}, 'april': {14}, '18': {14}, '2011': {14}, '1661': {14}, 
                                    'first': {15}, 'posted': {15}, 'november': {15}, '29': {15}, '2002': {15}, 
                                    'language': {17}, 'english': {17}, 'start': {20}}}
        
        self.assertEqual(ScanDirectoryTest.search_index.dirc, '/Users/Mahalidrisi/Desktop/STEVENS/3- Fall 2017/SSW 810/Homework/final_exam/')
        self.assertEqual(ScanDirectoryTest.search_index.dd, result) 
        self.assertEqual(ScanDirectoryTest.search_index.number_of_words, 104)
        self.assertEqual(len(ScanDirectoryTest.search_index.distinct_words), 62)
        self.assertEqual(ScanDirectoryTest.search_index.number_of_files, 1)
        

    def test_lookup(self):
        """test lookup function"""
        ScanDirectoryTest.search_index.lookup('Ebook')
        self.assertEqual(ScanDirectoryTest.search_index.lookup('Ebook'), [['sherlock1.txt', [4, 7, 14, 20]]])
        self.assertEqual(ScanDirectoryTest.search_index.lookup('maha'), [])

    def test_scan_directory(self):
        """test scan_directory function"""
        ScanDirectoryTest.search_index.dirc = 'wrong directory'
        self.assertRaises(FileNotFoundError, ScanDirectoryTest.search_index.scan_directory) #test invalid directory
    
    def test_summary(self):
        """test summary function"""
        self.assertEqual(ScanDirectoryTest.search_index.summary(), 'read 104 words from 1 files finding 62 distinct words')

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)