import random
from optparse import OptionParser
import sys


def generate_content(name):
    
    """
    Returns the input name concatinated 
    with a random number from 6 to 15
    """
    return name.capitalize() + " " + str(random.randrange(6, 15))


if __name__ == "__main__":
    usage = "usage: python %prog name"

    parser = OptionParser(usage)
    (options, args) = parser.parse_args()

    if len(sys.argv) == 2:
        print generate_content(sys.argv[1])
    else:
        parser.error("Wrong number of arguments: Try -h for help")                    
