__author__ = 'venkat'

class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        n = len(A)
        st = []
        for x in A:
            if x == '(' or x == '{' or x == '[':
               st.append(x)
            else:
                if len(st) == 0:
                    return 0
                elif (st[-1] == '(' and x == ')') or (st[-1] == '[' and x == ']') or (st[-1] == '{' and x == '}'):
                    st.pop()
                else:
                    return 0

        if len(st) != 0:
            return 0
        return 1

print Solution().isValid("()[]{}")