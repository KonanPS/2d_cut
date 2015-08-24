import Tkinter
import ttk 
import two_d_cut

root = Tkinter.Tk()
root.title("2D cut")

# lab = Tkinter.Label(root, text='Hello GUI world')
# lab.grid(row=0, columnspan=3)

lable_len = Tkinter.Label(text='Length:').grid(column=0, row=1)
lable_qua = Tkinter.Label(text='Quantity:').grid(column=0, row=2)

global PALLET_LEN
PALLET_LEN = 0

def pall_len(entery):
	"""
	Specify pallet len
	"""
	PALLET_LEN = int(entery.get())
	print PALLET_LEN
	return 

p_len_lab = Tkinter.Label(text='Pallet length:').grid(column=0, row=0)
p_len = Tkinter.Entry(root)
p_len.grid(row=0, column=1)
p_add = Tkinter.Button(root, text='Add pallet', command=lambda: pall_len(p_len)).grid(row=0, column=2)

e_length = Tkinter.Entry(root)
e_length.grid(column=1, row=1, columnspan=2)
e_quantity = Tkinter.Entry(root)
e_quantity.grid(column=1, row=2, columnspan=2)

pieces_dict = {}

def add_piece(pieces_d, e_len, e_num):
	"""
	Creates pieces_dict form Entry widgets
	"""
	elem_len = int(e_len.get())
	elem_num = int(e_num.get())

	if elem_len in pieces_d:
		pieces_d[elem_len] += elem_num
	else:
		pieces_d[elem_len] = elem_num
	
	e_len.delete(0,'end')
	e_num.delete(0,'end')
	print pieces_d
	return pieces_d

add_button = Tkinter.Button(root, text='Add', command=lambda: add_piece(pieces_dict, e_length, e_quantity))
add_button.grid(row=3, column=2)

logo = Tkinter.PhotoImage(file="laminacia.gif")
w1 = Tkinter.Label(root, image=logo).grid(row=4, column=0, columnspan=3)
# cv = Tkinter.Canvas(root, width=600, height=600)
# cv.pack()

result = Tkinter.Label(root, text='Result should appear here')
result.grid(row=6, columnspan=3)

def res(lable, pieces_dict, P_LEN):
	"""
	starts main program and updates lable with program results
	"""
	cuts, total_residue = two_d_cut.main(None, pieces_dict, P_LEN)
	# res_text = """"""
	# for cut in cuts:
	# 	res_text += str(cut) + '\n'
	lable.config(text="See results in output.txt file")

button = Tkinter.Button(root, text='Start', command=lambda: res(result, pieces_dict, PALLET_LEN))
button.grid(row=5, column=2)

Tkinter.mainloop()

