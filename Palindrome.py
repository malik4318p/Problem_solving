class Solution:
    def isPalindrome(self, x: int) -> bool:
        is_palindrome = True
        length = len(x)
        num=str(x)
        for i in range (length//2):
            if(num[i]!= num[-i+1]):
                is_palindrome=False
                break
        return is_palindrome