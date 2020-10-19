import sys

participant = sys.stdin

sys.stdout.write(participant.readline().strip() + '\n')
participant_nr = participants.readline()
names = {}
for i in range(int(participant_nr)):
    students = participants.readline().split()
    names[students[0]] = students[1]
for i in range(int(participant_nr)):
    username = participants.readline().split()
    print(names[username[0]] +' '+ username[1])
