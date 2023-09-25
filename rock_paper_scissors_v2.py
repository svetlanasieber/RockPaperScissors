import random


play = True
c_score = 0
u_score = 0
choices = ['R', 'P', 'S']

ch = {
    'R': 'Rock',
    'P': 'Paper',
    'S': 'Scissors'
}

u_choice = input('''type "R" for Rock,
     "P" for Paper,
     "S" for scissors and
     "Stop" to end the game.

    'Press "enter" to start the game.\n''').upper()
while play:
    c_choice = random.choice(choices)
    u_choice = input('>').upper()
    if u_choice == c_choice:
        print(f'''AI: chose :{c_choice}
                         DRAW
                You:{u_score} --- AI:{c_score}''')
    elif u_choice == 'R' and c_choice == 'P':
        c_score += 1
        print(f'''AI: Paper
                 AI WINS
                  You:{u_score} --- AI:{c_score}''')
    elif u_choice == 'S' and c_choice == 'R':
        c_score += 1
        print(f'''AI: Rock
                 AI WINS
                  You:{u_score} --- AI:{c_score}''')
    elif u_choice == 'P' and c_choice == 'S':
        c_score += 1
        print(f'''AI: Scissors
                 AI WINS
                  You:{u_score} --- AI:{c_score}''')
    else:
        u_score += 1
        print(f'''AI: {c_choice}
                     YOU WIN
                  You:{u_score} --- AI:{c_score}''')
    if u_choice == 'stop':
        break
        print('Game is terminated!')
    if c_score == 3 or u_score == 3:
        break
print(f'''           GAME OVER!
        Result: YOU ({u_score}) -- AI ({c_score})''')
