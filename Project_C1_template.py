import pygame, sys

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))


face=pygame.Rect(100,200,200,200)

eye1=pygame.Rect(120,240,60,30)

eye2=pygame.Rect(220,240,60,30)

mouth=pygame.Rect(130,350,140,10)

while True:    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
    pygame.draw.rect(screen,(120,120,120),face)  
    pygame.draw.rect(screen,(255,0,0),eye1)
    pygame.draw.rect(screen,(255,0,0),eye2)
    pygame.draw.rect(screen,(200,200,200),mouth)
    
    pygame.display.update()
    clock.tick(30)



