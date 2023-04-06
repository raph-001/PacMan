##imports
import pygame
import time
import random as rdm

pygame.init()
screen = pygame.display.set_mode((1426, 690))


##variable
nombre_de_gosts = 4
continuer = 1
liste_murs = []
liste_tournant = []
next_direction = ''
liste_bonbon = []
liste_rect_bonbon = []
nombre_bonbon_manges = 0




##caret de 31x15
carte =	[
  "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%",
  "%,...,%,...,.......,...,%,...,%",
  "%.%%%.%.%%%.%%%%%%%.%%%.%.%%%.%",
  "%.%,.,.,%,.,..,%,..,.,%,.,.,%.%",
  "%,.,%%%.%.%%%%.%.%%%%.%.%%%,.,%",
  "%%%.%,.,%.%,..,.,..,%.%,.,%.%%%",
  "%,.,%.%%%.%.%%% %%%.%.%%%.%,.,%",
  "%.%%%,...,.,%GG GG%,.,...,%%%.%",
  "%,.,%.%%%.%.%%%%%%%.%.%%%.%,.,%",
  "%%%.%,.,%.%,..,.,..,%.%,.,%.%%%",
  "%,.,%%%.%.%%%%.%.%%%%.%.%%%,.,%",
  "%.%,.,.,%,.,..,%,..,.,%,.,.,%.%",
  "%.%%%.%.%%%.%%%%%%%.%%%.%.%%%.%",
  "%,...,%,...,...,...,...,%,...,%",
  "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
  ]

class gost:
	def init__(self, xx, yy):
		self.vitesse = 2  
		self.couleur = (rdm.randint(1,255), rdm.randint(1,255), rdm.randint(1,255))
		self.gost_rect = pygame.Rect(xx, yy, 46, 46)
		self.direction = 'right'


	def gosts_move(self):
		if self.direction == 'up':
			self.gost_rect.y -= self.vitesse
		if self.direction == 'down':
			self.gost_rect.y += self.vitesse
		if self.direction == 'right':
			self.gost_rect.x += self.vitesse
		if self.direction == 'left':
			self.gost_rect.x -= self.vitesse

	def print_gost(self):
		pygame.draw.rect(screen, self.couleur, self.gost_rect)


	def modifier_direction_gost(self):
		direction_number = rdm.randint(1,6)
		if direction_number == 1:
			self.direction = 'up'
		if direction_number == 2:
			self.direction = 'down'
		if direction_number == 3:
			self.direction = 'left'
		if direction_number == 4:
			self.direction = 'right'

			##si le nombre est de 5 ou 6, ne pas changer de direction


	def gosts_collisions(self):

		##bloc tournant
		for i in liste_tournant:
			if [self.gost_rect.x, self.gost_rect.y] == i:
					e.modifier_direction_gost()

		##collision avec mur
		if pygame.Rect.collidelist(self.gost_rect,liste_murs) != -1:
			if self.direction == 'up':
				self.gost_rect.y += self.vitesse
			if self.direction == 'down':
				self.gost_rect.y -= self.vitesse
			if self.direction == 'right':
				self.gost_rect.x -= self.vitesse
			if self.direction == 'left':
				self.gost_rect.x += self.vitesse
			e.modifier_direction_gost()


class pacman:

	def init__(self):
		self.vitesse = 1
		self.direction = ''
		self.pacman_rect = pygame.Rect(690, 598, 46, 46)
		self.droit_de_changer_direction_pacman = 0

	def print_pacman(self):
		pygame.draw.rect(screen, '#FFFF00', self.pacman_rect)

	def pacman_move(self):
		if self.direction == 'up':
			self.pacman_rect.y -= self.vitesse
		if self.direction == 'down':
			self.pacman_rect.y += self.vitesse
		if self.direction == 'right':
			self.pacman_rect.x += self.vitesse
		if self.direction == 'left':
			self.pacman_rect.x -= self.vitesse

	def modifier_direction_pacman(self):
		for i in liste_tournant:
			if [self.pacman_rect.x, self.pacman_rect.y] == i:
					self.droit_de_changer_direction_pacman = 1

		if self.droit_de_changer_direction_pacman == 1:
			self.direction = next_direction
		self.droit_de_changer_direction_pacman = 0

	def collisions_pacman(self):
		if pygame.Rect.collidelist(self.pacman_rect,liste_murs) != -1:
			if self.direction == 'up':
				self.pacman_rect.y += self.vitesse
			if self.direction == 'down':
				self.pacman_rect.y -= self.vitesse
			if self.direction == 'right':
				self.pacman_rect.x -= self.vitesse
			if self.direction == 'left':
				self.pacman_rect.x += self.vitesse

class bonbon:
	def init__(self):
		self.couleur = (255,255,0)







def print_carte():
	compteur = 0
	x,y = 0,0
	for colonne in range(0,15):
		x = 0
		for position in range(0,31):
			if carte[colonne][position] == '%':
				pygame.draw.rect(screen, (50,50,50), pygame.Rect(x, y, 46, 46))
			if carte[colonne][position] == '.':
				pygame.draw.rect(screen, (100,100,100), pygame.Rect(x, y, 46, 46))
				pygame.draw.circle(screen, (liste_bonbon[compteur].couleur), (x+23,y+23), 5)
				compteur += 1
			if carte[colonne][position] == ',':
				pygame.draw.rect(screen, (100,100,100), pygame.Rect(x, y, 46, 46))
				pygame.draw.circle(screen, (liste_bonbon[compteur].couleur), (x+23,y+23), 5)		
				compteur += 1

			x += 46
		y += 46


def print_carte_first_time():
	compteur = 1
	x,y = 0,0
	for colonne in range(0,15):
		x = 0
		for position in range(0,31):
			if carte[colonne][position] == '%':
				pygame.draw.rect(screen, (50,50,50), pygame.Rect(x, y, 46, 46))
				liste_murs.append(pygame.Rect(x, y, 46, 46))
			if carte[colonne][position] == '.':
				pygame.draw.rect(screen, (100,100,100), pygame.Rect(x, y, 46, 46))
				liste_rect_bonbon.append(pygame.Rect(x,y,46,46))
				compteur += 1
			if carte[colonne][position] == ',':
				pygame.draw.rect(screen, (100,100,100), pygame.Rect(x, y, 46, 46))
				liste_rect_bonbon.append(pygame.Rect(x,y,46,46))
				compteur += 1
				liste_tournant.append([x,y])		

			x += 46
		y += 46

	return compteur

def collisions_entre_monstre_et_pacman():
	for e in liste_gosts:
		if pacman.pacman_rect.colliderect(e.gost_rect) == True:
			pygame.quit()

def mange():
	compteur = 0
	for x in liste_rect_bonbon:
		if pacman.pacman_rect.colliderect(x) == True:
			liste_bonbon[compteur].couleur = (100,100,100)
			global nombre_bonbon_manges
			nombre_bonbon_manges = nombre_bonbon_manges + 1
		compteur += 1

def fin():
	if nombre_bonbon_manges > 30 or nombre_bonbon_manges == 30:
		pygame.quit()




compteur = print_carte_first_time()
pacman = pacman()
pacman.init__()
a = gost()
b = gost()
c = gost()
d = gost()

a.init__(46,46)
b.init__(1334,598)
c.init__(1334,46)
d.init__(46,598)
liste_gosts = [a,b,c,d]

for z in range(1,compteur):
	liste_bonbon.append(bonbon())
for z in liste_bonbon:
	z.init__()

while continuer == 1:

	print_carte()
	for e in liste_gosts:
		e.gosts_move()
		e.gosts_collisions()		
		e.print_gost()
	pacman.modifier_direction_pacman()
	pacman.pacman_move()
	pacman.modifier_direction_pacman()
	pacman.collisions_pacman()
	pacman.print_pacman()
	collisions_entre_monstre_et_pacman()
	mange()
	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continuer = 0
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				next_direction = 'up'
			if event.key == pygame.K_DOWN:
				next_direction = 'down'
			if event.key == pygame.K_LEFT:
				next_direction = 'left'
			if event.key == pygame.K_RIGHT:
				next_direction = 'right'


	time.sleep(0.0001)









