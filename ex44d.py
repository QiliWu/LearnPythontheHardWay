class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

    def override(self):
        print "PARENT override()"

    def altered(self):
        print "PARENT altered()"


class Child(Parent):
    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered"
        #call super with arguments Child and self, then call the function altered in parent class
        super(Child,self).altered()
        print  "CHILD, AFTER PARENT altered"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()