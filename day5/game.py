import random

class Ninja: 
	def __init__(self, ninja_name, level, weapon_list):
		#creates a name variable for the ninja
		#creates a weapon variable for the ninja
		self.name = ninja_name
		self.weapons = weapon_list
		self.level = level

	def describe(self):
		#creates a function to describe the ninja
		print 'I am Ninja ' + self.name + ' (level ' + str(self.level) + ') and I can use these weapons: ' 
		for weapon in self.weapons:
			print weapon

	def dead(self):
		return self.level == 0

	def fight(self, other_ninja):

		if self.dead() or other_ninja.dead():
#			print 'Dead ninja, no fight'
			return 

		if self.level > other_ninja.level:
			#Self is stronger, other_ninja is weaker.
			if self.miracle(1):
				other_ninja.win(self)
			else:
				self.win(other_ninja)

		elif self.level < other_ninja.level:
			#Self is weaker, other_ninja is stronger.
			if self.miracle(1):
				self.win(other_ninja)
			else:
				other_ninja.win(self)
		
		else: #Equal levels
			if self.miracle(5):
				self.win(other_ninja)
			else:
				other_ninja.win(self)

		if self.dead():
			pass
#			print 'Ninja ' + self.name + ' had died. :('

	def win(self, other_ninja):
		# The outcome of the fight that I won it.
		self.level += 1
		other_ninja.level -= 1
#		print 'Ninja ' + self.name + ' wins'

	def miracle(self, likelihood):
		# likelihood the miracle is between 0 and 10.
		return random.randint(1, 10) <= likelihood


class Game:

	def __init__(self, ninja_list):
		self.ninjas = ninja_list

	def play(self):
		fights = 0 
		count = 0
		while not self.is_game_over():
			fights += 1
#			print fights
			#randomize ninjas after each round of battles
#			if count >= len(self.ninjas):
#				random.shuffle(self.ninjas)
			
			self.ninjas[count % len(self.ninjas)].fight(self.ninjas[(count + 1) % len(self.ninjas)])
			if self.ninjas[count % len(self.ninjas)].level == 0:
				self.ninjas.remove(self.ninjas[count % len(self.ninjas)])
				count = 0
			elif self.ninjas[(count + 1) % len(self.ninjas)].level == 0:
				self.ninjas.remove(self.ninjas[(count + 1) % len(self. ninjas)])
				count = 0
			else:
				count += 1
#		print self.winner()
		return fights

	def is_game_over(self):
		#returns true if game is over
		return len(self.ninjas) == 1
			
	def winner(self):
		return self.ninjas[0].name


total = 0
for i in range (0,1000000):
	ninjas = [Ninja('Caro', 5, ['sword', 'dart']), Ninja('Bob', 5, ['sword', 'dart']), Ninja('Xun', 5, ['sword', 'dart']), Ninja('Carl', 5, ['sword', 'dart']), Ninja('Billy Bob', 5, ['sword', 'dart']), Ninja('Angela', 5, ['sword', 'dart']), Ninja('Spongebob', 5, ['sword', 'dart']), Ninja('Jacob', 5, ['sword', 'dart']), Ninja('James', 5, ['sword', 'dart']), Ninja('Nick', 5, ['sword', 'dart'])]
	game = Game(ninjas)
	total += game.play()
	print total
print 'Average number of fights is: %i' %(total/1000000.0)



