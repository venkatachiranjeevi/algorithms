__author__ = 'venkat'

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def merger_interval(intervals, newInterval):
    num_of_intervals = len(intervals)
    if num_of_intervals is 0:
        return [newInterval]
    if newInterval.end < intervals[0].start:
        return [newInterval] + intervals
    if newInterval.start > intervals[-1].end:
        return intervals + [newInterval]
    i = -1
    j = -1
    left =0
    right = len(intervals)-1
    while left <= right:
        mid = left + (right-left)/2
        if intervals[mid].start < newInterval.start:
            left = mid
        elif intervals[mid].start > newInterval.start:
            right = mid
        else:
            i = mid
            break
        if mid == left + (right-left)/2:
            if intervals[right].start <= newInterval.start:
                i = right
                break
        if i == -1:
            i = left
        left = 0
        right = len(intervals)-1
        while left <= right:
            mid = left + (right-left)/2
            if intervals[mid].start < newInterval.end:
                left = mid
            elif intervals[mid].start > newInterval.end:
                right = mid
            else:
                j = mid
                break
            if mid == left + (right-left)/2:
                if intervals[right].start <= newInterval.end:
                    j = right
                break
        if j == -1:
            j = left
        if i == j:
            if max(intervals[i].start,newInterval.start) > min(intervals[i].end,newInterval.end):
                return intervals[:i+1]+[newInterval]+intervals[i+1:]
        if max(intervals[i].start,newInterval.start) > min(intervals[i].end,newInterval.end):
            i += 1
        if max(intervals[j].start,newInterval.start) > min(intervals[j].end,newInterval.end):
            j -= 1
        leftEnd = min(intervals[i].start, newInterval.start)
        rightEnd = max(intervals[j].end, newInterval.end)
        newInterval = Interval(leftEnd, rightEnd)
        intervals = intervals[:i] + [newInterval] + intervals[j+1:]
        return intervals
a = [ (1, 2), (3, 6) ]
b = [10,8]
c = [[1,3],[6,9]]
d = [2,5]
merger_interval(a,b)

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):

        num_of_intervals = len(intervals)
        if num_of_intervals is 0:
            return [new_interval]
        x_val = new_interval[0]
        x_limit =0
        while x_limit < num_of_intervals:
            if x_val >= intervals[x_limit][0] and x_val <=intervals[x_limit+1][0]:
                break
            x_limit += 1
        y_limit = x_limit
        y_val = new_interval[1]
        while y_limit < num_of_intervals:
            if y_val <= intervals[y_limit][1]:
                break
            y_limit += 1

        print  intervals[:x_limit] + [self.merge(intervals[x_limit:y_limit+1], new_interval)] + intervals[y_limit+1:]

    def merge(self, a, b):
        x_val = a[0][0] if a[0][0] <= b[0] else b[0]
        y_val = a[len(a)-1][1] if a[len(a)-1][1] >= b[1] else b[1]
        return [x_val, y_val]