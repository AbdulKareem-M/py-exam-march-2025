'''
 Create a Student class with attributes name and marks (list of subject marks).
 The class should have:- A method calculate_average()
 that returns the average marks.- A method get_grade() 
 that assigns a grade based on average marks:
  - 90 and above -> 'A'
  - 80-89 -> 'B'
  - 70-79 -> 'C'
  - Below 70 -> 'D'- Store multiple students in a dictionary
  where the student's name is the key.- 
  Use loops to iterate over student data and print their grades.
 Sample Input:
 students = {
    "Alice": [85, 90, 88],
    "Bob": [78, 65, 72],
    "Charlie": [95, 92, 97]
 }
 Expected Output:
 Alice: Grade B
 Bob: Grade C
 Charlie: Grade A
 '''
 
 
class Student:
  def details(self,name, marks):
    self.name = name
    self.marks = marks
    
  def calculate_average(self):
    self.average= sum(i for i in self.marks)/len(self.marks)
   
  def get_grade(self, average):
    average = self.average
    if average > 90:
      return 'A'
    elif 80<=average<=89:
      return 'B'
    elif 80<=average<=89:
      return 'C'
    else:
      return 'D'
  
  
  