counter = 0
f = open("meilsis.txt", "r")
first_line = int(f.readline())
#print(first_line)
mails = []
for i in range(int(first_line)):
    second_line = f.readline()
    mails.append(second_line)
    #print(second_line)
third_line = int(f.readline())
#print(third_line)
for h in range(third_line):
    mails2 = f.readline()
    if mails2 in mails:
        counter = counter = 1
        print(counter)
