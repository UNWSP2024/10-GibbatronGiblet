# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes:
# name, ID number, department, and job title.

# Once you have written the class, write a program that creates
# three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, \
# then display the data for each employee on the screen.

class Employee:
    def __init__(self, name, ID, department, job):
        self.name = name
        self.id = ID
        self.department = department
        self.job = job

    def display(self):
        intro_blurb = f'Hello I am {self.name} from {self.department} and I work as one of the {self.job}s.'
        print(intro_blurb)

def main():
    employee1 = Employee("Susan Meyer",47899,"Accounting","Vice President")
    employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
    employee1.display()
    employee2.display()
    employee3.display()

main()


#This program was written on 11/6/25 by Logan Gibson
#Its name is "Employee Directory"