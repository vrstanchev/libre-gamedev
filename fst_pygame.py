import pygame
pygame.init()
screen_size=pygame.display.setmode([600,600])
x=int(input("enter number:\n"))
if(x%2==0):
	screen_size.fill((255,255,255))
	pygame.draw.circle(screen_size,(0,0,255),(250,250),(75);
	pygame.display.flip()
else:
	pygame.quit();
