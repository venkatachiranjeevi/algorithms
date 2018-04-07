__author__ = 'venkat'

class Solution:

    def hotel(self, arrive, depart, K):
        events = [(t, 1) for t in arrive] + [(t, 0) for t in depart]
        events = sorted(events)

        people = 0

        for x in events:
            if x[1] == 1:
                people += 1
            else:
                people -= 1

            if people > K:
                return 0

        return 1


a = [1, 3, 5]
b = [2, 6 ,8]

print Solution().hotel(a, b, 1)