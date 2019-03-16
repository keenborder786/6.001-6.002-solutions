# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 14:36:17 2018

@author: MMOHTASHIM
"""

def marks_students(marks):
    x=()
    y=()
    z=()
    for t in marks:
         x=x+(t[0],)
         y=y+(t[1],)
         z=z+(t[2],)
    min_marks=min(x)
    max_marks=max(x)
    num_students=len(x)
    return min_marks,max_marks,num_students
Student_marks=((53,"Mohtashim",23),(73,"Ali",24),(84,"Ahmed",37))
(x,y,z)=marks_students(Student_marks)
print("The maximum marks are:",x,"The maximum marks are:",y,"The number of students in class are",z)









    
    