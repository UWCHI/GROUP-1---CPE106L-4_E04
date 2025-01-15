"""
  LAB 03
  PROGRAMMING PROBLEM 01

  Add methods to the Student class that compare two Student objects. One method should test for equality.
  The other methods should support the other possible comparisons. In each case, the method returns the
  result of the comparison of the two students’ names.
"""


def __eq__(self, other):
        return self.name == other.name
class Student:
    def __init__(self, name, number=0):
        self.name = name
        self.scores = [0] * number


    def __ne__(self, other):
        return self.name != other.name

    def __lt__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return self.name <= other.name

    def __gt__(self, other):
        return self.name > other.name

    def __ge__(self, other):
        return self.name >= other.name

    def getName(self):
        return self.name

    def setScore(self, i, score):
        self.scores[i - 1] = score

    def getScore(self, i):
        return self.scores[i - 1]

    def getAverage(self):
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):
        return max(self.scores)

    def __str__(self):
        return "Name: " + self.name + "\nScores: " + " ".join(map(str, self.scores))

# User input for demonstration
name1 = input("Enter the name of the first student: ")
name2 = input("Enter the name of the second student: ")
name3 = input("Enter the name of the third student: ")

student1 = Student(name1, 5)
student2 = Student(name2, 5)
student3 = Student(name3, 5)

for i in range(1, 6):
    score = int(input(f"Enter score {i} for {student1.name}: "))
    student1.setScore(i, score)

for i in range(1, 6):
    score = int(input(f"Enter score {i} for {student2.name}: "))
    student2.setScore(i, score)

for i in range(1, 6):
    score = int(input(f"Enter score {i} for {student3.name}: "))
    student3.setScore(i, score)

print("\nComparing students based on their names:")
print(f"{student1.name} == {student2.name}: {student1 == student2}")
print(f"{student1.name} != {student2.name}: {student1 != student2}")
print(f"{student1.name} < {student2.name}: {student1 < student2}")
print(f"{student1.name} <= {student2.name}: {student1 <= student2}")
print(f"{student1.name} > {student2.name}: {student1 > student2}")
print(f"{student1.name} >= {student2.name}: {student1 >= student2}")

# Equality check
print(f"{student1.name} == {student3.name}: {student1 == student3}")

# Additional feature: Compare all three names for equality
all_equal = student1 == student2 == student3
print(f"Are all three student names equal? {all_equal}")

print("\nStudent details:")
print(student1)
print(student2)
print(student3)
