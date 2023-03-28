import pygame

screen=pygame.display.set_mode((490,390))
pygame.display.set_caption("ball")
clock=pygame.time.Clock()

b_1=pygame.Surface((490,390))
b_2=pygame.Surface((490,390))
pygame.Surface.fill(b_2,(255,255,255))

x=0
y=0

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                if(y+45<=375):
                    y+=20
            if event.key==pygame.K_UP:
                if(y-45>=-25):
                    y-=20
            if event.key==pygame.K_RIGHT:
                if(x+45<=475):
                    x+=20
            if event.key==pygame.K_LEFT:
                if(x-45>=-25):
                    x-=20
        

    screen.fill('white')
    pygame.draw.circle(screen, (255,204,204), (x+25, y+25), 25)
    pygame.display.flip()
    clock.tick(60)