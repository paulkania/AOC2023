import os

with open('2f.txt','r') as file:
    file=file.read()

file=file.split('\n')
f2=[]
for line in file:
    line=line.split()
    f2.append(line)


def color_tally():
    global red, green, blue
    if color[0:-1] == 'red':
        red +=int(score)
    elif color[0:-1] == 'green':
        green +=int(score)
    elif color[0:-1] == 'blue':
        blue +=int(score)

winning_games=[]
for line in f2:
    blue=0
    green=0
    red=0
    print(line)
    id = int(line[1][0:-1])
    while line:
        line=line[2:]
        score = line[0]
        color = line[1]
        if color[-1] == ';':
            color = color[0:-1] #get rid of ;
            color_tally()
            if red <= 12 or green <= 13 or blue <= 14:
                blue=0
                green=0
                red=0
                winning_games.append(id)
            pass #reset
        color_tally()
