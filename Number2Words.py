import number2wordsModule
numberList = list(str(input("Number: ")))
num = ""
num1 = ""
num2 = ""
num3 = ""
num4 = ""
num5 = ""
num6 = ""
num7 = ""
num8 = ""
num9 = ""
num10 = ""
num11 = ""
num12 = ""
num13 = ""
num14 = ""
while True:
    if number2wordsModule.spec(numberList):
        print(number2wordsModule.spec(numberList))
        break
    if len(numberList) == 1:
        if numberList[0] == "0":
            numberList.remove(numberList[0])
        else:
            num = number2wordsModule.single(numberList[0])
            numberList.remove(numberList[0])
    elif len(numberList) == 2:
        num1 = number2wordsModule.words(numberList)
    elif len(numberList) == 3:
        num2 = number2wordsModule.hundreds(numberList)
    elif len(numberList) == 4:
        num3 = number2wordsModule.add(numberList, "Thousand")
    elif len(numberList) == 5:
        num4 = number2wordsModule.words(numberList)
    elif len(numberList) == 6:
        num6 = number2wordsModule.hundreds(numberList)
    elif len(numberList) == 7:
        num7 = number2wordsModule.add(numberList, "Million")
    elif len(numberList) == 8:
        num8 = number2wordsModule.words(numberList)
    elif len(numberList) == 9:
        num9 = number2wordsModule.hundreds(numberList)
    elif len(numberList) == 10:
        num10 = number2wordsModule.add(numberList, "Billion")
    elif len(numberList) == 11:
        num11 = number2wordsModule.words(numberList)
    elif len(numberList) == 12:
        num12 = number2wordsModule.hundreds(numberList)
    elif len(numberList) == 13:
        num13 = number2wordsModule.add(numberList, "Trillion")
    elif len(numberList) == 0:
        print(num13, num12, num11, num10, num9, num8, num7, num6, num5, num4, num3, num2, num1, num,
              num14)
        break