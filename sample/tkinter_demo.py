from tkinter import *


# root = Tk()
# myLabel = Label(root,text = "Vishy Inc © 2018")
# myLabel.pack()
# root.mainloop()

def hello(event):
    print( "Single Click, Button-l" )
def quit(event):
    print("Double Click, so let's stop")
    import sys; sys.exit()

widget = Button(None, text='Mouse Clicks')
widget.pack()
widget.bind('<1>',hello)
widget.bind('<Double-1>', quit)
widget.mainloop()