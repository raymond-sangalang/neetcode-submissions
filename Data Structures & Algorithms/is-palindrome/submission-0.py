class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert string into desired All alphanumeric readable input
        alnum_str = ''.join(char.lower() for char in s if char.isalnum())

        # compare ascending order to its descending order
        return alnum_str == alnum_str[::-1]