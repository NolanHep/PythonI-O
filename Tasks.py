#1

f = open("Task1.txt", "r")
print('Task1 file read.')
print(f.read())

#2
create = 0

try:
    x = open("november20.txt", "x") #Creates new file with
    x = open("november20.txt", "a")
    for i in range(0, 3):              #This just lets the program work smoother.
        x.write("Added 3 lines")

#3

except FileExistsError:

    x = open("november20.txt", "a")
    for i in range(0,3):
        x.write("\nAdded 3 lines")

#4

r = open("november20.txt", "w")

for i in range(0,4):
    r.write("\nWhoops 4 new lines.")\

r = open("november20.txt", "r")
print('New Lines')
print(r.read())
