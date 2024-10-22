class Hero():
    """Class to create Hero for our Game"""
    def __init__(self, name, level, race):
        """Initiate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
    
    def show_hero(self):
        """Print all parameters of Hero"""
        discription = ('Name is '+ self.name + ' Level is ' + str(self.level) + ' Health is ' + str(self.health)).title()
        print(discription)

    def level_up(self):
        """Upgrade level of this Hero"""
        self.level += 1

    def move(self):
        """Start moving Hero"""
        print('Hero ' + self.name + ' start moving...')

    def set_health(self, new_health):
        """Change health of hero"""
        self.health = new_health

# --------------------------------------------------------------

class SuperHero(Hero):
    """Class to create a Super Hero"""
    def __init__(self, name, level, race, magiclevel):
        """Initiate our super hero"""
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.magic = 100
    
    def makemagic(self):
        """Use magic"""
        self.magic -= 10

    def show_hero(self):
        discription = ('Name is '+ self.name + ' Level is ' + str(self.level) + ' Health is ' + str(self.health) + f'Magic is {str(self.magic)}').title()
        print(discription)
        
