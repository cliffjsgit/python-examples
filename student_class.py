#definition of the superclass Person starts here
class Person:
    # initializing the variables
    name = ""
    age = 0

    # defining constructor
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    # defining class methods
    def showName(self):
        print(self.name)

    def showAge(self):
        print(self.age)
#end of superclass Person definition


#definition of subclass Student starts here
#Student is the subclass and Person is the superclass
class Student(Person):
    studentId = ""

    def __init__(self, studentName, studentAge, studentId):
        #calling the superclass constructor and sending values of attributes
        Person.__init__(self, studentName, studentAge)
        self.studentId = studentId

    def getId(self):
        #returns the value of student id
        return self.studentId
#end of subclass Student definition



###########################################################
## Test the Person class
###########################################################
## The main function.
def main():
    print('Create a Person ...')
    # create an object of the superclass Person
    person1 = Person("Richard", 23)

    #call member methods of the objects
    person1.showName()
    person1.showAge()

    # create an object of the subclass Student
    print('Create a Student ...')
    student1 = Student("Max", 22, "102")
    student1.showName()
    student1.showAge()
    print(student1.getId())


# Call the main function.
if __name__ == '__main__':
    main()
