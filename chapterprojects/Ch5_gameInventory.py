#Fantasy Game Inventory
#Chapter 5 of Automate the Boring Stuff with Python
'''
You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.

Write a function named displayInventory() that would take any possible “inventory” and display it like the following:

Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62

...

Imagine that a vanquished dragon’s loot is represented as a list of strings like this:

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing the player’s inventory (like in the previous project) and the addedItems parameter is a list like dragonLoot. The addToInventory() function should return a dictionary that represents the updated inventory. Note that the addedItems list can contain multiples of the same item. 
'''

import logging, pytest
import io, sys

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.INFO)


def displayInventory(inventory):
	logging.debug('Start of displayInventory(%s)' % (str(inventory)))
	item_total = 0
	print ("Inventory:")
	
	logging.debug('Start of item loop with this dictionary: (%s)' % (str(inventory)))
	for key, value in inventory.items():
		logging.debug('Loop with key and value: %s, %s' % (str(key), str(value)))
		print(str(value) + " " + str(key))
		item_total += value
	print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
	logging.debug('Start of addToInventory(%s, %s)' % (str(inventory), str(addedItems)))
	outputInv = inventory
	for element in addedItems:
		#if element exists as a key in the dictionary increment the value
		logging.debug('Adding element (%s) to inventory, current value: (%s: %s)' % (str(element), str(element), str(outputInv.get(element, 'NONE'))))
		outputInv.setdefault(element, 0) #Create an item in the inventory if it does not exist
		outputInv[element] += 1 #Increment the item count
		logging.debug('Inventory value is now: (%s: %s)' % (str(element), str(outputInv[element])))
	return outputInv
	
class TestDisplayInventory():
	test_dictionary = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
		
	def test_displayInventory_output(self):
		#Redirect stdout
		old_stdout = sys.stdout
		sys.stdout = mock_stdout = io.StringIO()
		
		displayInventory(self.test_dictionary)
		
		#Restore stdout
		sys.stdout = old_stdout
		
		for key, value in self.test_dictionary.items():
			testValue = str(value) + " " + str(key)
			assert testValue in mock_stdout.getvalue()
			
	def test_displayInventory_total(self):
		#Redirect stdout
		old_stdout = sys.stdout
		sys.stdout = mock_stdout = io.StringIO()
		
		displayInventory(self.test_dictionary)
		
		#Restore stdout
		sys.stdout = old_stdout
		
		testValue = 0
		
		for key, value in self.test_dictionary.items():
			testValue += value
			
		testValue = "Total number of items: " + str(testValue)
		
		assert testValue in mock_stdout.getvalue()

class TestAddToInventory():
	test_tuples = [
	({'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12},
	['Dragon Helm', 'gold coin', 'rope', 'arrow', 'arrow', 'gold coin'],
	{'rope': 2, 'torch': 6, 'gold coin': 44, 'dagger': 1, 'arrow': 14, 'Dragon Helm':1}),
	
	({'gold coin': 42, 'rope': 1},
	['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'],
	{'gold coin': 45, 'rope': 1, 'dagger':1, 'ruby':1})
	]
	
	def test_addToInventory(self):
		for inventory, loot, expected_inventory in self.test_tuples:
			output = addToInventory(inventory, loot)
			assert output == expected_inventory

			
if  __name__ =='__main__':
	test_dictionary = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
	displayInventory(test_dictionary)
	print()
	
	inv = {'gold coin': 42, 'rope': 1}
	dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
	inv = addToInventory(inv, dragonLoot)
	displayInventory(inv)