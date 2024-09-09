# string_tools.py

class StringTools:
    @staticmethod
    def to_uppercase(s):
        return s.upper()

    @staticmethod
    def to_lowercase(s):
        return s.lower()

    @staticmethod
    def reverse_string(s):
        return s[::-1]

    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]

    @staticmethod
    def count_vowels(s):
        vowels = 'aeiouAEIOU'
        return sum(1 for char in s if char in vowels)
