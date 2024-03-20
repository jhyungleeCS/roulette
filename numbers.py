from random import randint

class Roulette():
	def __init__(self, tiles=38):
		self.tiles = tiles
		self.colors = {
		# Green 
		37: 'green', 38: 'green',
		# Red
		1: 'red', 3: 'red', 5: 'red', 7: 'red', 9: 'red',
        12: 'red', 14: 'red', 16: 'red', 18: 'red', 19: 'red',
        21: 'red', 23: 'red', 25: 'red', 27: 'red', 30: 'red',
        32: 'red', 34: 'red', 36: 'red',
        # Black
        2: 'black', 4: 'black', 6: 'black', 8: 'black', 10: 'black',
        11: 'black', 13: 'black', 15: 'black', 17: 'black', 20: 'black',
        22: 'black', 24: 'black', 26: 'black', 28: 'black', 29: 'black',
        31: 'black', 33: 'black', 35: 'black'
		}


	def spin(self):
		print("Spinning Wheel...")
		x = randint(1, self.tiles)
		colors = self.colors
		if x == 37:
			print('0', colors[x])
		elif x == 38:
			print('00', colors[x])
		else: 
			print(x, colors[x]) 
		return x 


game = input("Would you like to play Roulette?(y/n): ")

if game == 'y':
	bank_roll = input("How much would you like to play with today?: $")
	bet_amount = input("How much would you like to bet?: $")
	bet_number = input("What number would you like to bet on? (0, 00, 1-36): ")
	while game == 'y': 
		a1 = Roulette()
		result = a1.spin()
		#print("Bank roll: " + bank_roll)
		if result == int(bet_number): 
			earning = int(bet_amount) * 35 
			bank_roll += earning
			print("Congrats, you won: " + str(earning))
		else: 
			bank_roll = int(bank_roll) - int(bet_amount)
			print("Next time! ")
		if int(bank_roll) <= 0: 
			print("You ran out of money. Come back soon.")
			break
		else: 
			repeat = input("Would you like another spin?(y/n): ")
			if repeat == 'n':
				break
			else: 
				bet_amount = input("How much would you like to bet?: $")
				bet_number = input("What number would you like to bet on? (0, 00, 1-36): ")
else: 
	print("See you soon.")