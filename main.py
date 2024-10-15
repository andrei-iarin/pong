import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
running = True

ball = Ball('white', 20)
ball.rect.x = 345
ball.rect.y = 195

paddleA = Paddle('white', 20, 150)
paddleA.rect.x = 20
paddleA.rect.y = 275


paddleB = Paddle('white', 20, 150)
paddleB.rect.x = 1040
paddleB.rect.y = 275

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

scoreA = 0
scoreB = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(7)
    if keys[pygame.K_s]:
        paddleA.moveDown(7)
    if keys[pygame.K_UP]:
        paddleB.moveUp(7)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(7)    
 
    all_sprites_list.update()
    
    if ball.rect.x>=1060:
        scoreA += 1
        pygame.time.wait(1000)
        paddleA.reset()
        paddleB.reset()
        ball.rect.x = 540
        ball.rect.y = 360
    if ball.rect.x<=0:
        scoreB += 1
        pygame.time.wait(1000)
        paddleA.reset()
        paddleB.reset()        
        ball.rect.x = 540
        ball.rect.y = 360       
    if ball.rect.y>700:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1] 

    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    screen.fill('black')
    all_sprites_list.draw(screen) 

    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, 'white')
    screen.blit(text, (360,10))
    text = font.render(str(scoreB), 1, 'white')
    screen.blit(text, (720,10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()