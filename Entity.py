class Entity:
    
    def __init__(self, name):
    	self.name = name

class Characters(Entity):
	
	def __init__(self, hp, dmg):
		self.hp = hp
    	self.dmg = dmg
    
    def move_on(self, room_number):
    	self.room_number = room_number
    	room_number += 1 

    def look around(self)
    	self.objet

class Weapon(Entity):
	
	def __init__(self, dmg):
		self.dmg = dmg
	
	def attack(self, enemy, hp):
		enemy.hp = hp
		enemy.hp -= self.dmg

