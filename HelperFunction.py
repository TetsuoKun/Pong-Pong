import pygame
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

def playSFX (sound):
    effect = pygame.mixer.Sound(sound)
    effect.play()


