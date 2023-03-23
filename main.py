from main_assests import dialogue as m
from main_assests import functions as f

answer = f.message(m.welcome)
while True:
    match answer :
        case "a" :
            answer = f.message(m.dialogueA)
        case "b" :
            answer = f.message(m.dialogueB)
        case "c" :
            answer = f.message(m.dialogueC)
            exit()
        case "d" :
            answer = f.message(m.dialogueD)
print("uhhh this isnt finished yet lol")