import unittest

from passphrase import passphrase_contains_no_duplicates, passphrase_contains_no_anagrams, \
    count_passphrases_without_duplicates, count_valid_passphrases


class TestPassphraseFunctions(unittest.TestCase):
    def test_string_no_duplication(self):
        self.assertEqual(True, passphrase_contains_no_duplicates("aa bb cc"))

    def test_invalid_word_duplication(self):
        self.assertEqual(False, passphrase_contains_no_duplicates("aa bb aa"))

    def test_string_with_no_anagram(self):
        self.assertEqual(True, passphrase_contains_no_anagrams("aa ab ac ad"))

    def test_string_with_anagram(self):
        self.assertEqual(False, passphrase_contains_no_anagrams("aa ab ac ba"))

    def test_get_number_without_duplicates_from_input_text(self):
        self.assertEqual(451, count_passphrases_without_duplicates("input.txt"))

    def test_get_number_valid_passphrases_from_input_text(self):
        self.assertEqual(223, count_valid_passphrases("input.txt"))
