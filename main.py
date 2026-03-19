from pygame import *
from math import hypot
from random import randint
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

init()

sock = socket(AF_INET,SOCK_STREAM)
sock.connect(("localhost",8080))
my_data = list(map(int, sock.recv(64).decode().strip().split(",")))
my_id = my_data[0]
sock.setblocking(False)

window_size = 1000,1000
window = display.set_mode(window_size)
display.set_caption("Agario")
display.set_icon(image.load("ico_mini.png"))
FPS = 60
clock = time.Clock()
def receive_data():
    global all_players,running,lose
    while running:
        try:
            data = sock.recv(1024).decode().strip()
            if data == "LOSE":
                lose = True
            elif data:
                parts = data.strip("|").split("|")
                all_players = [list(map(int, part.split(",")[:4])) #[:4]
                               for part in parts if len(part.split(",")) == 5] # 4 ---> 5
        except:
            pass
class Player():
    def __init__(self,x,y,r,name,color=(randint(20,255),randint(20,255),randint(20,255))):
        self.x = x
        self.y = y
        self.r = r
        self.name = name
        self.color = color
    def draw(self,scale): draw.circle(window,self.color,(self.x,self.y),self.r * scale)
    def move(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.y -= 5
        if keys[K_s]:
            self.y += 5
        if keys[K_a]:
            self.x -= 5
        if keys[K_d]:
            self.x += 5
class Food():
    def __init__(self,x,y,r,c):
        self.x = randint(-2000,2000)
        self.y = randint(-2000,2000)
        self.r = 10
        self.c = (randint(5,15),randint(5,15),randint(5,15))
    def draw(self):
        draw.circle(window,self.c,(self.x,self.y),self.r)
    def cheack_collision(self,player):
        dx = self.x - player.x
        dy = self.y - player.y
        return hypot(dx,dy) < self.r + player.r
running = True
lose = False
f = font.SysFont("Arial",50)
foods = [Food() for _ in range(300)]
my_Player = Player(my_data[1],my_data[2],my_data[3],"Player")
all_players = []

while running:

    window.fill((12,12,12))
    display.update()
    clock.tick(FPS)
    
    scale = max(0.3, min(50, my_Player.r / 50))
    for p in all_players:
        if p[0] != my_id: continue
        sx = int((p[1] - my_Player.x) * scale + window_size[0] // 2)
        sy = int((p[2] - my_Player.y) * scale + window_size[1] // 2)
        draw.circle(window,(0,255,0),(sx,sy),int(p[3]*scale))
    to_remove = []
    for f in foods:
        if f.cheack_collision(my_Player):
            to_remove.append(f)
            my_Player.r += int(f.r * 0.5)
        else:
            sx = int((f.x - my_Player.x) * scale + window_size[0] // 2)
            sy = int((f.y - my_Player.y) * scale + window_size[1] // 2)
            draw.circle(window,f.c,(sx,sy),int(f.r*scale))
    for f in to_remove:
        foods.remove(f)
    if lose:
        t = f.render("You Lose!",True,(244,0,0))
        window.blit(t,(window_size[0]//2 - t.get_width()//2,window_size[1]//2 - t.get_height()//2))
    try:
        msg = f"{my_id},{my_Player.x},{my_Player.y},{my_Player.r},{my_Player.name}" # {my_Player.name}
        sock.send(msg.encode())
    except: pass

    for e in event.get():
        if e.type == QUIT:
            running = False