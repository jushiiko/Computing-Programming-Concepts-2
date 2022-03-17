from tkinter import Tk, Label, PhotoImage, LEFT, RIGHT, RIDGE
root = Tk()

text = Label(root,
             font=('Comic Sans MS', 20, 'bold'),
             foreground='brown',
             background='white',
             pady=10,
             text='John Sebastian Ablay \n Davao City, November 2002')
text.pack(side=RIGHT)

me = PhotoImage(file='asta.gif')
meLabel = Label(root,
                borderwidth=5,
                relief=RIDGE,
                image=me,)
meLabel.pack(side=LEFT)

root.mainloop()