from pygame import *
init()


WINDOW_SIZE = 800,600

display.set_icon(image.load(""))
display.set_caption("AGARIO")
window = display.set_mode(WINDOW_SIZE)

clk = time.Cl   ock()
FPS = 60

running = True
lose = False






while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    window.fill((12,12,12))
    

    display.update()
    clk.tick(FPS)

