import pygame
from Paddle import Paddle 
from ball import Ball 
import HelperFunction
import constants
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load(constants.BG_MUSIC)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(constants.BG_MUSIC_VOLUME)

game_background = pygame.image.load(constants.BG_GAME_IMAGE)
MMB = pygame.image.load(constants.MAIN_MENU)
icon = pygame.image.load(constants.ICON)

pygame.init()

pygame.display.set_caption("Pong")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

#TODO: Consider exiting the funciton loop instead of calling a new funciton for each sscene button to keep the stack from filling up.  

def main_menu():
    print ("Running Main Menu")
    intro = True
    play_button = HelperFunction.Button("Start", 100, 400, width = 100, height = 50, inactive_color = constants.GRUE, hover_color = constants.BGRUE, active_color =  constants.WHITE, font = "freesansbold.ttf", size = 25, action  =  game_loop)
    exit_button = HelperFunction.Button("Quit", 500, 400, width = 100, height = 50, inactive_color = constants.PURPLE, hover_color = constants.BURPLE, active_color = constants.WHITE, font =  "freesansbold.ttf", size = 25, action = quit)
    settings_button = HelperFunction.Button("Settings", 615, 20, width = 50, height = 25, size = 10, hover_color = (125, 125, 125), active_color = constants.WHITE, action = settings)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        constants.screen.fill(constants.WHITE)
        constants.screen.blit(MMB, (0,0))

        HelperFunction.draw_text("Pong Pong", (constants.WIDTH/2), (constants.HEIGHT/3), "freesansbold.ttf", 115)

        
        play_button.render_button()
        exit_button.render_button()
        settings_button.render_button()

        pygame.display.update()
        clock.tick(15) 

def settings():
    #settings = open("Data/settings.txt", "r+")
    #str = settings.read()
    #print ("The file says", str)
    menu_button = HelperFunction.Button("Main Menu", 30, 20, width = 50, height = 25, size = 9, hover_color = (125, 125, 125), active_color = constants.WHITE, action = main_menu)
    settings_page = True
    while settings_page == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        constants.screen.fill(constants.WHITE)
        constants.screen.blit(MMB, (0,0))
        
        HelperFunction.draw_text("Settings", (constants.WIDTH/2), (constants.HEIGHT/9), "freesansbold.ttf", 50)
        menu_button.render_button()

        pygame.display.update()
        clock.tick(15)
    #settings.close()


def game_loop():
    paddleA = Paddle(constants.BLACK, 10, 100)
    paddleA.rect.x = 20 
    paddleA.rect.y = 200 

    paddleB = Paddle(constants.BLACK, 10, 100)
    paddleB.rect.x = 670 
    paddleB.rect.y = 200 

    ball = Ball(constants.BLACK,10,10)
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
            paddleA.moveUp(constants.MOVE_SPEED)
        if keys[pygame.K_s]:
            paddleA.moveDown(constants.MOVE_SPEED)
        if keys[pygame.K_UP]:
            paddleB.moveUp(constants.MOVE_SPEED)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(constants.MOVE_SPEED)

        all_sprites_list.update()

        if ball.rect.x>=690:
            scoreA+=1
            HelperFunction.playSFX(constants.BOOP)
            ball.rect.x = 345
            ball.rect.y = 195
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x<=0:
            HelperFunction.playSFX(constants.BOOP)
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

        constants.screen.blit(game_background, (0,0))

        pygame.draw.line(constants.screen, constants.BLACK, [349, 0], [349,500], 5)

        all_sprites_list.draw(constants.screen)

        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, constants.BLACK)
        constants.screen.blit(text, (250,10))
        text = font.render(str(scoreB), 1, constants.BLACK)
        constants.screen.blit(text,(420,10))

        pygame.display.flip()

        clock.tick(30)

main_menu()



pygame.quit()

