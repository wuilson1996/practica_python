from tkinter import *
import qrcode
from BD import *
#creamos un objeto codigo QR

class Code_Qr():

	def __init__(self,info):

		self.qr = qrcode.QRCode(
			version = 1,
			error_correction = qrcode.constants.ERROR_CORRECT_H,
			box_size = 10,
			border = 4
		)

		#asignamos la informacion a la variable
		self.info = info
	
	def save_qr(self):

		#Agregamos la informacion
		self.qr.add_data(self.info+"\n")
		#self.qr.add_data(self.name)
		self.qr.make(fit = True)

		#creamos una imagen para el objeto codigo QR
		imagen = self.qr.make_image()

		#guardamos la imagen con la extension que queremos
		imagen.save('media/'+str(self.info)+'.png')

#creamos nuestra ventana

class Windows():

	def __init__(self,cap):
		
		self.windows = Tk()
		self.windows.geometry("800x500")

		self.code = StringVar()
		self.name = StringVar()
		self.tipo = StringVar()
		self.precio = IntVar()
		self.comentario = StringVar()

		self.cap = cap

		
		
		#codigo de producto
		label = Label(self.windows, text = 'Ingrese el Codigo del Producto')
		label.place(x = 30, y = 20)

		entry = Entry(self.windows,textvariable = self.code)
		entry.place(x = 50, y = 50)

		#nombre de producto
		label2 = Label(self.windows, text = 'Nombre de QR')
		label2.place(x = 30, y = 70)

		entry2 = Entry(self.windows,textvariable = self.name)
		entry2.place(x = 50, y = 90)

		#Tpo de producto
		label = Label(self.windows, text = 'Ingrese el Tipo')
		label.place(x = 30, y = 110)

		entry = Entry(self.windows,textvariable = self.tipo)
		entry.place(x = 50, y = 130)

		#Precio
		label = Label(self.windows, text = 'Ingrese el Precio')
		label.place(x = 30, y = 150)

		entry = Entry(self.windows,textvariable = self.precio)
		entry.place(x = 50, y = 170)

		#comentario
		label = Label(self.windows, text = 'Ingrese un comentario')
		label.place(x = 30, y = 190)

		entry = Entry(self.windows,textvariable = self.comentario)
		entry.place(x = 50, y = 210)

		#boton ir
		buton = Button(self.windows,text = 'Create QR', command = self.save)
		buton.place(x = 115, y = 250)

		buton = Button(self.windows,text = 'Create DB', command = self.conection_DB)
		buton.place(x = 40, y = 250)

		buton = Button(self.windows,text = 'Leer DB', command = self.leer)
		buton.place(x = 40, y = 280)

		buton = Button(self.windows,text = 'Limpiar', command = self.limpiarCampo)
		buton.place(x = 115, y = 280)

		buton = Button(self.windows,text = 'Usar QR', command = self.Usar_QR)
		buton.place(x = 115, y = 310)
		
		
		self.code.set(self.cap)

		self.windows.mainloop()

	def Usar_QR(self):
		print("entro")
		self.code.set("algo")
	
	#sirve para llamar a la clase que genera el qr
	def save(self):

		generate = Code_Qr(self.code.get())
		generate.save_qr()
		self.view_qr()
		DB = Date_Base(self.code,self.name,self.tipo,self.precio,self.comentario)
		DB.crear()
		print("codigo QR generado con exito")

	#sirve para ver el qr luego de ser creado
	def view_qr(self):

		print("aqui veremos el qr generado")
		File = str(self.code.get())+'.png'
		print(File)

		Qr_generated = Label(self.windows, text = "Codigo QR Generado")
		Qr_generated.place(x = 250, y = 20)
		self.img = PhotoImage(file = 'media/'+File).subsample(3)
		self.label_img=Label(self.windows,image = self.img)
		self.label_img.place(x = 250, y = 50)

	def conection_DB(self):
		DB = Date_Base(self.code,self.name,self.tipo,self.precio,self.comentario)
		DB.conexionBBDD()

	def leer(self):
		DB = Date_Base(self.code,self.name,self.tipo,self.precio,self.comentario)
		aux = DB.leer()

		if aux == 0:
			print("no existe el producto")

		else:
			print("el producto existe")

	def limpiarCampo(self):

		self.code.set("")
		self.name.set("")
		self.tipo.set("")
		self.precio.set(0)
		self.comentario.set("")





