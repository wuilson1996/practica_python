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


def Usar_QR(code):
	print("entro")
	code.set("algo")
	
#sirve para llamar a la clase que genera el qr
def save(code, name, tipo, precio, comentario):

	generate = Code_Qr(code.get())
	generate.save_qr()
	DB = Date_Base(code,name,tipo,precio,comentario)
	DB.crear()
	print("codigo QR generado con exito")

#sirve para ver el qr luego de ser creado

def conection_DB(code,name,tipo,precio,comentario):
	DB = Date_Base(code,name,tipo,precio,comentario)
	DB.conexionBBDD()

def leer(code,name,tipo,precio,comentario):
	DB = Date_Base(code,name,tipo,precio,comentario)
	aux = DB.leer()

	if aux == 0:
		print("no existe el producto")

	else:
		print("el producto existe")
