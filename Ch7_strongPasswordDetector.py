#Strong Password Detection
#Chapter 7 of Automate the Boring Stuff with Python
'''
Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.
'''

import logging, pytest
import re

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def validateStrongPass(password):

	minimumLength = re.compile(r'.{8,}') # Check if string is long enough, 8 at minimum
	containsUpperCase = re.compile(r'[A-Z]') # Contains uppercase
	containsLowerCase = re.compile(r'[a-z]') # Contains lowercase
	containsNumber = re.compile(r'[0-9]') # Contains at least one number
	
	strong = True
	
	matchObject = minimumLength.search(password)
	if matchObject == None:
		print('Password should be at least 8 characters in length')
		strong = False
	
	matchObject = containsUpperCase.search(password)
	if matchObject == None:
		print('Password should contain at least 1 uppercase character')
		strong = False
	
	matchObject = containsLowerCase.search(password)
	if matchObject == None:
		print('Password should contain at least 1 lowercase character')
		strong = False
		
	matchObject = containsNumber.search(password)
	if matchObject == None:
		print('Password should contain at least 1 number')
		strong = False
		
	if strong:
		print('Entered password is strong!')
		
	return strong
	
	
class Test_validateStrongPass():
	@pytest.mark.parametrize("input, output",[('hello',"Password should be at least 8 characters in length\nPassword should contain at least 1 uppercase character\nPassword should contain at least 1 number\n"), 
	('WE','Password should be at least 8 characters in length\nPassword should contain at least 1 lowercase character\nPassword should contain at least 1 number\n'),
	('TH1s',"Password should be at least 8 characters in length\n"),
	('thisd0esnt','Password should contain at least 1 uppercase character\n'),
	('NOTTHIS1','Password should contain at least 1 lowercase character\n'),
	('NopeForThis','Password should contain at least 1 number\n')])
	def test_failingPasswords(self, capsys, input, output):
		logging.debug('Start of test_failingPasswords, input, output: %s, %s' % (str(input), str(output)))
		
		result = validateStrongPass(input)
		stdout_capture = capsys.readouterr() # Get captured stdout
		
		assert stdout_capture[0] == output
		assert result == False
		
	@pytest.mark.parametrize("input, output",[('Th1sWorks',"Entered password is strong!\n"), 
	('C4ntBr34kmeD0wn','Entered password is strong!\n')])
	def test_passingPasswords(self, capsys, input, output):
		logging.debug('Start of test_passingPasswords, input, output: %s, %s' % (str(input), str(output)))
		
		result = validateStrongPass(input)
		stdout_capture = capsys.readouterr() # Get captured stdout
		
		assert stdout_capture[0] == output
		assert result == True
	pass
	
if __name__ == '__main__':
	passW = input('Enter your password: ')
	validateStrongPass(passW)
	pass