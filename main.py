from pygame import *
## https://uobschool.sharepoint.com/:p:/r/sites/ComputerScienceStudentResources/_layouts/15/Doc.aspx?sourcedoc=%7B218459FF-B59C-47CB-829B-BDFC78ADD6C4%7D&file=Space%20invaders.pptx&action=edit&mobileredirect=true


init()

width = 800
height = 600
iOFFSET = 40


c = time.Clock()
FPS = 60

screen = display.set_mode((width,height))

invaderList = []

class Invader: # defines invader
	def __init__(self, x, y): ## constructor (must be defined as __init__)
		SIZE = 40
		self.img = image.load("thumbnail_invader.png") ##loads the picture of invader
		self.img = transform.scale(self.img, (SIZE, SIZE)) ## scales it to a said size (e.g 40, 40)
		self.dx = 1 #direction
		self.rect = Rect(x,y, ## labels x,y
		                 self.img.get_width(), ##gets the width of the object
		                 self.img.get_height() ##gets the height of the object
		                 ) 
		           
	def draw(self, screen): ## this is considered a method (a regular function)
		screen.blit(self.img, self.rect) ## places image on rectangle
	def update(self):
		global width, height
		# checks the boundaries
		if self.rect.right + self.dx >= width or self.rect.left + self.dx <= 0:
			self.dx = self.dx * -1
		self.rect.x += self.dx
	def changeDirection(self):
		self.dx *= 1
		self.rect.y += 40
	def checkForWallCollision(self):
		return self.rect.right + self.dx >= width or self.rect.left + self.dx <= 0

		
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
	def update(self):
		has_collided = False
		for i in self.invaderList:
			if i.checkForWallCollision():
				has_collided = True
		if has_collided:
			for i in self.invaderList:
				i.changeDirection()
		for i in self.invaderList:
			i.update()

class Ship:
	def __init__(self):
		self.rect = Rect(400,520,40,80)
		self.img = image.load("ship.png")
		self.img = transform.scale(self.img, (40,80))
		self.dx = 0
	def update(self):
		global width
		if self.rect.left + self.dx < 0 or self.rect.right + self.dx > width:
			self.stop()
		self.rect.x += self.dx
	def moveLeft(self):
		self.dx = -5
	def moveRight(self):
		self.dx = 5
	def stop(self):
		self.dx = 0
	def draw(self,screen):
		screen.blit(self.img,self.rect)
		
class Bullet:
	def __init__(self, x,y):
		self.rect = Rect(x,y,5,10)
	
	def update(self):
		self.rect.y -= 5
	
	def draw(self,screen):
		draw.rect(screen, (255,255,255), self.rect)
endGame = False ##endgame boolean
screen.fill((255,255,255))
ig = InvaderGroup()
player = Ship()

while not endGame: ## gameloop (while the game hasn't finished)
	for e in event.get():
		if e.type == QUIT:
			endGame = True
		if e.type == KEYDOWN:
			if e.key == K_LEFT:
				player.moveLeft()
			elif e.key == K_RIGHT:
				player.moveRight()
		if e.type == KEYUP:
			if e.key == K_LEFT or e.key == K_RIGHT:
				player.stop()
					
			
	count = 0
	x = 10
	y = 20
	
	row = 0
	col = 0
		
	screen.fill((0,0,0))
	ig.update()
	ig.draw(screen)
	player.update()
	player.draw(screen)	

	c.tick(FPS)
	display.flip() ## shows the screen (the game)
