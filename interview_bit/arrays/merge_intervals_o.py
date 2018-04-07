__author__ = 'venkat'

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        num_of_intervals = len(intervals)
        if num_of_intervals is 0:
            return [newInterval]
        if newInterval.end < intervals[0].start:
            return [newInterval] + intervals
        if newInterval.start > intervals[-1].end:
            return intervals + [newInterval]

        if newInterval.start <= intervals[0].start:
            intervals = [newInterval] + intervals
        elif newInterval.start >= intervals[-1].start:
            intervals += [newInterval]
        else:
            for x in range(num_of_intervals -1):
                if newInterval.start >= intervals[x].start and newInterval.start < intervals[x+1].start:
                    intervals = intervals[:x+1] + [newInterval] + intervals[x+1:]
                    break
        li = []
        li.append(intervals[0])
        i =1
        while i< num_of_intervals+1:
            temp = []
            ref = li.pop()
            temp.append(ref)
            temp.append(intervals[i])
            res = self.merge(temp)
            li += res
            i +=1
        # for x in range(num_of_intervals):
        #     li.append(self.merge(intervals[x:x+2])[0])

        return li

    def merge(self, list):
        a1 = (list[0].start, list[1].start)
        a2 = (list[0].end, list[1].end)

        max_1 = max(a1)
        min_2 = min(a2)
        if max_1 > min_2:
            return list
        max_1 = list[0].start if list[0].start < list[1].start else list[1].start
        max_2 = list[1].end if list[1].end > list[0].end else list[0].end
        return [Interval(max_1, max_2)]




x = Solution()
a = [ [1,2],[3,5],[6,7],[8,10],[12,16] ]
b =  [4,9]

def cal():
    li = []
    for i in a:
        li.append(Interval(i[0], i[1]))
    new_interval = Interval(b[0], b[1])
    x = Solution()
    result = x.insert(li, new_interval)
    print "sad"
cal()









