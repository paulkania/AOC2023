import os

with open('2r.txt','r') as file:
    file=file.read()


file=file.split('\n')

maxred = 12
maxgreen = 13
maxblue = 14
r=0
g=0
b=0
winning_games=0

def color_checker():
    global r,g,b
    if balls_color_raw[0] == 'r':
        r+=balls_pulled
    elif balls_color_raw[0] == 'g':
        g+=balls_pulled
    elif balls_color_raw[0] == 'b':
        b+=balls_pulled

def overflow_checker():
    global illegal_game
    if r > maxred or b > maxblue or g > maxgreen:
        illegal_game = True

def reset_balls():
    global r,g,b
    r=0
    g=0
    b=0 

for game in file:
    game=game.split()
    game=game[1:]
    game_id = int(game[0][0:-1]) #.
    game=game[1:]
    
    illegal_game = False

    while game:
        balls_pulled = int(game[0])
        balls_color_raw = game[1]
        game=game[2:]
        if balls_color_raw[-1] == ',':
            color_checker()
        elif balls_color_raw[-1] == ';':
            color_checker()
            overflow_checker()
            reset_balls()
            
        else: #ballcolor -1 is e,n,d
            color_checker()
            overflow_checker()
            reset_balls()
            if illegal_game == False:
                winning_games += game_id
            illegal_game = False
        
print(winning_games)