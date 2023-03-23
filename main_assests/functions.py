import sys
import time
from main_assests import dialogue as m

prompt = "\n\n>> "

def message(a) :
    for i in a:
        print(i, end='')
        sys.stdout.flush()
        time.sleep(0.05)
    x = input(prompt).lower()
    return x
