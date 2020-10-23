digit_1=float(input('Please enter the digit 1:'))
digit_2=float(input('Please enter the digit 2:'))
digit_3=float(input('Please enter the digit 3:'))
digit_4=float(input('Please enter the digit 4:'))
digit_5=float(input('Please enter the digit 5:'))
digit_6=float(input('Please enter the digit 6:'))
digit_7=float(input('Please enter the digit 7:'))
digit_8=float(input('Please enter the digit 8:'))
digit_9=float(input('Please enter the digit 9:'))
digit_10=float(input('Please enter the digit 10:'))
digit_11=float(input('Please enter the digit 11:'))
digit_12=float(input('Please enter the digit 12:'))
checkNum=0

variables = [digit_1,digit_2,digit_3,digit_4,digit_5,digit_6,digit_7,digit_8,digit_9,digit_10,digit_11,digit_12]
newlist = [digit_1,digit_2,digit_3,digit_4,digit_5,digit_6,digit_7,digit_8,digit_9,digit_10,digit_11,digit_12]
count=0
for i in variables:
    if variables[count] % 2 !=0:
       newlist[count]=variables[count]*3
    count +=1
    print(count-1)   
       
    print(newlist[count-1], variables[count-1])
    

for x in newlist:
    count=0
    checkNum = checkNum + newlist[count]
    count +=1
print(checkNum%10)
checkNum =10-(checkNum%10)

print(digit_1,digit_2,digit_3,'-',digit_4,'-',digit_5,digit_6,digit_7,'-',digit_8,digit_9,digit_10,digit_11,digit_12,'-',checkNum)



