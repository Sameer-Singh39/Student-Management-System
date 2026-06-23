#Student Management System
import json
import os

class Student:
    def __init__(self,student_id,student_name,age,marks):
        self.student_id=student_id
        self.student_name=student_name
        self.age=age
        self.marks=marks
      
        
    def display(self):
        print(f" {self.student_id:<15}{self.student_name:<15}{self.age:<10}{self.marks:<10}")  
        
    
class StudentManagementSystem:
    
    def Save_data(self):
        data=[]
        for student in self.students:
            data.append({
                "student_id" : student.student_id,
                "student_name" : student.student_name,
                "age" : student.age,
                "marks" : student.marks
            })
        with open("students.json","w")as file:
            json.dump(data,file,indent=4)  
            
    def load_data(self):
        if os.path.exists("students.json"):
            with open("students.json","r")as file:
                data=json.load(file)
                
            for s in data:
                student=Student(
                    s["student_id"],
                    s["student_name"],
                    s["age"],
                    s["marks"]
                )
                
                self.students.append(student)    
                    
    
    
    
    def __init__(self):
        self.students=[] 
        self.load_data()
        
    def add_student(self):
        student_id=int(input("Enter a student Id : "))
        student_name=input("Enter a student Name : ")
        age=int(input("Enter Student Age : "))
        marks=float(input("Enter Student Marks : "))   
        student=Student(student_id,student_name,age,marks) 
        self.students.append(student)  
        self.Save_data()
        print("Student added successfully")  
        
        
    def   ViewAll_Students(self):
        if not self.students:
            print("Not student found")
            return
        
        print(f" {'Student ID':<15}{'Student Name':<15}{'Age':<10}{'Marks':<10}")  
        print("-"*50)
        for student in self.students:
            student.display()
                   
                
    def search_student(self):
        sid=int(input("Enter a Student ID : "))
        for student in self.students:
            if student.student_id==sid:
                print("Student Found")
                student.display() 
                return 
        print("Student not fouund") 
                 
                
    def update_marks(self):   
        sid=int(input("Enter a student ID : "))
        for student in self.students:
            if student.student_id==sid:
                new_marks=float(input("Enter a new Marks :" ))
                student.marks=new_marks
                self.Save_data()
                print("Marks updated successfully")  
                return
        print("Student not found") 
      
        
    def delete_student(self):
        sid=int(input("Enter a student Id : "))
        for student in self.students:
            if student.student_id == sid:
                self.students.remove(student)  
                self.Save_data()
                print("Student Deleted Successfully")    
                return
        print("Student not Found")     
        
    def highest_marks_student(self):
        if not self.students:
            print("No students Available")  
            return
        top_student=max(self.students,key=lambda x:x.marks)  
        print("\nHighest Marks Student")
        top_student.display() 
        
sms=StudentManagementSystem()  

while True:
    print("\n====== Student Management System ===========")
    print("Press 1 for Add Student")
    print("Press 2 for View All Student")
    print("Press 3 for Search for a student using student ID")
    print("Press 4 for Update a student marks")
    print("Press 5 for Delete a student record")
    print("Press 6 for Display the student with the highest marks")
    print(" Press 7 for Exit the application")
    
    choice=int(input("Enter your choice "))   
    if choice==1:
     sms.add_student()
    elif choice == 2:
     sms.ViewAll_Students()
    
    elif choice == 3:
     sms.search_student() 
 
    elif choice == 4:
     sms.update_marks()    
    
    elif choice == 5:
     sms.delete_student()
    
    elif choice == 6:
     sms.highest_marks_student() 
 
    else:
     exit()                    
       
    
 
 
 
 
 
 
 
 
          