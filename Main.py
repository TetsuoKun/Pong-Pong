import pygame
from Paddle import Paddle 
from ball import Ball 
from HelperFunction import playSFX
# pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
# pygame.mixer.music.load('Media/bgmusic.wav')
# pygame.mixer.music.play(-1)

background = pygame.image.load("images/egg.png")

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (252,186,3)
PURPLE = (111,4,194)
BURPLE = (251,5,255)
GRUE = (4,194,130)
BGRUE = (5,255,172)

MOVE_SPEED = 10
WIDTH = 700
HEIGHT = 500

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def draw_text(word, x, y, font, size):
    Text = pygame.font.Font(font, size)
    textSurf, textRect = text_objects(word, Text)
    textRect.center = (int(x),int(y))
    screen.blit(textSurf, textRect)

def button(message, x, y, width, height, inactive_color, active_color, font, size, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height  > mouse[1] > y:
        pygame.draw.rect(screen, active_color,( x, y , width, height))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, inactive_color,(x, y, width, height))
    draw_text(message, (x+(width/2)), (y+(height/2)), font, size)


def main_menu():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False

        screen.fill(WHITE)

        draw_text("Pong Pong", (WIDTH/2), (HEIGHT/3), "freesansbold.ttf", 115)

        button("Start", 100, 400, 100, 50, GRUE, BGRUE, "freesansbold.ttf", 25, game_loop)
        button("Quit", 500, 400, 100, 50, PURPLE, BURPLE, "freesansbold.ttf", 25, quit)

        pygame.display.update()
        clock.tick(15) 

def game_loop():
    paddleA = Paddle(WHITE, 10, 100)
    paddleA.rect.x = 20 
    paddleA.rect.y = 200 

    paddleB = Paddle(WHITE, 10, 100)
    paddleB.rect.x = 670 
    paddleB.rect.y = 200 

    ball = Ball(WHITE,10,10)
    ball.rect.x = 345
    ball.rect.y = 195

    all_sprites_list = pygame.sprite.Group()

    all_sprites_list.add(paddleA)
    all_sprites_list.add(paddleB)
    all_sprites_list.add(ball)

    carryOn = True

    scoreA = 0 
    scoreB = 0 

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x: 
                    carryOn=False 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                while True:
                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleA.moveUp(MOVE_SPEED)
        if keys[pygame.K_s]:
            paddleA.moveDown(MOVE_SPEED)
        if keys[pygame.K_UP]:
            paddleB.moveUp(MOVE_SPEED)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(MOVE_SPEED)

        all_sprites_list.update()

        if ball.rect.x>=690:
            scoreA+=1
            playSFX('Media/boop.wav')
            ball.rect.x = 345
            ball.rect.y = 195
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x<=0:
            playSFX('Media/boop.wav')
            scoreB+=1
            ball.rect.x = 345
            ball.rect.y = 195
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y>490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y<0:
            ball.velocity[1] = -ball.velocity[1]

        if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
            ball.bounce()

        screen.blit(background, (0,0))

        pygame.draw.line(screen, WHITE, [349, 0], [349,500], 5)

        all_sprites_list.draw(screen)

        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, WHITE)
        screen.blit(text, (250,10))
        text = font.render(str(scoreB), 1, WHITE)
        screen.blit(text,(420,10))

        pygame.display.flip()

        clock.tick(30)

main_menu()

pygame.quit()

