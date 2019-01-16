import Rooms
import Entity

class World:

    def __init__(self):

    	Hero = MainHero(100, 20)
    	Krovosos = Characters(40, 25)
    	HischniyUyeber = Characters(40, 65)
    	Key = Entity('ключ')
    	Fakel = Entity('факел')
    	Zelie = Entity('зелье')
    	Mech = Weapon('меч', 20)

    	for i in range(1,6):

    		if i = 1:
    			print('В погоне за сокровищами капитана Пистолетова ты оказался в подземелье. Ты ранен в левую руку, так что можешь пользоваться только правой. Осматривая помещение, находишь сундук с двумя предметами: ', Key.name, Fakel.name, '. Ты можешь взять только один из них!')
    			yourchoice = input
