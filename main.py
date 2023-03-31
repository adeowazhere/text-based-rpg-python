from main_assests import dialogue as m
from main_assests import functions as f
current_dialogue = m.dialogue
answer = f.message(current_dialogue)
while True:
    current_dialogue = f.responseCheck(answer, current_dialogue)
    answer = f.message(current_dialogue)