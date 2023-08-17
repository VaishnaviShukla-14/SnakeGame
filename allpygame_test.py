import pygame
pygame.init()
gameWindow=pygame.display.set_mode((800,700))
clock= pygame.time.Clock()
fps=40
while True:
      for event in pygame.event.get():
            if event.type==pygame.quit:
                  pygame.quit()
                  quit()



