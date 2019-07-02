#Comma Code
#Chapter 4 of Automate the Boring Stuff with Python
'''
Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.
'''

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.INFO)

def listFixer(things):
    logging.debug('Start of listFixer(%s)' % (str(things)))
    if len(things) > 1:
        logging.debug('"things" has more than one element')
        body = things[:-1]
        logging.debug('"body" list created: %s' % (str(body)))
        end = things[-1]
        logging.debug('"end" list created: %s' % (str(end)))

        things = ""
        
        logging.info('Entering string building loop')
        for i in range(len(body)):
            logging.debug('Adding element at index %s, value: %s' % (i, body[i]))
            things = things + body[i] + ", "
            logging.debug('"things" is now: "%s" with length of %s characters' % (things, len(things)))

        logging.info('End of string building loop')
        
        logging.debug('Adding end (%s), at end of "things"' % (end))
        things = things + "and " + end
        logging.debug('"things" is now: %s' % (things))
    
    return things

inv = ["Axe","Pole","Rope","Lens","Flute"]
inv = listFixer(inv)
print("Your adventurer is equiped with: " + inv)
