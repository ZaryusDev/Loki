import pygame
from pygame.locals import *
import button


class menu:
    ###############################
    #           INIT              #
    ###############################
  def __init__(self, screen):
    self.screen = screen
    


  def run(self):
    clock = pygame.time.Clock()
    running = True
    self.screen.fill((20, 103, 55))
    font = pygame.font.Font('./break.ttf', 50)
    text = font.render('Stealing is not good', True, (255, 255, 255))
    textRect = text.get_rect()
    X, Y = self.screen.get_size()
    textRect.center = (X // 2, Y // 2)
    retour = button.Button(self.screen, X//2, Y//2+Y//4, 80, 30, (41, 181, 99), (32, 85, 53), "retour", (255, 255, 255), pygame.font.Font("./notes.ttf", 24))
    
    while running:
        self.screen.blit(text, textRect)
        x,y = pygame.mouse.get_pos()
        retour.draw(x, y)

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_x,click_y = pygame.mouse.get_pos()
                
                if retour.action(click_x,click_y):
                    return False
        clock.tick(60)
