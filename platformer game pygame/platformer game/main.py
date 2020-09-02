import pygame

pygame.init()

win = pygame.display.set_mode((850, 480))

pygame.display.set_caption("Corona Game")

walk_right = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walk_left = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')


clock = pygame.time.Clock()

x = 250
y = 416
width = 64
height = 64
ve = 5
screenwidth = 850
screenheight = 480

is_jump = False
jump_count = 10

left = False
right = False
walk_count = 0


def redraw():
    global walk_count
    
    win.blit(bg, (0,0))

    if walk_count + 1 >= 27:
        walk_count = 0

    if left:
        win.blit(walk_left[walk_count//3],(x,y))
        walk_count += 1
    elif right:
        win.blit(walk_right[walk_count//3], (x,y))
        walk_count += 1
    else:
        win.blit(char, (x,y))
    pygame.display.update()

running = True
while running:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= ve
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < (screenwidth - width):
        x += ve
        left = False
        right = True
    else:
        right = False
        left = False
        walk_count = 0
    if not (is_jump):
        if keys[pygame.K_SPACE]:
            is_jump = True
            right = False
            left = False
            walk_count = 0
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10
    redraw()

pygame.quit()

    

