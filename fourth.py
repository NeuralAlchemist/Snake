# Contributors : ChenLong Li, PeiPei Han and Yashaswini Seeta.


from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
up = "W"
down = "S"
left = "A"
right = "D"
class snake_game:
    snake=[]
    foodX = 0
    foodY= 0
    snake_dir = up 
    speed = 1.5
    score = 0

class snake_game:
    def move_up(self):
        if self.snake_dir != down: 
            self.snake_dir = up
    def move_down(self):
        if self.snake_dir != up:
            self.snake_dir = down
    def move_left(self):
        if self.snake_dir != right:
            self.snake_dir = left
    def move_right(self):
        if self.snake_dir != left:
            self.snake_dir = right
     
    def __init__(self):
        self.score = 0
        self.speed = 1.0
        self.snake = [2,3,2,4]
        self.snake_dir = up
        self.foodX = randint(0, 7)
        self.foodY=randint(0, 7)
        self.stick_control=False
        sense.stick.direction_up = self.move_up
        sense.stick.direction_down = self.move_down
        sense.stick.direction_left = self.move_left
        sense.stick.direction_right = self.move_right
    
    def rearrange_snake(self):
        snake_length = len(self.snake)
        if self.snake_dir == up:
            self.snake[1] -=1
        elif self.snake_dir == down:
            self.snake[1] +=1
        elif self.snake_dir == left:
            self.snake[0] -=1
        else:
            self.snake[0] +=1

        if self.snake[0]>7:
            self.snake[0]=0
        if self.snake[0]<0:
            self.snake[0]=7
        if self.snake[1]>7:
            self.snake[1]=0
        if self.snake[1]<0:
            self.snake[1]=7

    def make_food(self):
         sense.set_pixel(self.foodX, self.foodY, 0, 255, 0)
         #Sets food in random pixels

    def create_snake(self,t):
        originalX = self.snake[0]
        originalY = self.snake[1]
        self.snake.insert(0, originalX)
        self.snake.insert(1, originalY)
        snake_length = len(self.snake)
        if t == 0:
            del self.snake[snake_length-1]
            del self.snake[snake_length -2]
 
        snake_length = len(self.snake)
        self.rearrange_snake() 
        
        for i in range (0, int(snake_length/2)):
            if i == 0:
                sense.set_pixel(self.snake[2*(i)], self.snake[2*(i)+1], 255, 0, 0)
            else:
                sense.set_pixel(self.snake[2*(i)], self.snake[2*(i)+1], 255, 255, 255)

    def run(self): 
        while True:
            sense.clear()
            snake_length = len(self.snake)
            for i in range (1, int(snake_length/2)-1):
                    if self.snake[0] == self.snake[2*i] and self.snake[1] == self.snake[2*i+1]:
                        sense.show_message("You scored " + str(self.score))         
                        self.__init__()
                        break
            
            self.make_food()
            if self.foodX == self.snake[0] and self.foodY == self.snake[1]:
                self.create_snake(1)
                self.speed = self.speed * 0.8
                self.foodX = randint(0, 7)
                self.foodY = randint(0, 7)
                self.score += 1
            else:
                self.create_snake(0)
            sleep(self.speed)

snakeGame =snake_game()
snakeGame.run()
