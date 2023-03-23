from main_assests import dialogue as m
from main_assests import functions as f

answer = f.message(m.welcome)
while True:
    match answer :
        case "a" :
            answer = f.message(m.toiletOwnershipDebate)
        case "b" :
            answer = f.message(m.kiwiRobbery)
        case "c" :
            answer = f.message(m.toiletUhOh)
            exit()
        case "d" :
            answer = f.message(m.narratorSmells)
print("uhhh this isnt finished yet lol")