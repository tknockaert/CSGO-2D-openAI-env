class Agent :
    
    def __init__(self,x,y,orientation,team = 'CT', weapon = 'AK', smoke = False, molotov = False, flash1 = False, flash2 = False, nade = False,life = 100):
        self.x = x #position x
        self.y = y #position y
        self.orientation = orientation #orientation en degré
        self.team = team #equipe
        self.weapon = weapon #arme equipee
        self.smoke = smoke
        self.molotov = molotov
        self.flash1 = flash1
        self.flash2 = flash2
        self.nade = nade
        self.shooting = False
        self.life = life     