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
logging.disable(logging.INFO)

def printTable(table):
	logging.debug('Start of printTable(%s)' % (str(table)))
	#Get length of longest word in each column
	longest = [0] * len(table)
	for column in range(len(table)):
		for row in range(len(table)):
			logging.debug('The longest for this column is: %s, %s has length %s' % (str(longest[column]), str(table[column][row]), str(len(table[column][row]))))
			if longest[column] < len(table[column][row]) : longest[column] = len(table[column][row])
	logging.debug('Lengths for columns are: %s' % (str(longest)))
			
	
	#Print contents of the table
	for row in range(len(table[0])):
		for column in range(len(table)):
			logging.debug('Item: %s, Column: %s, Row: %s, Column space: %s' % (str(table[column][row]), str(column), str(row), str(longest[column])))
			space = "" if column + 1 == len(table)  else " " #space between columns as necessary
			print(str(table[column][row]).rjust(longest[column]) + space , end="")
		print() #Go to the next row
	pass

class TestPrintTable():
	tableData = [['apples', 'oranges', 'cherries', 'banana'],
				['Alice', 'Bob', 'Carol', 'David'],
				['dogs', 'cats', 'moose', 'goose']]
	expected = '''  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
'''
  
	def test_printTable(self, capsys):
		#Redirect stdout
		# old_stdout = sys.stdout
		# sys.stdout = mock_stdout = io.StringIO()
		
		printTable(self.tableData)
		
		#Restore stdout
		# sys.stdout = old_stdout
		stdout_capture = capsys.readouterr()
		assert stdout_capture[0] == self.expected
		# assert mock_stdout.getvalue() == self.expected

if  __name__ =='__main__':
	tableData = [['apples', 'oranges', 'cherries', 'banana'],
				['Alice', 'Bob', 'Carol', 'David'],
				['dogs', 'cats', 'moose', 'goose']]
	printTable(tableData)