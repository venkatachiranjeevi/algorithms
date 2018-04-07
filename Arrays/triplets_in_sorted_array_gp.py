__author__ = 'venkat'

def find_pair():
    li = [10,12, 4, 5, -9, 6]
    num = 3
    size = len(li)-1
    li = sorted(li)
    i=0
    while i < size:
        if li[i] + li[size] == num:
            print [li[i], li[size]]
            return
        elif li[i]+li[size] > num:
          size -= 1
        else:
            i +=1

# find


