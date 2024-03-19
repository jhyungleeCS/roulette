from random import randint

class Roulette(): 
    def __init__(self, tiles=38):
        self.tiles = tiles 
    
    def spin(self):
        print("Spinning Wheel...")

action = Roulette() 
action.spin()