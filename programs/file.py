file = open("programs/teams.txt", "r")

outfile = ""

for line in range(1, 6):
    if line == 1 or line == 2:
        outfile += file.readline()
    else:
        file.readline()

print(outfile)
file.close()