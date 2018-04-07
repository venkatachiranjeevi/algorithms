__author__ = 'venkat'


li = [2, 8, 10, 15, 16, 30, 32, 64]

j =1
while(j < len(li)-1):
    i = j-1
    k = j+1
    while(i>=0 and k<len(li)):
        while(li[j]% li[i] ==0 and li[k] % li[j] == 0 and li[j]/li[i] == li[k]/li[j]):
            print "triplets are " + str(li[i])+ "  ," + str(li[j])+ "  ," + str(li[k])
            i = i-1
            k = k+1
        if(li[j] % li[i] == 0 and li[k] %li[j] ==0 ):
           if li[j]/ li[i] < li[k]/li[j]:
               i = i-1
           else:
                k = k+1

        elif li[j] %li[i] ==0:
            k = k + 1
        else:
            i = i-1
    j = j+1