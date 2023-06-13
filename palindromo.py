def palindrome(s):
    return s == s[::-1]
s = "radar"
ans = palindrome(s)

def palindromo(cadena):
    if len(cadena)<2:
        return True
    if cadena [0] != cadena[-1]:
        return False

    return palindromo(cadena[1:-1])

c1= "neuquen"

import unittest
class TestPalindrome(unittest.TestCase):

    def test_palindromo(self):
        result = palindromo('menem')
    def test_palindrome1(self):
        result = palindromo('Arenera') 
    def test_palindrome2(self):
        result = palindromo('Solos')
    def test_palindrome4(self):
        result = palindromo('reconocer')
       
    def test_palindromoa(self):
        result = palindrome('menem')
    def test_palindromeb(self):
        result = palindrome('Arenera') 
    def test_palindromec(self):
        result = palindrome('Solos')
    def test_palindromed(self):
        result = palindrome('reconocer') 

if __name__ == '__main__':
    unittest.main()