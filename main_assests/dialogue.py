class Dialogue :
        def __init__(self, script, a, b, c, d) :
                self.script = script
                self.a = a
                self.b = b
                self.c = c
                self.d = d

                self.data = { 0 : script, "a" : a, "b" : b, "c" : c, "d" : d}
        
placeholder = Dialogue("uhhhh hi i didnt finish this bit, if you go any further you will get an error. so uhhh dont do that\n\n -adeowazhere", None, None, None, None)

dialogueAA = Dialogue("""
        You try to encourgae a further debate of toilet ownership and its implications...
        But the narrator just assumes you are suffering from short term memory loss,
        And proceeds to escort you out of the toilet.
        
        You look around and see 3 doors, which door do you pick?
        
        A: The door with a triangle on it.
        B: The door with a kiwi on it.
        C: The door that doesn't exist???
        D: Ummm, nuh uh!!!! I want another door""", placeholder, placeholder, placeholder, placeholder)

dialogueAB = Dialogue("""
        You and the narrator leave your impeccably crafted toilet to find a stranger waiting oustide.
        You feel like inspecting them...but what to inspect???
        That is the question not that smelly dude's 'To be or not to be'
        
        A: Their face.
        B: Their feet???
        C: Their clothing!!!
        D: Their body shape""", placeholder, placeholder, placeholder, placeholder)

dialogueAC = Dialogue("""
        You take your opportunity to fufill your carnal wicked desires...
        You take a deep breath and you whip it out...
        YOUR GIANT JUICY FAT KIWI OF CARNAL DESTRUCTION AND WAR!!!!!
        Huh, you seem surprised? Don't look at me with that face you are the one bringing a kiwi to a swordfight.
        Well good thing I brought a GUN TO THIS SWORDFIGHT!!!!!!
        
        A: WHAT!!!! NO FAIR I WANT ONE TOO!!!!!
        B: Hehehehe this isn't no normal kiwi...
        C: Well it isn't a swordfight any more because none of us have swords.
        D: I politely disagree with the illogical narrative of you having a firearm in a toilet.
""", placeholder, placeholder, placeholder, placeholder)

dialogueAD = Dialogue("""
        Indeed, what better way to spend this fine hour than inspecting the toilet... 
        With you...
        And with your narrator...
        And the rising toilet water...
        ...
        Oh its getting higher.
        Wow, thats alot of um water...
        And now its starting to overflow now huh...
        Uhhh we should probably do something about this
        
        A: Continue observing the toilet water rising like a deer in headlights.
        B: Have a lil' taste of the drink being served :3
        C: Shove the narrator into the toilet.
        D: BRO I'M GETTING OUTTA HERE, YOU CAN FIX THAT LMAOOOOOOOO""", placeholder, placeholder, placeholder, placeholder)

dialogueA = Dialogue("""
        Who is this guy to tell you who's toilet this is???
        You intellectually argue with the LITERAL NARRATOR about toilet ownership and its implications. 
        You did win the debate but not because of your 'profound genius' but because none of you remember anything before this point.
        Well since I'm in your toilet, what next?
        
        A: Huh, what do you mean this is my toilet???
        B: We should probably leave the toilet...
        C: SWORDFIGHT!!!
        D: Stay in the toilet thinking about the amazing craftmanship of said object.
""", dialogueAA, dialogueAB, dialogueAC, dialogueAD)

dialogueB = Dialogue("""
        A robbery with what, the kiwi in your hand??? 
        Actually, you know...
        If you give me the kiwi, I'll let the robbery commence.
        Sounds fair?
        
        A: Of course!!!
        B: Of course!!!
        C: Of course!!!
        D: You really want this kiwi huh...
""" , placeholder, placeholder, placeholder, placeholder)

dialogueC = Dialogue("""
        Oh okay then well take some toilet paper as a parting gift, random intruder!
         
        (You recieved Toilet paper!!!)
        (It spontaneously turns into a black hole because Adeo forgot to add a storing system :3)
        (Oh well there goes the progra---)
""", placeholder, placeholder, placeholder, placeholder)

dialogueD = Dialogue("""
        You obliterate the harmless narrator with your cutting words that etch wounds into their poor soul...
        You make clear you are a force to be reckoned with, A FORCE WITH UNIMAGINABLE POWER!
        (You feel something has awakened in you...)
        The narrator is very sorry for questioning your power and introduces himself as Joe.
        
        A: Who's Joe???
        B: I'm not falling for that...
        C: Mama
        D: HI JOE :DDD""", placeholder, placeholder, placeholder, placeholder)

dialogue = Dialogue("""
        You are in my toilet????

        A: Huh, what do you mean this is your toilet???
        B: This is a robbery.
        C: Oh my bad I'll leave right now.
        D: YOU SMELLLLL!!!!1!!1!!!
""", dialogueA, dialogueB, dialogueC, dialogueD)