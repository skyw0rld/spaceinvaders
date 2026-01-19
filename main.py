from pygame import *

init()

invaderList = []
FPS = 60


class Invader:
    def __init__(self, x, y):
        SIZE = 30
        self.img = transform.scale(image.load("spaceinvader.png"), (SIZE,SIZE))
        self.rect = Rect(x, y, self.img.get_width(), self.img.get_height())
        self.dx = 1
        self.dy = 0
    def draw(self, screen):
        screen.blit(self.img, self.rect)
    def update(self):
        global width, height
        if self.rect.right + self.dx >= width or self.rect.left + self.dx <= 0:
            self.dy = 20
            self.dx = -self.dx
        self.rect.x += self.dx
        self.rect.y += self.dy
        self.dy = 0
       
class InvaderGroup:
	def __init__(self):
		self.invaderList = []
		for i in range(0,10):
			for j in range(0,5):
				x = 100 + (i * 40)
				y = 100 + (j * 40)
				self.invaderList.append(Invader(x,y))
	def draw(self,screen):
		for i in self.invaderList:
			i.draw(screen)





width = 800
height = 600

c = time.Clock()
window = display.set_mode((width, height))

endGame = False

x = 30
count = 0

while count < 6:  # creates 6 invaders
    newInvader = Invader(x, 60)
    invaderList.append(newInvader)
    x += 120
    count += 1

ig = InvaderGroup()
while not endGame:
    for e in event.get():
        if e.type == QUIT:
            endGame = True

    window.fill((0, 0, 0))

    for invader in invaderList:
        invader.draw(window)
    
    ig.draw(window)
    c.tick(FPS)
    display.flip()
