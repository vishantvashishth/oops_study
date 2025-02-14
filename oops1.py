#initiate a  class

class Employee:
    #special method/magic method/dunder method-constructor
    def __init__(self):
        print("started execcuting data")
        self.id=123
        self.salary=50000
        self.designation="SDE"
        print("End")


    def travel(self,destination):
        print(f"He will be travelling to {destination} ")



#creating an object or instance of class
sam=Employee()
print(sam.salary)
print(sam.id)


# calling a method
sam.travel("France")
print(type(sam))