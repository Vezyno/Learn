

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


myhero1 = Hero('Vurdalak', 5, 'Ork')
myhero2 = Hero('Nikita', 4, 'Human')

myhero1.show_hero()
myhero2.move()
myhero1.level_up()
myhero1.show_hero()
myhero1.set_health(70)
myhero1.show_hero()
        
