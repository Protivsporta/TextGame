from GameOver import GameOver
class Entity:
    
    def __init__(self, name):
    	self.name = name

class MainHero(Entity):

	def __init__(self, hitpoint, damage):
	    self.hp = int(hitpoint)
	    self.dmg = int(damage)


class Characters(Entity):
	
	def __init__(self, hitpoint, damage):
	    self.hp = int(hitpoint)
	    self.dmg = int(damage)

class Weapon(Entity):
	
	def __init__(self, name, damage):
		self.name = name
		self.dmg = int(damage)

Hero = MainHero(100, 20)
Krovosos = Characters(40, 25)
HischniyUyeber = Characters(40, 65)
Key = Entity('ключ')
Fakel = Entity('факел')
Mech = Weapon('меч', 20)
Inventory = []
	

