__author__ = 'customfurnish'



def longestPalSubstr(string):
    maxLength = 1

    start = 0
    length = len(string)

    # One by one consider every character as center point of
    # even and length palindromes
    for i in xrange(1, length):
        # Find the longest even length palindrome with center
    # points as i-1 and i.
        low = i - 1
        high = i
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1

        # Find the longest odd length palindrome with center
        # point as i
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1

    print "Longest palindrome substring is:",
    print string[start:start + maxLength]

    return maxLength

# Driver program to test above functions
# string = "forgeeksskeegfor"
# print "Length is: " + str(longestPalSubstr(string))

class Solution:

    def longestPalindrome(self, A):
        n = len(A)
        start = 0
        maxLength = 1
        for x in xrange(1,n):
            low = x -1
            high = x
            while low >=0 and high < n and A[low] == A[high]:
                if high-low+1 > maxLength:
                    start = low
                    maxLength = high-low+1
                low -= 1
                high += 1

            low = x -1
            high = x + 1
            while low >=0 and high < n and A[low] == A[high]:
                if high-low+1 > maxLength:
                    start = low
                    maxLength = high-low+1
                low -= 1
                high += 1

        return A[start:start + maxLength]

print Solution().longestPalindrome("")