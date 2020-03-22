class ConversationHandler:
    
    emoji =  {"confused":"\U0001F615", "wink":"\U0001F609", "repeat":"\U0001F501",
    "worried":"\U0001F61F","muscle":"\U0001F4AA", "smiling":"\U0001F60A"}
    states =  {
    0 : ("Hallo! Schön, dass Du da bist! Wie geht es Dir heute?",
    "1: Mir geht es gut! = " + emoji["smiling"]+" \n2: Mir geht es schlecht... = " + emoji["worried"]),
    1 : ("Hey ich habe Zeit, was möchtest Du tun?",
    "1: Willst Du mit jemandem sprechen? Ich kenne interessante Chat-Partner, die sich auf Dich freuen! = "+ emoji["smiling"]+
    "\n: Oder willst Du etwas Neues ausprobieren? Ich habe da ein paar coole Tipps für Dich! = " + emoji["muscle"]),
    2 : ("Oh,Dir geht es schlecht.  Kannst Du mir einen Tipp geben, was Dich belastet?", ""),
    3 : ("Chat Starten", "1: Hast du vielleicht Lusts nochmal mit mir zu reden? = " + emoji["repeat"]),
    4 : ("Informationen", "1: Hast du vielleicht Lusts nochmal mit mir zu reden? = " + emoji["repeat"]),
    900: ("Hallo ich bin Coco, deine persönlicher Mental-Health Support. Und wer bist du?")
    }
    indices =  {
    0 : {"1":1, "2":2, emoji["smiling"]:1,emoji["worried"]:2},
    1 : {"1":3, "2":4, emoji["smiling"]:3,emoji["muscle"]:4},
    2 : {},
    3 : {"1":0,  emoji["repeat"]:0},
    4 : {"1":0,  emoji["repeat"]:0},
    }
    
    default_message = "Leider kann ich dir darauf keine Anwort geben"+emoji["confused"]+\
        "Bitte benutze eine der Antwortmöglichkeiten, die ich dir gegeben habe" + emoji["wink"]
    
    def current_message(self, state):
        return self.states[state][0] + " \n\n" + self.states[state][1]
    
        
    def update (self, message, state):

        if (state==900):
            return 901 , self.states[900]
        
        new_state = self.indices[state].get(message, -1)
        if new_state==-1:
            return state, self.default_message
        else:
            return new_state, self.current_message(new_state)