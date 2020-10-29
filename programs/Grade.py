def calculator(homework,assessment,exam):
     total= (homework+assessment+exam)/175
     total=total*100
     return total

def grade(score):   
 if score>=70 :
    return"A"
 elif score>=60 :
    return"B"
 elif score>=50 :
    return"C"
 elif score>=40 :
    return"D"
 else :
    return"F"



#numberOfStudents = int(input('Enter how many students:'))

#for count in range (numberOfStudents):
 #name = input('enter students name:')
 #homeworkScore = int(input('Enter homework score /25:'))
 #assesmentScore = int(input('Enter assessment score /50:'))
 #examScore = int(input('Enter exam score /100:'))

 #percentage=int(calculator(homeworkScore,assesmentScore,examScore))
 #gradeAchieved = str(grade(percentage))
 #print(name, 'percentage is:', percentage,'% and achieved a grade of:', gradeAchieved)


    