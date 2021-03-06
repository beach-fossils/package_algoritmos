# -*- coding: utf-8 -*-
"""
Package dos algoritmos implementados em aula
Algoritmos Avançados de Bioinformática
"""

"""
Unit test: Trie
"""

import unittest
from trie import Trie


class test_Trie(unittest.TestCase):
    def setUp(self) -> None:
        self.pat = ["AGAGAT", "AGC", "AGTCC", "CAGAT", "CCTA", "GAGAT", "GAT", "TC"]
        self.trie = Trie()
        self.trie.trieFromPatterns(self.pat)


class test_TrieMethods(test_Trie):

    def test_prefixTrieMatch(self):
        x = self.trie.prefixTrieMatch("GAGATCCTA")
        y = "GAGAT"
        self.assertEqual(x, y)

    def test_trieMatches(self):
        x = self.trie.trieMatches("GAGATCCTA")
        y = ["(0, 'GAGAT')", "(2, 'GAT')", "(4, 'TC')", "(5, 'CCTA')"]
        for test, truth in zip(x, y):
            self.assertEqual(str(test), truth)

    # def test_printTrie(self):
    #     x = self.trie.printTrie()
    #     y = ["0 -> {'A': 1, 'C': 11, 'G': 19, 'T': 25}", "1 -> {'G': 2}",
    #          "2 -> {'A': 3, 'C': 7, 'T': 8}", "3 -> {'G': 4}", "4 -> {'A': 5}",
    #          "5 -> {'T': 6}", "6 -> {}", "7 -> {}", "8 -> {'C': 9}", "9 -> {'C': 10}",
    #          "10 -> {}", "11 -> {'A': 12, 'C': 16}", "12 -> {'G': 13}", "13 -> {'A': 14}",
    #          "14 -> {'T': 15}", "15 -> {}", "16 -> {'T': 17}", "17 -> {'A': 18}", "18 -> {}",
    #          "19 -> {'A': 20}", "20 -> {'G': 21, 'T': 24}", "21 -> {'A': 22}", "22 -> {'T': 23}",
    #          "23 -> {}", "24 -> {}", "25 -> {'C': 26}", "26 -> {}"]
    #     self.assertEqual(x, y)

if __name__ == '__main__':
    unittest.main()