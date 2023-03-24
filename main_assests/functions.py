import sys
import time
from main_assests import dialogue as m

prompt = "\n\n>> "

def message(a) :
    for i in a[0]:
        print(i, end='')
        sys.stdout.flush()
        time.sleep(0.05)
    x = input(prompt).lower()
    return x

def responseCheck(r, d) :
    match r :
        case "a" :
            d = d[1]
        case "b" :
            d = d[2]
        case "c" :
            d = d[3]
        case "d" :
            d = d[4]
        case _ :
            pass
    return d