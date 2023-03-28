import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((604, 544))
pygame.display.set_caption("clock")
clock=pygame.time.Clock()

rama=pygame.image.load('mickeyclock.png')
# body=pygame.image.load('mickeyclock.png')

min=pygame.image.load('handr.png')
minrec=min.get_rect()
minrec.center=(300,250)
mincnt=-5

sec=pygame.image.load('handl.png')
secrec=sec.get_rect()
secrec.center=(300,250)
seccnt=-5

currt=datetime.datetime.now()

seccnt=currt.second
mincnt=currt.minute

running = True

while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running=False
                        
        screen.blit(rama,(0,0))

        minhand1=pygame.transform.rotate(min, -1*((6*mincnt)%360))
        minrec1=minhand1.get_rect()
        minrec1.center=minrec.center
        screen.blit(minhand1, minrec1)

        # screen.blit(body,(260,170))

        sechand1=pygame.transform.rotate(sec, -1*((6*seccnt+305)%360))
        secrec1=sechand1.get_rect()
        secrec1.center=secrec.center
        screen.blit(sechand1, secrec1)

        currt=datetime.datetime.now()
        seccnt=currt.second
        mincnt=currt.minute


        pygame.display.update()
        clock.tick(60)