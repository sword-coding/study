import tkinter as tk
import time
class DIRSEARCH():
	def __init__(self):
		self.top=tk.Tk()
		self.top.geometry('200x300')
        self.top.topic("hello")
		self.version=tk.Label(self.top,text="version 0.0.1")
		self.version.pack()
		self.frame=tk.Frame(self.top)
		self.scroll=tk.Scrollbar(self.top)
		self.scroll.pack(side=tk.RIGHT,fill=tk.Y)
		# self.listbox=tk.Listbox(self.frame,height=15,width=50,yscrollcommand=self.scroll.set)
		# self.listbox.bind('Double-1',self.setDIRR)
		self.frame.pack()
		self.top.mainloop()
app=DIRSEARCH()

