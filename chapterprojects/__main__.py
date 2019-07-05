import sys
import Ch3_collatz 

modules = {(3,0):Ch3_collatz}


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    mainLoop()
    
def mainLoop():
    for key in modules.keys():
        modules[key].main()
        input("Press enter to continue...")

main()