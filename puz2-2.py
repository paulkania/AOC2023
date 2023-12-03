import os

with open('2r.txt','r') as file:
    file=file.read()


file=file.split('\n')

r=0
g=0
b=0
sum=0

def color_checker():
    global r,g,b
    if balls_color_raw[0] == 'r':
        r+=balls_pulled
    elif balls_color_raw[0] == 'g':
        g+=balls_pulled
    elif balls_color_raw[0] == 'b':
        b+=balls_pulled

def max_balls_needed():
    global maxred, maxgreen, maxblue
    if r > maxred:
        maxred = r
    if g > maxgreen:
        maxgreen = g
    if b > maxblue:
        maxblue = b


def reset_balls():
    global r,g,b
    r=0
    g=0
    b=0

for game in file:
    maxred = 0
    maxgreen = 0
    maxblue = 0

    game=game.split()
    game=game[1:]
    game_id = int(game[0][0:-1])
    game=game[1:]
    
    while game:
        balls_pulled = int(game[0])
        balls_color_raw = game[1]
        game=game[2:]
        if balls_color_raw[-1] == ',':
            color_checker()
        elif balls_color_raw[-1] == ';':
            color_checker()
            max_balls_needed()
            reset_balls()
            
        else: #ballcolor -1 is e,n,d
            color_checker()
            max_balls_needed()
            reset_balls()
            game_answer = maxred * maxgreen * maxblue
            sum += game_answer
        
print(sum)