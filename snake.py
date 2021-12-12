import curses
from random import randint #random integer import
# Guide at https://www.youtube.com/watch?v=M_npdRYD4K0

#setup window
curses.initscr()
win = curses.newwin(20, 60, 0 , 0)
# Create new window 20 height 60 width, starts at y=0, x=0
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
# draw a border
win.nodelay(1)
# Not waiting for next user input, 1 = true

# snake and food logic
snake = [(4, 10), (4, 9), (4, 8)]
# Creating snake as a list, with immutable twople within it
food = (10, 20)
# food using twople

win.addch(food[0], food[1], 'ʘ')
#adding first food

# Game Logic
score = 0
# we want this to increase each time you eat a fruit

ESC = 27
#this is the key # of the escape button in curses
key=curses.KEY_RIGHT

while key != ESC:
    # while key is not being pressed, here it is escape
    # while True: is an endless loop

    win.addstr(0, 2, 'Score ' + str(score) + ' ')

    win.timeout(150 -(len(snake)) // 5 + len(snake)//10 % 120) 
    # Increase speed based on length of snake

    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key

    #calculate the next coordinates for our snake
    y = snake[0][0]
    #getting the first twople
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1

    snake.insert(0, (y, x)) #append w/ a list, it is faster sometimes, append 0(n)

    # check if we hit the border
    if y == 0: break
    if y == 19: break
    if x == 0: break
    if x == 59: break
    #breaks at borders

    #if snake runs over itself
    if snake[0] in snake[1:]: break
    # check if the snake is running into a coordinate that it already contains (runs into self)
    # snake[1:] check all other positions starting at 1 - method called list slicing

    if snake[0] == food:
        #eat the food
        score += 1
        #draw a new food
        food = ()
        while food == ():
            food = (randint(1,18), randint(1,58))
            #after food is eaten the twople is empty, make a new food within random coordinate of window boundaries
            if food in snake:
                #Don't place food in snake!
                food = ()
        win.addch(food[0], food[1], 'ʘ')
    else:
        #move snake
        last = snake.pop() #return last coordinate, and remove it from the array
        win.addch(last [0], last[1], ' ')
    
    # for c in snake:
    #     #For every coordinate in snake:
    #     win.addch(c[0], c[1], '*')
    #     #Specifies coordinates of next asterisk creation (snake segment)

    # win.addch(food[0], food[1], 'ʘ')
    # #Specifies x and y coordinates of food, and the food's symbol

    win.addch(snake[0][0], snake[0][1], '*')




curses.endwin()
# ends game
print(f"Final score = {score}")
# f string w/ curly braces