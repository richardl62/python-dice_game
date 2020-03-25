from tkinter import *

class IntegerBox(Frame) :
    def __init__ (self, top, callback, initial_text=""):
        super().__init__(top)
        
        self.callback = callback
        self.initial_text = initial_text
        

        self.t = Text(self, height=1, width=16)
        

        def return_cb(*args):
            value = self.t.get("1.0",END)
            try:
                score = int(value)
                self.callback(score)
            except ValueError:
                messagebox.showwarning(
                "IntegerBox",
                "\"%s\" is not an integer" % value.strip()
                )
                
            self.clear()

        def focus_in_cb(*args):
            self.clear()

        def focus_out_cb(*args):
            self.reset()

        self.t.bind("<Return>", return_cb)
        self.t.bind("<FocusIn>", focus_in_cb)
        self.t.bind("<FocusOut>", focus_out_cb)
        self.t.pack()
        
        self.reset()
        
    def set_focus(self):
        self.t.focus_set()
            
    def clear(self):
        self.t.delete("1.0",END)

    def reset(self):
        self.clear()
        self.t.insert(END, self.initial_text)
    
class ScorePad(Frame) :
    def __init__ (self, top, name):        

        super().__init__(top)
        
        name_wid = Label(self, text=name)

        self.score_reader_wid = IntegerBox(self, self.process_scores,
            initial_text="<score>")

        self.scores_str = StringVar()
        scores_wid=Label(self, textvariable=self.scores_str, anchor=E, justify=RIGHT)

        self.total_str = StringVar()
        total_wid = Label(self, textvariable=self.total_str, anchor=E, justify=RIGHT)

        self.total = 0
        
        name_wid.grid(row=0,columnspan=2)
        self.score_reader_wid.grid(row=1,columnspan=2)

        scores_wid.grid(row=2,column=0,sticky=W)
        total_wid.grid(row=2,column=1,sticky=W)

        self.post_score_action = lambda : None
        self.post_score_action()
        
        self.reset()

    def set_focus(self):
        self.score_reader_wid.set_focus()

    def reset(self):
        self.total = 0
        self.scores_str.set("Scores")
        self.total_str.set("Total")
        self.score_reader_wid.reset()
        
    def process_scores(self, score): # private use
        self.scores_str.set(self.scores_str.get() + "\n" + str(score))

        self.total = self.total + score;
        self.total_str.set(self.total_str.get() + "\n" + str(self.total))

        self.post_score_action()


class ScorePads(Frame) :
    def __init__ (self, top, nplayers):

        super().__init__(top)

        def make_set_focus_lamdba(sp):
            return lambda : sp.set_focus();

        score_pads = []
        for i in range(1,nplayers+1) :
            sp = ScorePad(self, "Player " + str(i))
            score_pads.append(sp)
            sp.pack(side=LEFT,expand=True,fill=Y)

        for i in range(0,nplayers) :
          
            if i == nplayers - 1 :
                next_sp = score_pads[0]
            else:
                next_sp = score_pads[i+1]

            score_pads[i].post_score_action = make_set_focus_lamdba(next_sp)
        
        self.score_pads = score_pads

    def reset(self) :
        for sp in self.score_pads:
            sp.reset()
        
if __name__ == "__main__":
    root = Tk()

    sp=ScorePads(root, 3)
    sp.pack()

    root.mainloop() 








 
