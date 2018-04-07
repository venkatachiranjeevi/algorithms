__author__ = 'venkat'

li1 = [12, 4, 78, 90, 45, 23, 90]
li2 = [20, 4, 1, 2, 3, 4, 2, 10]
def method():
    li = [40, 30, 20, 10]
    i =0
    j = len(li)-1
    while(i<j):

        while(li[i] > li [i+1] and i == len(li) -1):
            i = i+1

        if(i == len(li) -1):
            i =0

        while(li[j] > li [j-1]):
            j = j-1
        if(j ==0):
            j = len(li)-1

        index1 = i
        index2 = j
        while(li[i]< li[i+1] and i< j and i == len(li) -1):
            i = i+1
            if i == len(li) -1:
                break
        while(li[j] < li [j-1] and i<j):
            j = j-1
            if j ==0:
                break
        if(i == j):
            print li[index1:index2+1]
            break

def method2():
    li = [12, 4, 78, 90, 45, 23, 90]
    inc = [1, 0, 0, 0, 0, 0, 0]
    dec = [0,0,0,0,0,0,1]
    inc[0] = 1
    dec [len(li)-1] = 1
    i =1
    while(i< len(li)):
        if(li[i] > li[i-1]):
            inc[i] = inc[i-1] + 1
        else:
            inc[i] = 1
        i = i+1
    j = len(li)-2
    while(j >= 0):
        if(li[j] > li[j+1]):
            dec[j] = dec[j+1] +1
        else:
            dec[j] = 1
        j= j-1
    max = inc[0] + dec[0] -1
    i =1
    while(i< len(li)):
        if((inc[i] + dec[i]) -1 > max):
            max = inc[i] + dec[i] -1
        i = i+1
    print max

method2()