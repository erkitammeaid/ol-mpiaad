f = open("yksis.txt", "r")
first_line = f.readline().split()
print(first_line)
a = int(first_line[0]) + int(first_line[1]) *10
print(a)
maximum = a
o = f.readline().split()
for i in range(int(o)):
    o1 = o.readline().split()
    print(o1)
