__author__ = 'venkat'


class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


def find_next_greater():
    li =  [11,3,2,13,21]
    st = Stack()
    st.push(li[0])
    i =1
    while(i<len(li)):
        next_ele = li[i]
        if(st.size() > 0):
            ele = st.pop()
            while ele < next_ele:
                print "next grreater is " + str(next_ele) + " for element is " + str(ele)
                if st.size() ==0:
                    break
                ele = st.pop()
            if ele >next_ele:
                st.push(ele)

        st.push(next_ele)
        i = i+1
    while st.size() != 0:
        ele  = st.pop()
        print "next greater is -1 for element is " + str(ele)

find_next_greater()