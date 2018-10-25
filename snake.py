# Funnest Snake Game bought to you by Group Hex.
# Contributors : ChenLong Li, PeiPei Han and Yashaswini Seeta.


from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

score = 0
speed = 0.50
snake = [0, 3, 0, 4, 0, 5, 0, 6]
frog = [randint(0, 7), randint(0, 7)]

snake_dir = 1
# Direction of snake
# W = up
# S = down
# A = left
# D = right

def make_frog():
    sense.set_pixel(frog[0], frog[1], 0, 255, 0)
    #Sets frog in random pixels

def create_snake(t):
    # Argument of function is 0(draw normally) or 1(increase length of snake)
    global snake, snake_dir

    if t==1:
            snake.append(snake[len(snake)-2])
            snake.append(snake[len(snake)-1])
            # Increases the snake by duplicating the last two segments of snake.

    for i in range(1, len(snake)-1):
        global snake
        snake[len(snake)-i]=snake[len(snake)-i-2]
        # Except the head , move each snake segment forward by 1  


    if snake_dir == 1:    
        snake[1]-=1   #If snake is oriented up then increase the y coordinate by 1
    elif snake_dir == 2:
        snake[1]+=1   #If snake is oriented down then decrease the y coordinate by 1
    elif snake_dir == 3:
        snake[0]-=1   #If snake is oriented left then decrease the x coordinate by 1
    elif snake_dir == 4:
        snake[0]+=1   #If snake is oriented right then increase the x coordinate by 1
  
    #Makes snake move through end of LED matrix
    if snake[0]>7:
        snake[0]=0
    if snake[0]<0:
        snake[0]=7
    if snake[1]>7:
        snake[1]=0
    if snake[1]<0:
        snake[1]=7
    
    #Color up the snake
    for i in range (0, int(len(snake)/2)):
        if i == 0:
            sense.set_pixel(snake[2*(i)], snake[2*(i)+1], 255, 255, 255)
        else:
            sense.set_pixel(snake[2*(i)], snake[2*(i)+1], 168, 4, 192)

# Functions to change the direction of the snake
# Snake cannot make move in the complete opposite direction of its current orientation
def up_move():
    global snake_dir 
    snake_dir = 'W'
def down_move():
    global snake_dir
    snake_dir = 'S'
def left_move():
    global snake_dir
    snake_dir = 'A'
def move_right():
    global snake_dir
    snake_dir = 'D'

# Controls mapped to the joystick
if True:
    sense.stick.direction_up = up_move
    sense.stick.direction_down = down_move
    sense.stick.direction_left = left_move
    sense.stick.direction_right = right_move

# Main game loop
#Startup screen
sense.show_message("Classic Snake by Group")
sense.show_letter("H",back_colour[128,0,128])
sense.show_letter("E",back_colour[128,0,128])
sense.show_letter("X",back_colour[128,0,128])
    
while True:
    sense.clear()
    #Game start countdown"
    sense.show_message("Game Starts in:")
    for i in reversed(range(0,3)):
        sense.show_letter(str(i))
        time.sleep(1)
    
    end = False
    for i in range (1, int(len(snake)/2)-1):
     #Game ends when snake eats itself , so we run the main loop for as many times as the snake'same
     #segments.
        if not end:
            # Checks it the snake head is colliding with any of the snake segments
            if snake[0] == snake[2*i] and snake[1] == snake[2*i+1]:
                sense.show_message("Game over ! You scored " + str(score))  
                
                score = 0
                speed = 0.50
                snake = [4, 3, 4, 4, 4, 5, 4, 6]
                frog = [randint(0, 7), randint(0, 7)]
                snake_dir = 1
                        # Reset
                end = True
    #Setting up the environment
    make_frog()

    #Mechanism to check if the frog is eaten and increasing the speed with every increase in score
    if frog[0]==snake[0] and frog[1] == snake[1]:
        create_snake(1)
        speed = speed * 0.9
        frog[0] = randint(0, 7)
        frog[1] = randint(0, 7)
        score += 1
    else:
        create_snake(0)
    sleep(speed)
