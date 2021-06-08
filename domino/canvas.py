	def Captura_mouse(self):

		self.canvas1=Canvas(self.ventana, width = 1000, height = 120)
		self.canvas1.create_image(500,333,image=self.fondo)
		self.canvas1.bind("<Motion>", self.mover_mouse)
		self.canvas1.bind("<Button-1>", self.presion_mouse)
		self.canvas1.place(x=0, y=530)
		print("canvas")
	
	def presion_mouse(self, evento):
		self.canvas1.create_oval(evento.x-5,evento.y-5,evento.x+5,evento.y+5, fill="red")

	def mover_mouse(self, evento):        
		self.ventana.title(str(evento.x)+"-"+str(evento.y))
		print(str(evento.x))