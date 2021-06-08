from tkinter import messagebox
import sqlite3
class Date_Base():


	def __init__(self,code,name,tipo,precio,comentario):

		self.Code = code
		self.Name = name
		self.Type = tipo
		self.Precio = precio
		self.Comentario = comentario
		self.control = " "

		self.miConexion = sqlite3.connect("Productos")
		self.miCursor = self.miConexion.cursor()

	def conexionBBDD(self):
		
		try:
			self.miCursor.execute('''
				CREATE TABLE DATOS_PRODUCTOS (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				CODE VARCHAR(50),
				NAME VARCHAR(50),
				TYPE VARCHAR(50),
				PRECIO INTEGER,
				COMENTARIO VARCHAR(100))
				''')

			messagebox.showinfo("BBDD", "BBDD creada con exito")

		except:

			messagebox.showwarning("!Atencion¡", "La BBDD ya existe")

	def crear(self):

		datos = self.Code.get(),self.Name.get(),self.Type.get(),self.Precio.get(),self.Comentario.get()

		"""miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,'"+ miNombre.get()+
			"','"+ miPass.get() +
			"','"+ miApellido.get() +
			"','"+ miDireccion.get() +
			"','"+ textoComentario.get("1.0",END)+"')")"""
		self.miCursor.execute("INSERT INTO DATOS_PRODUCTOS VALUES(NULL,?,?,?,?,?)",(datos))	
		self.miConexion.commit()
		messagebox.showinfo("BBDD","Registro insertado con éxito")

	def leer(self):
		#self.Id = IntVar()
		self.miCursor.execute("SELECT * FROM DATOS_PRODUCTOS WHERE CODE = " + self.Code.get())

		the_Product = self.miCursor.fetchall()
		print(the_Product)
		
		for Product in the_Product:
			self.control = "."
			#self.Id.set(the_Product[0])
			self.Code.set(Product[1])
			self.Name.set(Product[2])
			self.Type.set(Product[3])
			self.Precio.set(Product[4])
			self.Comentario.set(Product[5])


		self.miConexion.commit()

		if self.control == " ":
			return 0
			
		else:
			return 1