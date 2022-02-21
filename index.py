import webbrowser 
import pygame
import pygame.freetype
import button
from enum import Enum
from gen import menu
BLUE = (20, 103, 55)
WHITE = (255, 255, 255)


class GameState(Enum):
  QUIT = -1
  TITLE = 0
  NEWGAME = 1

def title_screen(screen):
    clock = pygame.time.Clock()
    screen.fill((20, 103, 55))
    X, Y = screen.get_size()
    run = button.Button(screen, 300, 200, 80, 30, (41, 181, 99), (32, 85, 53), "Run", (255, 255, 255), pygame.font.Font("./notes.ttf", 24))
    back = button.Button(screen, 300, 300, 80, 30, (41, 181, 99), (32, 85, 53), "Retour", (255, 255, 255), pygame.font.Font("./notes.ttf", 24))
    
    running = True
    while running:
      x,y = pygame.mouse.get_pos()
      run.draw(x, y)
      back.draw(x, y)


      pygame.display.flip()

      for event in pygame.event.get():

        if event.type == pygame.QUIT:
                return True
        if event.type == pygame.MOUSEBUTTONDOWN:
          click_x,click_y = pygame.mouse.get_pos()
                
          if run.action(click_x,click_y):
            return GameState.NEWGAME
          elif back.action(click_x, click_y):
            return GameState.QUIT
        clock.tick(60)

if __name__ == '__main__':
  pygame.init()

  screen = pygame.display.set_mode((600, 500))
  pygame.display.set_caption("Loki - Menu")
  game_state = GameState.TITLE
  
  boucle = True
  while boucle:
    if game_state == GameState.TITLE:
      game_state = title_screen(screen)
    if game_state == GameState.NEWGAME:
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        pygame.display.set_caption("Loki - Generator")
        men = menu(screen)
        test = men.run()
        if test:
            boucle = False
        elif test == False:
            game_state = title_screen(screen)

    if game_state == GameState.QUIT:
      boucle= False

  pygame.quit()
    
  
