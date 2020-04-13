in_ = [4, 1, 2, 1, 2, 5,5]


def singled_number(in_):
    in_.sort()
    x = in_
    i =0
    while i < (len(x)-1):
        if x[i] != x[i+1]:
            return x[i]
        i = i+2
    return x[i]


print(singled_number(in_))
