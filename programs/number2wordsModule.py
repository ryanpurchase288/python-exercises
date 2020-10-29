def single(numberList):
    singles = {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven",
               "8": "Eight", "9": "Nine"}
    if numberList in list(singles.keys()):
        return singles[numberList]


def teens(numberList):
    teen = {"10": "Ten", "11": "Eleven", "12": "Twelve", "13": "Thirteen", "14": "Fourteen", "15": "Fifteen",
               "16": "Sixteen", "17": "Seventeen", "18": "Eighteen", "19": "Nineteen"}
    if numberList in list(teen.keys()):
        return teen[numberList]


def tens(numberList):
    ten = {"2": "Twenty", "3": "Thirty", "4": "Forty", "5": "Fifty", "6": "Sixty", "7": "Seventy", "8": "Eighty",
           "9": "Ninety"}
    if numberList in list(ten.keys()):
        return ten[numberList]

def hundreds(numberList):
    if numberList[0] == "0":
        numberList.remove(numberList[0])
        empty = ""
        return empty
    elif numberList[1] == "0" and numberList[2] == "0":
        hundred = single(numberList[0]) + " " + "Hundred"
        numberList.remove(numberList[0])
        numberList.remove(numberList[0])
        return hundred
    else:
        hundred = single(numberList[0]) + " " + "Hundred" + " " + "and"
        numberList.remove(numberList[0])
        return hundred


def words(numberList):
    if numberList[0] == "0":
        numberList.remove(numberList[0])
        empty = ""
        return empty
    elif numberList[0] == "1":
        joint = "".join(numberList[0:2])
        word = teens(joint)
        if len(numberList) == 5:
            word = teens(joint) + " " + "Thousand"
        elif len(numberList) == 8:
            word = teens(joint) + " " + "Million"
        elif len(numberList) == 11:
            word = teens(joint) + " " + "Billion"
        numberList.remove(numberList[0])
        numberList.remove(numberList[0])
        return word
    else:
        word = tens(numberList[0])
        numberList.remove(numberList[0])
        return word


def add(numberList, string1):
    if numberList[0] == "0":
        numberList.remove(numberList[0])
    else:
        add = single(numberList[0]) + " " + string1
        numberList.remove(numberList[0])
        return add


def spec(numberList):
    specials = {"100000": "One Hundred Thousand", "1000000": "One Million", "100000000": "One Hundred Million",
                "10000000": "Ten Million", "1000000000000": "One Trillion"}
    new = "".join(numberList)
    if new in list(specials.keys()):
        done = specials[new]
        return done
    else:
        return False