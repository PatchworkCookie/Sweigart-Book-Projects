#The Collatz Sequence
#Chapter 3 of Automate the Boring Stuff with Python
'''
Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.
Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1. (Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)
Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value.
Hint: An integer number is even if number % 2 == 0, and it’s odd if number % 2 == 1.
The output of this program could look something like this:
Enter number:
3
10
5
16
8
4
2
1
'''

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)

def collatz(number):
    logging.debug('Start of collatz(%s)' % (number))
    if (number % 2 == 0):
        logging.debug('Found "number" (%(n)s) to be even. "number" will now = %(n)s / 2 = %(nN)s' % {'n':number, 'nN':int(number/2)})
        number = int(number / 2)
        print(number)
        logging.debug('Returing: (%s)' % number)
        return number
    else:
        logging.debug('Found "number" (%(n)s) to be odd. "number" will now = 3 * %(n)s + 1 = %(nN)s' % {'n':number, 'nN':int((3*number)+1)})
        number = (3 * number) + 1
        print(number)
        logging.debug('collatz is returing: %s' % number)
        return number
    
def collatzLoop(number):
    logging.debug('Start of collatzLoop(%s)' % (number))
    while number != 1:
        logging.debug('"number" (%s) != 1' % (number))
        logging.debug('Calling collatz(%s)' % (number))
        number = collatz(number)

    logging.debug('collatzLoop is returing: %s' % number)
    return number

if __name__ == '__main__':
	logging.debug('Start of program')
	number = input("Enter a number: ")
	try:
		number = int(number)
	except ValueError:
		print("You must enter an integer number to proceed")
	else:
		collatzLoop(number)
		logging.debug('End of program')