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
MOVE_SPEED = 5

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

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

clock = pygame.time.Clock()

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

pygame.quit()

