import sys
import Ch3_collatz


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    print("This is the main routine.")
    Ch3_collatz.main()

main()