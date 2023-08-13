import unittest
from word_search import (
    is_isogram,
    is_palindrome,
    is_semordnilap,
    has_maximum_length,
    has_minimum_length,
    starts_with,
    ends_with,
    contains_only,
    apply_search_rules,
    parse_arguments,
)


class WordSearchTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Read the contents of the wordlist.txt file and store them in cls.word_list
        with open("wordlist.txt", "r") as file:
            cls.word_list = [word.strip() for word in file]

    def setUp(self):
        self.args = parse_arguments()

    def test_is_isogram(self):
        self.assertTrue(is_isogram("word"))
        self.assertFalse(is_isogram("hello"))
        self.assertTrue(is_isogram("python"))
        self.assertTrue(is_isogram(""))  # Empty string is an isogram

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome(""))  # Empty string is a palindrome

    def test_is_semordnilap(self):
        word_list = ["live", "evil", "god", "dog"]
        self.assertTrue(is_semordnilap("live", set(word_list)))
        self.assertTrue(is_semordnilap("dog", set(word_list)))
        self.assertFalse(is_semordnilap("live", set(["hello", "world"])))
        self.assertFalse(is_semordnilap("live", set([])))  # Empty word list should always return False

    def test_has_maximum_length(self):
        self.assertTrue(has_maximum_length("word", 5))
        self.assertFalse(has_maximum_length("hello", 3))
        self.assertTrue(has_maximum_length("python", 10))
        self.assertTrue(has_maximum_length("", 5))  # Empty string should always return True

    def test_has_minimum_length(self):
        self.assertTrue(has_minimum_length("word", 3))
        self.assertFalse(has_minimum_length("hello", 10))
        self.assertTrue(has_minimum_length("python", 5))
        self.assertFalse(has_minimum_length("", 1))  # Empty string should always return False

    def test_starts_with(self):
        self.assertTrue(starts_with("banana", "ba"))
        self.assertFalse(starts_with("hello", "ba"))
        self.assertTrue(starts_with("python", "py"))
        self.assertFalse(starts_with("", "ba"))  # Empty string should always return False

    def test_ends_with(self):
        self.assertTrue(ends_with("banana", "na"))
        self.assertFalse(ends_with("hello", "na"))
        self.assertTrue(ends_with("python", "on"))
        self.assertFalse(ends_with("", "na"))  # Empty string should always return False

    def test_contains_only(self):
        self.assertTrue(contains_only("bad", "abcde"))
        self.assertFalse(contains_only("hello", "abcde"))
        self.assertTrue(contains_only("decade", "abcde"))
        self.assertTrue(contains_only("", "abcde"))  # Empty string contains only the specified characters

    def test_apply_search_rules(self):
        word_list = ["hello", "banana", "python", "bad", "dab", "racecar"]

        query = "class=palindrome"
        expected_result = ["racecar"]
        self.assertEqual(apply_search_rules(query, word_list), expected_result)

        query = "maxlength=5 minlength=3"
        expected_result = ["hello", "bad", "dab"]
        self.assertEqual(apply_search_rules(query, word_list), expected_result)

        query = "startswith=ba"
        expected_result = ["banana", "bad"]
        self.assertEqual(apply_search_rules(query, word_list), expected_result)

        query = "endswith=on"
        expected_result = ["python"]
        self.assertEqual(apply_search_rules(query, word_list), expected_result)

        query = "containsonly=abcde"
        expected_result = ["bad", "dab"]
        self.assertEqual(apply_search_rules(query, word_list), expected_result)

        query = "class=isogram"
        expected_result = ["hello", "banana", "racecar"]
        self.assertNotEqual(apply_search_rules(query, word_list), expected_result)

        query = "class=semordnilap"
        expected_result = ["bad", "dab"]
        self.assertEqual(apply_search_rules(query, word_list), expected_result)




if __name__ == "__main__":
    unittest.main()