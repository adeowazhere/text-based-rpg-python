import sys
import time
prompt = "\n\n>> "
output = """
        You are in my toilet????

        A: Huh, what do you mean this is your toilet???
        B: This is a robbery.
        C: Oh my bad I'll leave right now.
        D: YOU SMELLLLL!!!!1!!1!!!
"""

for i in output:
    print(i, end='')
    sys.stdout.flush()
    time.sleep(0.075)
x = input(prompt)