
  
def near(string1, string2):
    for i in range(len(string1)):
        newstr = string1[:i] + string1[i+1:]
        if newstr == string2:
            return True
    return False

print(near('dragoon', 'dragon'))
    