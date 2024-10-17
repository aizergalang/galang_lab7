name=(input('enter your name'))
section=(input('enter your section'))
prelim=float(input('enter your prelim grade'))

if(prelim<40 or prelim>100):
    print('error')
else:
    midterm=float(input('enter your midterm grade'))
    if(midterm<40 or midterm>100):
        print('error')    
    else:
        final=float(input('enter your final term grade'))
        if(final<40 or final>100):
            print('error')
        else:
            final_grade=(prelim*0.3333+midterm*0.3333+final*0.3333)
            print("your final grade this sem is",final_grade)
            
if final_grade >= 99: 
    grade_point = 1.00
    description = "Excellent"

elif final_grade >= 96:
    grade_point = 1.25
    description = "Outstanding"
    
elif final_grade >= 93:
    grade_point = 1.50 
    description = "Superior"
    
elif final_grade >= 90:
    grade_point = 1.75
    description = "Very Good"
    
elif final_grade >= 87:
    grade_point = 2.00
    description = "Good"

elif final_grade >= 84:
    grade_point = 2.25
    description = "Satisfactory"
    
elif final_grade >= 81:
    grade_point = 2.50
    description = "Fairly Satisfactory"
    
elif final_grade >= 78:
    grade_point = 2.75
    description = "Fair"
    
elif final_grade >= 75:
    grade_point = 3.00
    description = "Passed"

else:
    grade_point = 5.00
    description = "Failed"
    
print (f"Average: {final_grade:.0f}")
print (f"Description: {description}")