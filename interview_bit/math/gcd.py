__author__ = 'venkat'

class Solution:
    def gcd(self, n1, n2):
        if abs(n1) > 2 **31 or abs(n2) > 2 **31:
            return 0
        if n1 is 0 or n2 is 0:
            return max(n1, n2)
        lcd = self.lcd(n1,n2)
        return (n1 * n2)/ lcd

    def lcd(self, n1, n2):
        m = min(n1,n2)

        while(1):
            if m%n1 is 0 and m%n2 is 0:
                return m
            m +=1
    def gcda(self, a, b):
        if (b == 0):
            return a
        else:
            return self.gcd(b, a%b)

print Solution().gcda(4, 8)