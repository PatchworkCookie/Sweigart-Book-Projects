#Strong Password Detection
#Chapter 7 of Automate the Boring Stuff with Python
'''
Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.
'''

import logging, pytest
import re

def validateStrongPass(password):

	minimumLength = re.compile(r'.{8,}')
	#TODO: Check if string is long enough, 8 at minimum
	containsUpperCase = re.compile(r'[A-Z]')
	#TODO: Contains uppercase
	containsLowerCase = re.compile(r'[a-z]')
	#TODO: Contains lowercase
	containsNumber = re.compile(r'[0-9]')
	#TODO: Contains at least one number
	
	strong = True
	
	matchObject = minimumLength.search(password)
	if matchObject == None:
		print('Bad')
		strong = False
		
	return strong
	
	#TODO: Logic to test each case
	#TODO: 
	#TODO: 
	pass

class Test_validateStrongPass():
	@pytest.mark.parametrize("input, output",[('hello',"Password should be at least 8 characters in length\nPassword should contain at least 1 uppercase character\nPassword should contain at least 1 number\n"), 
	('WE','Password should be longer than 7 characters\nPassword should contain at least 1 lowercase character\nPassword should contain at least 1 number\n'),
	('TH1s',"Password should be at least 8 characters in length\n"),
	('thisd0esnt','Password should contain at least 1 uppercase character\n'),
	('NOTTHIS1','Password should contain at least 1 lowercase character\n'),
	('NopeForThis','Password should contain at least 1 number\n')])
	def test_failingPasswords(self, monkeypatch, capsys, input, output):
		logging.debug('Start of test_failingPasswords, input, output: %s, %s' % (str(input), str(output)))
		
		result = validateStrongPass(input)
		
		stdout_capture = capsys.readouterr()
		assert stdout_capture[0] == output
		assert result == False
		
	def test_passingPasswords(self):
		pass
	pass
	
if __name__ == '__main__':
	passW = input('Enter your password: ')
	validateStrongPass(passW)
	pass