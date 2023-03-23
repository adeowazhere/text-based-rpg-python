from main_assests import messages as m
from main_assests import functions as f

answer = input(f.fluff(m.welcome))
match answer :
    case "a" :
        answer = input(f.fluff(m.toiletOwnershipDebate))
    case "b" :
        answer = input(f.fluff(m.kiwiRobbery))
    case "c" :
        answer = input(f.fluff(m.toiletUhOh))
        exit()
    case "d" :
        answer = input(f.fluff(m.narratorSmells))

print("uhhh this isnt finished yet lol")