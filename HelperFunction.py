import pygame
import constants
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

def playSFX (sound,loops=0):
    effect = pygame.mixer.Sound(sound)
    effect.play(loops)

def text_objects(text, font):
    textSurface = font.render(text, True, constants.BLACK)
    return textSurface, textSurface.get_rect()

def draw_text(word, x, y, font, size):
    Text = pygame.font.Font(font, size)
    textSurf, textRect = text_objects(word, Text)
    textRect.center = (int(x),int(y))
    constants.screen.blit(textSurf, textRect)

def button(message, x, y, width, height, inactive_color, active_color, font, size, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height  > mouse[1] > y:
        pygame.draw.rect(constants.screen, active_color,( x, y , width, height))
        playSFX('Media/sounds/blip.wav', 0)
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(constants.screen, inactive_color,(x, y, width, height))
    draw_text(message, (x+(width/2)), (y+(height/2)), font, size)
