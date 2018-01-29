# -*- coding: utf-8 -*-
#Search_Index - Author Maha

import os
from collections import defaultdict

class SearchIndex:
    """reads all .txt files in a directory and creates a Search index [files, words, disticnt lines]"""

    def __init__(self, dirc):
        """intilize SearchIndex instance"""
        self.dirc = dirc
        self.dd = defaultdict(lambda: defaultdict(set)) #dict of dict - key: file name, value: {key: word, value: distinct lines}
        self.number_of_words = 0
        self.distinct_words = set()
        self.number_of_files = 0
        self.scan_directory()

    def scan_directory(self):
        """scan dirc for .txt files and call scan file func, returns a """
        try:
            files = os.listdir(self.dirc)
        except FileNotFoundError:
            raise FileNotFoundError('directory not found')
        else:
            for f in files:
                if f.lower().endswith('.txt'):
                    self.number_of_files += 1
                    self.scan_file(f)
            return self.dd

    def scan_file(self, f):
        """ reads given file and stores [file name, words, and number of lines]"""
        try:
            fp = open(f, 'r')
        except FileNotFoundError:
            raise FileNotFoundError('unable to open the file')
        else:
            with fp:
                for  offset, line in enumerate(fp):
                    self.number_of_words += len(line.split()) #count number of words read
                    for word in line.split():
                        self.distinct_words.add(word.lower()) #add words to distinct_words set
                        self.dd[f][word.lower()].add(offset)

    def lookup(self, target):
        """returns sorted list the file name and number of lines were given taget is found"""
        search_result = []
        for f in self.dd:
            for word, lines in self.dd[f].items():
                if word == target.lower():
                    search_result.append([f, sorted(lines)])
        return sorted(search_result)

    def summary(self):
        """returns number of read words, files, and distinct words."""
        return 'read {} words from {} files finding {} distinct words'.format(self.number_of_words, self.number_of_files, len(self.distinct_words))

def main():
    """main function to create a SearchIndex instance and search for words."""
    s = SearchIndex('/Users/Mahalidrisi/Desktop/STEVENS/3- Fall 2017/SSW 810/Homework/final_exam/final_exam_Maha')
    print('Summary:', s.summary())
    print('lookup results for extra:', s.lookup('extra'))
    print('lookup results for Holmes:', s.lookup('Holmes'))
    print('lookup results for Ebook:', s.lookup('Ebook'))
    print('lookup results for Not_a_word:', s.lookup('Not_a_word'))
    
if __name__ == '__main__':
    main()
