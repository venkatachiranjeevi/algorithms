__author__ = 'venkat'

li = [6, -2, -3, 2, 3]


def equli_brum():
    for i in range(len(li)):
        if i ==0:
            if(sum(li[i+1:])== 0):
                print "equlibrium position is " + str(i)
        elif i== len(li) -1:
            if(sum(li[:i]) == 0):
                print "equlibium position is" + str(i)
        else:
            if(sum(li[:i]) == sum(li[i+1:])):
                print "equlibru position is " + str(i)




def brium_wuli():
    total_sum = sum(li)
    left_sum = 0
    for i in range(len(li)):
        total_sum = total_sum - li[i]
        if left_sum == total_sum:
            print "equlibrium postions is " + str(i)
        left_sum = left_sum+ li[i]


brium_wuli()
equli_brum()