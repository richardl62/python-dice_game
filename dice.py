import random
from tkinter import *

class Dice:
    ''' A single die with a flag to say if it is held '''
    def __init__(self, value=-1, held=False):
        self.value = value
        self.held = held

        if(value < 0): # Is there a better way to see of parameter is supplied?
            self.roll()

    def reset(self):
        self.held = False
        self.roll()

    def roll(self):
        self.value = random.SystemRandom().randint(1, 6);

    def __repr__(self):
        return "Dice(value=%d,held=%d)" % (self.value, self.held)


class DiceFrame(Frame):
    def __init__(self, top):
        super().__init__(top)
 
        self.value = IntVar()
        Label(self, textvariable=self.value).pack()

        self.held = IntVar()
        Checkbutton(self, text="", variable=self.held).pack()

    def get(self):
        return Dice(value=self.value.get(), held=self.held.get())

    def set(self, dice):
        self.value.set(dice.value)
        self.held.set(dice.held)
        
class DiceSet(Frame):

    def __init__(self, top, ndice):
        super().__init__(top)
        
        self.dice_frames = []
        for i in range(0,ndice):
            df = DiceFrame(self)
            df.pack(side=LEFT)
            self.dice_frames.append(df)

    def get(self):
        return map(DiceFrame.get, self.dice_frames);

    def set(self, dice):
        for df,d in zip(self.dice_frames, dice):
            df.set(d);


    def roll_unheld(self):
        def sort_key(dice) :
            return not dice.held

        all_dice = sorted(self.get(), key=sort_key)

        for d in all_dice:
            if(not d.held):
                d.roll()

        self.set(all_dice)

    def roll_all(self):
        for df in self.dice_frames:
            df.set(Dice())

if __name__ == "__main__":

    root = Tk()
    
    button_frame = Frame(root)
    button_frame.pack()

    dice = DiceSet(root, 6)
    dice.roll_all()
    dice.pack()
    
    Button(button_frame, text="Roll unheld", command=dice.roll_unheld).pack(side=LEFT)
       
    Button(button_frame, text="Roll all", command=dice.roll_all).pack(side=LEFT)


    root.mainloop()



