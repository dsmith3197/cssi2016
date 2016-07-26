import random

class Ninja: 
	def __init__(self, ninja_name, weapon_list, level):
		#creates a name variable for the ninja
		#creates a weapon variable for the ninja
		self.name = ninja_name
		self.weapons = weapon_list
		self.level = level

	def describe(self):
		#creates a function to describe the ninja
		print 'I am Ninja ' + self.name + ' (level ' + str(self.level) + ') and I can use these weapons: ' + " ".join(self.weapons)

	def dead(self):
		return self.level == 0

	def fight(self, other_ninja):

		if self.dead() or other_ninja.dead():
			print 'Dead ninja, no fight'
			return

		if self.level > other_ninja.level:
			#Self is stronger, other_ninja is weaker.
			if miracle(1):
				other_ninja.win(self)
			else:
				self.win(other_ninja)

		elif self.level < other_ninja.level:
			#Self is weaker, other_ninja is stronger.
			if miracle(1):
				self.win(other_ninja)
			else:
				other_ninja.win(self)
		
		else: #Equal levels
			if miracle(5):
				self.win(other_ninja)
			else:
				other_ninja.win(self)

		if self.dead():
				print 'Ninja ' + self.name + ' had died. :('

	def win(self, other_ninja):
		# The outcome of the fight that I won it.
		self.level += 1
		other_ninja.level -= 1
		print 'Ninja ' + self.name + ' wins'

	def miracle(likelihood):
		# likelihood the miracle is between 0 and 10.
		return random.randint(1, 10) <= likelihood

