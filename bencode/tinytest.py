"""
A simple function to check some basic assertions.
"""
import sys
def run(test):
    TTY = sys.stdout.isatty()
    passed = False
    try:
        test()
        message = '{name}: pass'.format(name=test.__name__)
        passed = True
    except AssertionError:
        message = '{name}: fail'.format(name=test.__name__)

    if TTY:
        # see https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences
        RESET = '\033[0m'
        BOLD = '\033[1m`'
        BLACK = 30 
        RED = 31
        GREEN = 32
        YELLOW = 33
        WHITE = 7
        COLOR = GREEN if passed else RED
        tty_template = '\033[{COLOR};{WEIGHT}{message}{RESET}'
        print(tty_template.format(
            message=message, 
            COLOR=COLOR,
            WEIGHT='1m',
            RESET=RESET
        ))
    else:
        print(message)

    return test
