from tkinter import *
from dice import DiceSet
from score_pad import ScorePads

def read_int(prompt):
    
    while True:
        print("%s: " % prompt, end='')

        try:
            value = int(input())
        except:
            pass
        else:
            if value >= 0:
                return value

        
def dice_game(nplayers, ndice):

    root = Tk()
    button_frame = Frame(root)
    button_frame.pack()
    
    dice = DiceSet(root, ndice)
    dice.pack()
    dice.roll_all()

    score_pads = ScorePads(root, nplayers)
    score_pads.pack();

    def restart() :
        score_pads.reset()
    
            
    Button(button_frame, text="Roll unheld", command=dice.roll_unheld).pack(side=LEFT)
    Button(button_frame, text="Roll all", command=dice.roll_all).pack(side=LEFT)
    Button(button_frame, text="Reset", fg="red", command=restart).pack(side=LEFT)
    Button(button_frame, text="Quit", fg="red", command=root.quit).pack(side=LEFT)

    # Bring to top
    root.lift()
    root.attributes("-topmost", True)
    root.attributes("-topmost", False)

    
    root.mainloop()
    root.destroy()

if __name__ == "__main__" :

    dice_game(
        nplayers=read_int("Number of players"),
        ndice=read_int("Number of dice")
        )
