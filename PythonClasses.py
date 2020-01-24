class myClass(): #"master" class
    def method1(self):
        print("myClass method1")
    def method2(self, someString):
        print("myClass method2 " + someString)

class anotherClass(myClass): #class inherits from myClass
    def method1(self):
        myClass.method1(self) #encompasses myClass.method1() as well as printing "anotherClass method1"
        print("anotherClass method1")
    def method2(self, someString):
        print("anotherClass method2 ")


def main():
    c = myClass() #instantiate myClass
    c.method1()
    c.method2("This is a string")

    c2 = anotherClass() #instantiate anotherClass
    c2.method1() #prints 2 lines because this method inherits from myClass and prints its own line
    c2.method2("This is a string") #prints a single line because it does not inherit from myClass and only prints its own line
if __name__ == "__main__":
    main()