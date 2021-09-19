import pygame, random

# Window Setup
windowWidth = 800
windowHeight = 600
pygame.init()
win = pygame.display.set_mode((windowWidth, windowHeight))

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

stickForwardImage = pygame.image.load("Color Wall\FinnStick.png").convert_alpha()

colors = [
    (255, 165, 0),
    (138,43,226),
    (255, 0, 0),
    (127,255,0)
]

changeRectColor = (255,255,255)

class Stickman:
    def __init__(self, pos):
        self.sprite = stickForwardImage
        self.dead = False
        self.score = 0
        self.pos = pos
        self.sprite = pygame.transform.scale(self.sprite, (75, 75))

    def draw(self):
        if not self.dead:
            win.blit(self.sprite, self.pos)

stickman = Stickman((20,230))

class ColorWall:
    def __init__(self, color, x):
        self.x = x
        self.color = color

    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, 0, 75, 600))

    def update(self):
        if not stickman.dead:
            self.x -= 3
            if self.x <= -75:
                self.x = 800
                stickman.score += 1
                print(stickman.score)
                self.color = random.choice(colors)
            elif self.x >= 20 and self.x <= 95 and changeRectColor != self.color:
                stickman.dead = True


running = True

walls = []
for i in range(2):
    walls.append(ColorWall(random.choice(colors), (i+3)*875/2))

changeWallColor = (255, 255, 255)
scoreDisplay = font.render("Your Score: 0", True, (50, 50, 50))
scoreDisplayText = str(stickman.score)


while running:
    # Window stuff
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((135,206,235))

    #Drawing
    stickman.draw()

    #Change player color
    if not stickman.dead:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            #Orange
            changeRectColor = colors[0]
        elif keys[pygame.K_2]:
            #Purple
            changeRectColor = colors[1]
        elif keys[pygame.K_3]:
            #Red
            changeRectColor = colors[2]
        elif keys[pygame.K_4]:
            #Chartruese
            changeRectColor = colors[3]

    pygame.draw.rect(win, (changeRectColor), (20, 300, 75, 300))
    for wall in walls:
        wall.draw()
        wall.update()
    scoreDisplayText = font.render("Your Score: " + str(stickman.score), True, (0, 0, 0))
    win.blit(scoreDisplayText, (25, 15))
    pygame.display.update()



pygame.quit()
