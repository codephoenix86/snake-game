# import statements
import pygame,sys,os
os.chdir(r'C:\Users\91861\Documents\coding\python\snake game')
from pygame.math import Vector2
from random import randint
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()

# Display Surface
cell_size = 20
screen_resolution = (cell_size*70,cell_size*30)
screen = pygame.display.set_mode(screen_resolution)
background_color = (175,215,70)
pygame.display.set_caption('Snake Game')

# Game Speed
clock = pygame.time.Clock()
FPS = 60

# board
grass_color = (167,209,61)
grass_surf = pygame.Surface((20,20))
grass_surf.fill(grass_color)

# Font
font = pygame.font.Font('PoetsenOne-Regular.ttf',20)
sc = 0

# Sounds
crunch_sd = pygame.mixer.Sound('crunch.wav')

# Fruit
class FRUIT:
    def __init__(self):
        self.pos = Vector2(randint(0,69),randint(0,29))
    def draw_fruit(self):
        surf = pygame.image.load(r'Graphics\apple.png').convert_alpha()
        surf = pygame.transform.scale(surf,(20,20))
        self.place()
        rect = surf.get_rect(topleft=(self.pos.x*cell_size,self.pos.y*cell_size))
        screen.blit(surf,rect)
    def draw_score(self):
        score = font.render(str((len(snake.body)-5)*10),True,(56,74,12))
        score_rect = score.get_rect(bottomright=(1380,580))
        screen.blit(score,score_rect)
    def place(self):
        while self.pos in snake.body[:-1]:
            self.pos = Vector2(randint(0,69),randint(0,29))

# Snake
class SNAKE:
    head_right = pygame.transform.scale(pygame.image.load(r'Graphics\head_right.png'),(20,20)).convert_alpha()
    head_left = pygame.transform.scale(pygame.image.load(r'Graphics\head_left.png'),(20,20)).convert_alpha()
    head_up = pygame.transform.scale(pygame.image.load(r'Graphics\head_up.png'),(20,20)).convert_alpha()
    head_down = pygame.transform.scale(pygame.image.load(r'Graphics\head_down.png'),(20,20)).convert_alpha()

    tail_right = pygame.transform.scale(pygame.image.load(r'Graphics\tail_right.png'),(20,20)).convert_alpha()
    tail_left = pygame.transform.scale(pygame.image.load(r'Graphics\tail_left.png'),(20,20)).convert_alpha()
    tail_up = pygame.transform.scale(pygame.image.load(r'Graphics\tail_up.png'),(20,20)).convert_alpha()
    tail_down = pygame.transform.scale(pygame.image.load(r'Graphics\tail_down.png'),(20,20)).convert_alpha()

    body_horizontal = pygame.transform.scale(pygame.image.load(r'Graphics\body_horizontal.png'),(20,20)).convert_alpha()
    body_vertical = pygame.transform.scale(pygame.image.load(r'Graphics\body_vertical.png'),(20,20)).convert_alpha()

    body_tl = pygame.transform.scale(pygame.image.load(r'Graphics\body_tl.png'),(20,20)).convert_alpha()
    body_bl = pygame.transform.scale(pygame.image.load(r'Graphics\body_bl.png'),(20,20)).convert_alpha()
    body_br = pygame.transform.scale(pygame.image.load(r'Graphics\body_br.png'),(20,20)).convert_alpha()
    body_tr = pygame.transform.scale(pygame.image.load(r'Graphics\body_tr.png'),(20,20)).convert_alpha()
    def __init__(self):
        self.body = [Vector2(4,2),Vector2(5,2),Vector2(6,2),Vector2(7,2),Vector2(8,2)]
        self.direction = Vector2(1,0)
        self.new_block = False
    def draw_snake(self):
        for i in range(len(self.body)):
            if i == len(self.body)-1:
                if self.body[-1]-self.body[-2] == Vector2(1,0):
                    screen.blit(self.head_right,(self.body[i].x*cell_size,self.body[i].y*cell_size))
                elif self.body[-1]-self.body[-2] == Vector2(-1,0):
                    screen.blit(self.head_left,(self.body[i].x*cell_size,self.body[i].y*cell_size))
                elif self.body[-1]-self.body[-2] == Vector2(0,1):
                    screen.blit(self.head_down,(self.body[i].x*cell_size,self.body[i].y*cell_size))
                elif self.body[-1]-self.body[-2] == Vector2(0,-1):
                    screen.blit(self.head_up,(self.body[i].x*cell_size,self.body[i].y*cell_size))
            elif i == 0:
                if self.body[1]-self.body[0] == Vector2(1,0):
                    screen.blit(self.tail_left,(self.body[i].x*cell_size,self.body[i].y*cell_size))
                elif self.body[1]-self.body[0] == Vector2(-1,0):
                    screen.blit(self.tail_right,(self.body[i].x*cell_size,self.body[i].y*cell_size))
                elif self.body[1]-self.body[0] == Vector2(0,1):
                    screen.blit(self.tail_up,(self.body[i].x*cell_size,self.body[i].y*cell_size))
                elif self.body[1]-self.body[0] == Vector2(0,-1):
                    screen.blit(self.tail_down,(self.body[i].x*cell_size,self.body[i].y*cell_size))
            else:
                # rect = pygame.Rect(self.body[i].x*cell_size,self.body[i].y*cell_size,cell_size,cell_size)
                # pygame.draw.rect(screen,(183,111,122),rect)
                if self.body[i]-self.body[i-1] == self.body[i+1]-self.body[i] == Vector2(1,0) or self.body[i]-self.body[i-1] == self.body[i+1]-self.body[i] == Vector2(-1,0):
                    screen.blit(self.body_horizontal,(self.body[i].x*cell_size,self.body[i].y*cell_size))
                elif self.body[i]-self.body[i-1] == self.body[i+1]-self.body[i] == Vector2(0,1) or self.body[i]-self.body[i-1] == self.body[i+1]-self.body[i] == Vector2(0,-1):
                    screen.blit(self.body_vertical,(self.body[i].x*cell_size,self.body[i].y*cell_size))
                elif self.body[i]-self.body[i-1] == Vector2(1,0) and self.body[i+1]-self.body[i] == Vector2(0,1):
                    screen.blit(self.body_bl,(self.body[i].x*cell_size,self.body[i].y*cell_size))
                elif self.body[i]-self.body[i-1] == Vector2(1,0) and self.body[i+1]-self.body[i] == Vector2(0,-1):
                    screen.blit(self.body_tl,(self.body[i].x*cell_size,self.body[i].y*cell_size))
                elif self.body[i]-self.body[i-1] == Vector2(-1,0) and self.body[i+1]-self.body[i] == Vector2(0,1):
                    screen.blit(self.body_br,(self.body[i].x*cell_size,self.body[i].y*cell_size))
                elif self.body[i]-self.body[i-1] == Vector2(-1,0) and self.body[i+1]-self.body[i] == Vector2(0,-1):
                    screen.blit(self.body_tr,(self.body[i].x*cell_size,self.body[i].y*cell_size))
                elif self.body[i]-self.body[i-1] == Vector2(0,1) and self.body[i+1]-self.body[i] == Vector2(1,0):
                    screen.blit(self.body_tr,(self.body[i].x*cell_size,self.body[i].y*cell_size))
                elif self.body[i]-self.body[i-1] == Vector2(0,1) and self.body[i+1]-self.body[i] == Vector2(-1,0):
                    screen.blit(self.body_tl,(self.body[i].x*cell_size,self.body[i].y*cell_size))
                elif self.body[i]-self.body[i-1] == Vector2(0,-1) and self.body[i+1]-self.body[i] == Vector2(1,0):
                    screen.blit(self.body_br,(self.body[i].x*cell_size,self.body[i].y*cell_size))
                elif self.body[i]-self.body[i-1] == Vector2(0,-1) and self.body[i+1]-self.body[i] == Vector2(-1,0):
                    screen.blit(self.body_bl,(self.body[i].x*cell_size,self.body[i].y*cell_size))
    def move_snake(self):
        if self.new_block == True:
            self.body.append(self.body[-1]+self.direction)
            self.new_block = False
        else:
            self.body.pop(0)
            self.body.append(self.body[-1]+self.direction)
    def check_collision(self):
        if [snake.body[-1].x,snake.body[-1].y] == fruit.pos:
                fruit.pos = Vector2(randint(0,69),randint(0,29))
                snake.new_block = True
                crunch_sd.play()
        if not(0<=self.body[-1].x<70 and 0<=self.body[-1].y<30):
            pygame.quit()
            sys.exit()
        for i in range(len(self.body)):
            if self.body[-1] == self.body[i] and i != len(self.body)-1:
                pygame.quit()
                sys.exit()
# Objects
fruit = FRUIT()
snake = SNAKE()

# Time Specific Events
MOVESNAKE = pygame.USEREVENT
pygame.time.set_timer(MOVESNAKE,150)

def draw_grass():
    for y in range(0,600,20):
        if y % 40 == 0:
            for x in range(0,1400,40):
                grass_rect = grass_surf.get_rect(topleft=(x,y))
                screen.blit(grass_surf,grass_rect)
        else:
            for x in range(20,1400,40):
                grass_rect = grass_surf.get_rect(topleft=(x,y))
                screen.blit(grass_surf,grass_rect)
# Game Loop
gameOn = True
while gameOn:
    all_events = pygame.event.get()
    # Event Loop
    for event in all_events:
        if event.type == MOVESNAKE:
            snake.move_snake()
            snake.check_collision()
        if event.type == pygame.QUIT:
            gameOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.direction != Vector2(-1,0):
                snake.direction = Vector2(1,0)
            elif event.key == pygame.K_LEFT and snake.direction != Vector2(1,0):
                snake.direction = Vector2(-1,0)
            elif event.key == pygame.K_DOWN and snake.direction != Vector2(0,-1):
                snake.direction = Vector2(0,1)
            elif event.key == pygame.K_UP and snake.direction != Vector2(0,1):
                snake.direction = Vector2(0,-1)
    screen.fill(background_color)
    draw_grass()
    fruit.draw_score()
    snake.draw_snake()
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(FPS)

# Exiting the program
pygame.quit()
sys.exit()