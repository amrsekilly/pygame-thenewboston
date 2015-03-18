import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
# Set name for the title
pygame.display.set_caption('Brave SNAKEY')

pygame.display.update()

gameExit = False

while not gameExit:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      gameExit = True


pygame.quit()
quit()
