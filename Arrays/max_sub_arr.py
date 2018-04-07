__author__ = 'venkat'

li = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
k =4
max = li [0]
max_arr = []
j =1
while(j< k):
    if(li[j]> max):
        max = li[j]
    j = j+1
max_arr.append(max)

j =k
while(j<len(li)):
    if(max < li[j]):
        max = li[j]
    max_arr.append(max)
    j = j+1

print max_arr