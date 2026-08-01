class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1 
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
        return True  






"""
Pointer Positions
L --------->
<--------- R

Algorithm
1. Start Left at beginning.
2. Start Right at end.
3. Skip non-alphanumeric characters.
4. Compare lowercase characters.
5. If different -> False.
6. If same -> Move both pointers.
7. Repeat until pointers cross.
8. Return True.

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Two Pointer Pattern
        # Left starts from beginning
        # Right starts from end
        left = 0
        right = len(s) - 1

        # Continue until both pointers meet/cross.
        # If all comparisons before this are equal,
        # then the string is a palindrome.
        while left < right:

            # Ignore characters that are NOT letters or digits.
            # Move only the left pointer and check again.
            if not s[left].isalnum():
                left += 1
                continue

            # Ignore characters that are NOT letters or digits.
            # Move only the right pointer and check again.
            if not s[right].isalnum():
                right -= 1
                continue

            # Compare both characters after converting them
            # to lowercase (case-insensitive comparison).
            # If they don't match, it's NOT a palindrome.
            if s[left].lower() != s[right].lower():
                return False

            # Characters matched.
            # Move both pointers inward
            # and compare the next pair.
            left += 1
            right -= 1

        # Checked every valid character without finding
        # a mismatch, so it IS a palindrome.
        return True

Problem:
Valid Palindrome

Pattern:
Two Pointers

Key Idea:
Start one pointer from each end.
Skip invalid characters.
Compare lowercase letters.
Move inward until pointers cross.

Why this pattern?
Checking from both ends avoids extra space and keeps the solution O(n).

Time:
O(n)

Space:
O(1)

Mistakes I made:
1. Used nested loops instead of pointers.
2. Tried sorting (doesn't preserve order).
3. Forgot right starts at len(s)-1.
4. Used return instead of continue.
5. Forgot to move pointers after comparison.
6. Didn't know isalnum() is a method.
7. Didn't know lower() needs ().
"""