import random

def dice(sides):
    return random.randrange(0, sides + 1)

class Player():
    def __init__(self, isPlayer=False):
        self.loc = (0, 0)
        self.icon = "☆"
        self.troops = 1000
        self.hasNukes = False
        self.isAlive = True
        self.isPlayer = isPlayer

    def recruit(self, conscripts):
        self.troops += conscripts

    def move(self, newX, newY):
        self.loc = (newX, newY)

    def kill_soldiers(self, casualties):
        self.troops -= casualties
        if self.troops <= 0:
            self.isAlive = False


class Region():
    def __init__(self, coord):
        self.coord = coord
        self.population = random.randrange(100, 5001)
        self.isSovereign = True
        self.isPlayer = False
        self.isEnemy = False
        self.icon = "□"
        self.defenses = 0

    def kill_populace(self, casualties, assailant):
        self.population -= casualties
        if self.population <= 0 and self.isSovereign:
            self.isSovereign = False
            if assailant == "player":
                self.isPlayer = True
            elif assailant == "enemy":
                self.isEnemy = True
        elif self.population <= 0 and self.isPlayer:
            self.isEnemy = True
        elif self.population <= 0 and self.isEnemy:
            self.isPlayer = True

    def build_defenses(self):
        built = dice(6)
        if built > 1 and built < 6:
            self.defenses += built
        elif built == 6:
            self.defenses += 36
        elif self.defenses == 1:
            self.defenses -= 6
        if self.defenses <= 0:
            self.defenses = 0