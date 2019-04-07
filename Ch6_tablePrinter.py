#Table Printer
#Chapter 6 of Automate the Boring Stuff with Python
'''
Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

Your printTable() function would print the following:

  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
'''

import logging, pytest
import io, sys

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.INFO)

def printTable(table):
	logging.debug('Start of printTable(%s)' % (str(table)))
	pass

class TestPrintTable():
	tableData = [['apples', 'oranges', 'cherries', 'banana'],
				['Alice', 'Bob', 'Carol', 'David'],
				['dogs', 'cats', 'moose', 'goose']]
	expected = '''	  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose'''
  
	def test_printTable(self):
		#Redirect stdout
		old_stdout = sys.stdout
		sys.stdout = mock_stdout = io.StringIO()
		
		printTable(self.tableData)
		
		#Restore stdout
		sys.stdout = old_stdout
		
		assert mock_stdout.getvalue() == self.expected