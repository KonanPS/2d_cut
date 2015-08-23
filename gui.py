import Tkinter
import ttk 
import two_d_cut

root = Tkinter.Tk()
root.title("2D cut")

lab = Tkinter.Label(root, text='Hello GUI world')
lab.grid(row=0, columnspan=3)

lable_len = Tkinter.Label(text='Length:').grid(column=0, row=1)
lable_qua = Tkinter.Label(text='Quantity:').grid(column=0, row=2)

e_length = Tkinter.Entry(root)
e_length.grid(column=1, row=1, columnspan=2)
e_quantity = Tkinter.Entry(root)
e_quantity.grid(column=1, row=2, columnspan=2)

add_button = Tkinter.Button(root, text='Add', width=40)
add_button.grid(row=3, column=0, columnspan=3)

logo = Tkinter.PhotoImage(file="laminacia.gif")
w1 = Tkinter.Label(root, image=logo).grid(row=4, column=0, columnspan=3)
# cv = Tkinter.Canvas(root, width=600, height=600)
# cv.pack()

result = Tkinter.Label(root, text='Result should appear here')
result.grid(row=6, columnspan=3)

def res(lable=result):
	"""
	starts main program and updates lable with program results
	"""
	cuts, total_residue = two_d_cut.main()
	# res_text = """"""
	# for cut in cuts:
	# 	res_text += str(cut) + '\n'
	lable.config(text="See results in output.txt file")

button = Tkinter.Button(root, text='Start', command=res, width=40)
button.grid(row=5, columnspan=2)

Tkinter.mainloop()

