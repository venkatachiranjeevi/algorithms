__author__ = 'venkat'

class Parent(object):

    def __init__(self):
        self.x = 10
        self.y = 30

    def altered(self):
        print (self.x)
        print "PARENT altered()"

class Child(Parent):

    # def __init__(self):
    #     super(Child, self).__init__()
    #     self.x = 10
    #     self.y = 30

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        # super(Child, self)
        print "CHILD, AFTER PARENT altered()"

# dad = Parent()
son = Child()

# dad.altered()
son.altered()