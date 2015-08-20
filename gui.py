import Tkinter
import ttk 
import two_d_cut

root = Tkinter.Tk()
root.title("2D cut")
cv = Tkinter.Canvas(root, width=600, height=600)
cv.pack()
button = Tkinter.Button(root, text='Start', command=two_d_cut.main)
button.pack()
Tkinter.mainloop()

