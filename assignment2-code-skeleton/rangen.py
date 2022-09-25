import sys
import random

def rangen(max):
    f = open('nums.txt', 'w')
    random.seed()

    for i in range(0,max):
        f.write(str(random.randint(0, max)) + "\n")

    f.close()

if(len(sys.argv) != 2):
    print "Wrong number of arguments. Usage: python rangen.py max"
else:
    rangen(int(sys.argv[1]))
