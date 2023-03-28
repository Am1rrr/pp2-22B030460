from pygame import mixer as mix
import pygame as pg
import os
from tkinter import *
from tkinter import filedialog

Playlist=[]

allsongs = os.listdir(r"/Users/amirkhamraev/sfksmfbkmsf/audio")
for song in allsongs:
       if song.endswith(".mp3"):
           Playlist.append(song)

pg.init()
mix.init()
clock=pg.time.Clock()

screen=pg.display.set_mode((500, 250))
pg.display.set_caption("music player")

icon=pg.image.load("iconn.png")
pg.display.set_icon(icon)

BG=pg.Surface((500,500))
pg.Surface.fill(BG,(241,203,255))
f1=pg.font.SysFont('calibri', 20, True)
f2=pg.font.SysFont('calibri', 15)



play=pg.image.load("play.png")
pause=pg.image.load("pause.png")


next=pg.image.load("next.png")
next2=pg.image.load("next2.png")


prev=pg.image.load("prev.png")
prev2=pg.image.load("prev2.png")


currid=0
currsong=pg.mixer.music.load(Playlist[currid])
pg.mixer.music.play()
pg.mixer.music.pause()
ch=False
ch1=False
ch2=False
tm=0
tm2=0

running=True
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        elif event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                if(ch):
                    pg.mixer.music.pause()
                    ch=0
                else:
                    pg.mixer.music.unpause()
                    ch=1
            if event.key==pg.K_RIGHT:
                currid=(currid+1)%3
                pg.mixer.music.stop()
                pg.mixer.music.load(Playlist[currid])
                pg.mixer.music.play()
                ch1=True
                if not ch :
                    pg.mixer.music.pause()
            if event.key==pg.K_LEFT:
                currid=(currid-1+3)%3
                pg.mixer.music.stop()
                pg.mixer.music.load(Playlist[currid])
                pg.mixer.music.play()
                ch2=True
                if not ch :
                    pg.mixer.music.pause()
                   


                  
    text1=f1.render("Currently playing:", True, (138,25,151))
    text2=f2.render(Playlist[currid], True, (99,20,108))        
    screen.blit(BG, (0,0))
    screen.blit(text1,(25,25))
    screen.blit(text2,(100,50))
    if ch:
        screen.blit(pause, (195,90))
    else:
        screen.blit(play, (195,90))

    if ch1:
        screen.blit(next2, (295,90))
        tm+=1
    else:
        screen.blit(next, (295,90))

    if ch2:
        screen.blit(prev2, (95,90))
        tm2+=1
    else:
        screen.blit(prev, (95,90))

    if tm>=8:
        ch1=False
        tm=0
    if tm2>=8:
        ch2=False
        tm2=0
    pg.display.update()
    clock.tick(60)