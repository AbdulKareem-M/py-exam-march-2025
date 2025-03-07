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
    students = {}
    students[name] = marks
    
  def calculate_average(self, average):
    self.average = average
    self.average= sum(i for i in self.marks)/len(self.marks)
   
  def get_grade(self, grade):
    self.grade = grade
    if self.average >=90:
      self.grade = 'A'
    elif 80<=grade<=89:
      self.grade = 'B'
    elif 70<=grade<=79:
      self.grade = 'C'
    else:
      self.grade = 'D'
    
  def details(self):
    for i in self.students:
      print(i, self.get_grade(self.students[i]), self.get_grade())
      
obj = Student()
obj.details('Alice',[10,30,20])
    
      
       
  
  
  