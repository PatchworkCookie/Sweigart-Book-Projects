#Mad Libs
#Chapter 8 of Automate the Boring Stuff with Python
'''
Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.

The program would find these occurrences and prompt the user to replace them.

Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck

The following text file would then be created:

The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.

The results should be printed to the screen and saved to a new text file.
'''

import logging, pytest
	
def promptForInputFile():
	filepath = ''
	pass

def openInput(filePath):
	#Return opened file
	pass
	
def createWordList(filedata):
	wordList = []
	pass
	
def promptForWords(list):
	responses = []
	pass
	
def generateText(filedata, list):
	text = ''
	pass
	
def displayText(text):
	pass

def promtForOutputFile():
	filePath = ''
	pass
	
def saveText(text, filepath):
	pass
	
class Test_():
	@pytest.mark.parametrize('input, exOutput, exResult', [(['test','test'],'wrong','bad')])
	def test_promptForInputFile(self, monkeypatch, capsys, input, exOutput, exResult):
		monkeypatch.setattr('builtins.input', lambda x : input.pop(0)) # Return next item in input list
		
		result = promptForInputFile()
		stdout_capture = capsys.readouterr()
		
		assert stdout_capture[0] == exOutput
		assert result == exResult
	
	@pytest.mark.parametrize('input, exOutput, exResult', [(['test','test'],'wrong','bad')])
	def test_openInput(self, monkeypatch, input, exOutput, exResult):
		
		assert 0
	
	def test_createWordList(self):
		assert 0
	
	def test_promptForWords(self):
		assert 0
	
	def test_generateText(self):
		assert 0
	
	def test_displayText(self):
		assert 0
	
	def test_promtForOutputFile(self):
		assert 0
	
	def test_saveText(self):
		assert 0
	pass
	
if __name__ == '__main__':
	pass # luv you too, bb : >