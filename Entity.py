class Entity:
    
    def __init__(self, name):
    	self.name = name

class Characters(Entity):
	
	def __init__(self, hitpoint, damage, owner ):
	    self.hp = hitpoint
	    self.dmg = damage
    
    def move_on(self, room_number):
    	self.rn = room_number
    	room_number += 1 


class Weapon(Entity):
	
	def __init__(self, damage):
		self.dmg = damage
	
	def attack(self, enemy, hitpoint):
		enemy.hp = hitpoint
		enemy.hp -= self.dmg

