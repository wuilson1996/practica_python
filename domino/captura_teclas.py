from tkinter import *

class captura():
	
	def __init__(self):

		self.ventana = Tk()
		self.ventana.geometry("600x500")
		self.Captura_mouse()
		self.ventana.mainloop()

	def Captura_mouse(self):

		self.canvas1 = Canvas(self.ventana, width = 600, height = 500)
		#self.canvas1.create_image(500,333,bg="white")
		self.canvas1.bind("<a>",self.tecla)
		self.canvas1.place(x = 0, y = 530)
		print("canvas")
	
	def tecla(self, evento):

		print(evento)


cap = captura()