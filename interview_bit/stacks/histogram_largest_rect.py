__author__ = 'venkat'

class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        st = []
        n = len(A)
        temp = res = 0
        i = 0
        while i < n:
            if len(st) == 0 or A[i] >= A[st[-1]]:
                st.append(i)
                i += 1
            else:
                top = st.pop()
                temp = A[top] *( i if len(st) == 0 else i-st[-1] -1 )
                if temp > res:
                    res = temp

        while len(st) != 0:
            top = st.pop()
            temp = A[top] * ( i if len(st) == 0 else i-st[-1] -1 )
            if temp > res:
                res = temp

        return res

print Solution().largestRectangleArea([6,1,5,4,5,3,7])



public class Solution {
	public int diffPossible(final List<Integer> A, int B) {

	    HashMap<Integer, Integer> hashMap = new HashMap<>();

	    for (int num : A) {
	        if (hashMap.containsKey(num)) {
	            int value = hashMap.get(num);
	            value++;
	            hashMap.put(num, value);
	        } else {
	            hashMap.put(num, 1);
	        }
	    }

	    for (int num : A) {

	        int n = B + num;

	        if (hashMap.containsKey(n)) {
	            if (num == n && hashMap.get(n) > 1)
	                return 1;
	            else if (num != n)
	                return 1;
	        }

	        n = num - B;

	        if (hashMap.containsKey(n)) {
	            if (num == n && hashMap.get(n) > 1)
	                return 1;
	            else if (num != n)
	                return 1;
	        }
	    }

	    return 0;


	}
}