counter = 0
f = open("meilsis.txt", "r")
first_line = f.readline()
print(first_line)
mails = []
for i in range(int(first_line)):
    second_line = f.readline()
    print(second_line)
