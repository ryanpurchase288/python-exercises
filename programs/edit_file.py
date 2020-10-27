file = open("programs/teams.txt", "r")

outfile = ""

for line in range(5):
    if line == 0:
        file.readline()
        outfile += "This is a new line\n"
    else:
        outfile += file.readline()

file = open("programs/teams.txt", "w")
file.write(outfile)
file = open("programs/teams.txt", "r")
lines = file.readlines()
print(lines)
file.close()
