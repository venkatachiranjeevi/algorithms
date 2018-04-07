__author__ = 'venkat'



def find_len():
    li =   [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]

    li_len = len(li)
    i =0
    while(li[i]< li[i+1] and i < li_len):
        i = i+1
    key = li[i+1]
    while(i> 0 and li[i-1]> key):
        i = i-1
    print i
    j = li_len -1
    while(li[j] > li[j-1]):
        j = j-1
    j = j-1
    key = li[j]
    while j+1 < len and li[j+1] < key:
        j = j+1
    print j

find_len()