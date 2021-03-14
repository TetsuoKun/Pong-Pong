import pygame
import constants
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

def playSFX (sound,loops=0, volume=1):
    """Plays sounds for any effect in the game"""
    effect = pygame.mixer.Sound(sound)
    effect.set_volume(volume)
    effect.play(loops)

def text_objects(text, font):
    textSurface = font.render(text, True, constants.BLACK)
    return textSurface, textSurface.get_rect()

def draw_text(word, x, y, font = "freesansbold.ttf", size = 30):
    """Creates text"""
    Text = pygame.font.Font(font, size)
    textSurf, textRect = text_objects(word, Text)
    textRect.center = (int(x),int(y))
    constants.screen.blit(textSurf, textRect)

class Button:
    def __init__(self, message, x, y, width = 100, height = 50, inactive_color = constants.GREY, hover_color = constants.GREY, active_color = constants.GREY, font = "freesansbold.ttf", size = 25, action = None):
        self.message = message
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 
        self.inactive_color = inactive_color
        self.hover_color = hover_color
        self.active_color = active_color
        self.font = font
        self.size = size
        self.action = action
        self.CanPlayHoverSound = True
        self.HasBeenClicked = False

        #TODO: FIX ACTIVE COLOR 

    def render_button(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x + self.width > mouse[0] > self.x and self.y + self.height  > mouse[1] > self.y:
            pygame.draw.rect(constants.screen, self.hover_color,( self.x, self.y , self.width, self.height))
            
            if self.CanPlayHoverSound == True:
                playSFX(constants.BUTTON_HOVER_SOUND, 0)
                self.CanPlayHoverSound = False
                
            if click[0] == 1 and self.action != None and self.HasBeenClicked == False:
                #can't remember, what this does, .... uhhhhh keep.
                #pygame.draw.rect(constants.screen, constants.WHITE,( self.x, self.y , self.width, self.height))
                #if click[0] == 0:
                playSFX(constants.BUTTON_CLICK_SOUND, 0, constants.CLICK_SOUND_VOLUNE)
                self.HasBeenClicked = True 
                self.action() 
                

        else:
            pygame.draw.rect(constants.screen, self.inactive_color,(self.x, self.y, self.width, self.height))
            self.CanPlayHoverSound = True
        draw_text(self.message, (self.x+(self.width/2)), (self.y+(self.height/2)), self.font, self.size)
    
