def timestable(max):
    table = ''

    for i in range(max):
        for j in range(max):
            table += str(((i+1)*(j+1))) + '\t'
        table += '\n'
        
    return table

print(timestable(10))