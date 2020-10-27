def timestable():
    table = ''

    for i in range(1,11):
        for j in range(1,11):
            table += str((i*j)) + '\t'
        table += '\n'
        
    return table

print(timestable())