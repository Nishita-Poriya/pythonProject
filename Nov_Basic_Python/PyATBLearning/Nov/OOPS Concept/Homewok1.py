'''
Task 1 - Create a Class PyATB , 5 Attributes, 3 Functions/Methods
Use PC - to set the value of the attributes
create a Print student information method/function
'''

class PyATB:
    # Parameterized Constructor to set values
    def __init__(self, name, age, roll_no, grade, city):
        self.name = name  # Attribute 1: Name
        self.age = age  # Attribute 2: Age
        self.roll_no = roll_no  # Attribute 3: Roll Number
        self.grade = grade  # Attribute 4: Grade
        self.city = city  # Attribute 5: City

    # Method 1: Print student information
    def print_student_info(self):
        print("----- Student Information -----")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Grade: {self.grade}")
        print(f"City: {self.city}")

    # Method 2: Update student's grade
    def update_grade(self, new_grade):
        self.grade = new_grade
        print(f"Grade updated to: {self.grade}")

    # Method 3: Change city
    def change_city(self, new_city):
        self.city = new_city
        print(f"City updated to: {self.city}")


# Example usage
student1 = PyATB("John Doe", 20, "101", "A", "New York")  # Setting attributes via PC
student1.print_student_info()  # Display student details

student1.update_grade("A+")  # Updating grade
student1.change_city("San Francisco")  # Changing city

student1.print_student_info()  # Display updated details
