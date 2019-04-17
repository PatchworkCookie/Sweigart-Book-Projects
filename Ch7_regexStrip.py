#Regex Version of strip()
#Chapter 7 of Automate the Boring Stuff with Python
'''
Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. Otherwise, the characters specified in the second argument to the function will be removed from the string.
'''
import logging, pytest

def regexStrip(string, *args):
	pass
	
class Test_():
	
	@pytest.mark.parametrize("input, output",[('  space   ','space'), ('\ttab\t\t','tab'), ('newline\n','newline'), (' \tmixed\t   \n','mixed'), ('  \temb\ted d  e\nd\t  \n','emb\ted d  e\nd')])
	def test_standardStrip(self, input, output):
		result = regexStrip(input)
		assert result == output
		
	@pytest.mark.parametrize("input, characters, output",[('  test   ', ' ','test'), ('abcbabcaYorkiecabcbabc','abc','Yorkie'), ('fiGEFellowshipfiGEEGff','EfGi','Fellowship'), ('iaiaiaarainaaiaiiaiii','ai','rain')])
	def test_charStrip(self, input, characters, output):
		result = regexStrip(input, characters)
		assert result == output
	
if __name__ == '__main__':
	pass