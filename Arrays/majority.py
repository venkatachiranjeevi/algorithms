__author__ = 'venkat'

def find_maj_candidate(li):
    maj_index = 0
    count = 1
    i = 0
    for i in range(1,len(li)):
        if li[maj_index] == li[i]:
            count += 1
        else:
            count -=1
        if count == 0:
            maj_index = i
            count = 1
    return li[maj_index]

def is_majority(li, ele):
    count = 0
    for i in range(len(li)):
        if li[i] == ele:
            count += 1
    if count >len(li)/2:
        print ele
    else:
        print "no such element"

def main():
    li = [3, 3, 4, 2, 4, 5, 2, 5, 6]
    n = find_maj_candidate(li)
    is_majority(li, n)


main()