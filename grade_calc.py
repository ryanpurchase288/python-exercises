mathsMark = int(input("Please Enter maths mark:"))
chemMark = int(input("Please Enter chemistry mark:"))
physMark = int(input("Please Enter physics mark:"))

average=(mathsMark+chemMark+physMark)/3
grade="You failed"

if average>=70 :
    grade ="A"
elif average>=60 :
    grade="B"
elif average>=50 :
    grade="C"
elif average>=40 :
    grade="D"

print("Your percentage score is: ",average,"%")
print("You scored a grade of: ",grade)
