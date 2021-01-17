import pygame
#colors70
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (252,186,3)
PURPLE = (111,4,194)
BURPLE = (251,5,255)
GRUE = (4,194,130)
BGRUE = (5,255,172)

#sounds
BOOP = 'Media/sounds/boop.wav'
BELL = 'Media/sounds/Tacobell.wav'
BG_MUSIC = 'Media/sounds/bgmusic.wav'
BUTTON_CLICK_SOUND = "Media/sounds/derp.wav"
BUTTON_HOVER_SOUND = "Media/sounds/blip.wav"

#images
BG_GAME_IMAGE = "Media/images/poached.png" 
MAIN_MENU = "Media/images/boiledegg.png"
ICON = "Media/images/icon1.png"

#numbers
MOVE_SPEED = 10
WIDTH = 700
HEIGHT = 500
BG_MUSIC_VOLUME = .1
PADDLE_HIT_SOUND = .1
CLICK_SOUND_VOLUNE = .1

#variables
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

#TODO: clean up dependencies
