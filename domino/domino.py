from tkinter import *
import random

class domino:

	def __init__(self):

		#variables
		self.cruzar_I = 0
		self.cruzar_D = 0

		self.aux = 0
		self.posi = 0
		
		self.X1 = 600
		self.X2 = 600
		
		self.Y1 = 300
		self.Y2 = 325

		self.Y2_D = 325
		self.Y2_I = 325

		self.Y1_D = 300
		self.Y1_I = 300

		self.X_J2 = 200
		self.X_J1 = 200
		self.ganador = ''

		#variables de limites
		self.pixel_I = 100
		self.pixel_D = 1100

		self.aux_pixel_I = 600
		self.aux_pixel_D = 600

		#variable de aumento de piezas de jugador automatico
		self.cont = 7
		self.cont2 = 7
		#variable de la mesa
		self.mesa_list_D = []
		self.mesa_list_posi_D = []
		self.mesa_buton_D = []
		self.mesa_list_I = []
		self.mesa_list_posi_I = []
		self.mesa_buton_I = []
		
		#variables de jugador 1
		self.jugador1_v = []
		self.jugador1_v_copy = []
		self.jugador1_v_posi = []
		self.jugador1_v_posi_copy = []

		self.jugador1_h = []
		self.jugador1_h_copy = []
		self.jugador1_h_posi = []
		self.jugador1_h_posi_copy = []

		#variables de jugador 2
		self.jugador2_v = []
		self.jugador2_v_copy = []
		self.jugador2_v_posi = []
		self.jugador2_v_posi_copy = []

		self.jugador2_h = []
		self.jugador2_h_copy = []
		self.jugador2_h_posi = []
		self.jugador2_h_posi_copy = []


		#piezas horizontales
		self.img_horiz = []
		self.img_horiz_copy = []
		self.img_horiz_posi = []
		self.img_horiz_posi_copy = []

		#piezas verticales
		self.img_vert = []
		self.img_vert_copy = []
		self.img_vert_posi = []
		self.img_vert_posi_copy = []
		

	def ventana(self):

		self.ventana = Tk()
		self.ventana.geometry("1200x795")
		#self.ventana.resizable(0,0)
		
		self.puntos_J1 = 0
		self.puntos_J2 = 0

		self.fondo = PhotoImage(file = 'media/mesa.png')
		self.fondo_mesa = Label(self.ventana, image = self.fondo)
		self.fondo_mesa.place(x =- 2,y =- 2)
		
		#puntos jugador 1
		self.J1_puntos = Label(self.ventana, text = "Puntos")
		self.J1_puntos.place(x = 70, y = 650)

		self._J1_puntos = Label(self.ventana, text = self.puntos_J1)
		self._J1_puntos.place(x = 70, y = 700)

		#puntos jugador 2
		self.J2_puntos = Label(self.ventana, text = "Puntos")
		self.J2_puntos.place(x = 70, y = 20)

		self._J2_puntos = Label(self.ventana, text = self.puntos_J2)
		self._J2_puntos.place(x = 70, y = 70)

		self.carga_img()
		self.ventana.mainloop()

	def carga_img(self):

		for i in range(7):
			for j in range(i,7,1):

				#llenado de piezas horizontales
				self.img_D = PhotoImage(file = 'media/' + str(i) + '-' + str(j) + '.png')
				self.img_horiz.append(self.img_D)
				self.img_D = PhotoImage(file = 'media/' + str(j) + '-' + str(i) + '.png')
				self.img_horiz_copy.append(self.img_D)

				self.img_horiz_posi.append(str(i) + '-' + str(j))
				self.img_horiz_posi_copy.append(str(j) + '-' + str(i))

				#llenado de piezas verticales
				self.img_D = PhotoImage(file = 'media/v' + str(i) + '-' + str(j) + '.png')
				self.img_vert.append(self.img_D)
				self.img_D = PhotoImage(file = 'media/v' + str(j) + '-' + str(i) + '.png')
				self.img_vert_copy.append(self.img_D)

				self.img_vert_posi.append(str(i) + '-' + str(j))
				self.img_vert_posi_copy.append(str(j) + '-' + str(i))

		self.repartir()

	def repartir(self, cont = 0):

		if cont < 7:
			
			self.llenar_jugador(self.jugador1_v, self.jugador1_v_copy, self.jugador1_v_posi, self.jugador1_v_posi_copy, self.jugador1_h, self.jugador1_h_copy, self.jugador1_h_posi, self.jugador1_h_posi_copy)
			
			self.llenar_jugador(self.jugador2_v, self.jugador2_v_copy, self.jugador2_v_posi, self.jugador2_v_posi_copy, self.jugador2_h, self.jugador2_h_copy, self.jugador2_h_posi, self.jugador2_h_posi_copy)

			self.aux = self.ventana.after(5,self.repartir, cont+1)

		else:
			self.Ganador()

			#print(self.jugador2_v)
			self.jugador2_buton = []
			for i in range(7):
				self.jugador2_buton.append(Button(self.ventana,image = self.jugador2_v[i]))
				self.jugador2_buton[i].place(x = self.X_J2,y=10)
				self.X_J2 += 60

			
			self.P_jugador1=[]

			for i in range(7):
				self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i], text = i ))
				self.P_jugador1[i].place(x = self.X_J1, y = 640)
				self.X_J1+=60

			self.P_jugador1[0].configure(command = lambda: self.asignar(0))
			self.P_jugador1[1].configure(command = lambda: self.asignar(1))
			self.P_jugador1[2].configure(command = lambda: self.asignar(2))
			self.P_jugador1[3].configure(command = lambda: self.asignar(3))
			self.P_jugador1[4].configure(command = lambda: self.asignar(4))
			self.P_jugador1[5].configure(command = lambda: self.asignar(5))
			self.P_jugador1[6].configure(command = lambda: self.asignar(6))
			
			
			#print("P_jugador1",self.P_jugador1[0].cget('text'))
			self.turno()
			
			
			self.ventana.after_cancel(self.aux)

		
	def asignar(self, posi_boton):
		#print(posi_boton)

		tam = len(self.jugador1_v_posi)-1
		#print("asignar",posi_boton, tam)
		
		if posi_boton <= tam:

			self.Jugador_one(self.jugador1_v_posi[posi_boton],posi_boton)

	def llenar_jugador(self, j_v, j_v_copy, j_v_posi, j_v_posi_copy, j_h, j_h_copy, j_h_posi, j_h_posi_copy,):
		
		posicion = random.randint(0,(len(self.img_vert_posi))-1)

		#posicion vertical

		j_v.append(self.img_vert[posicion])
		j_v_copy.append(self.img_vert_copy[posicion])
		j_v_posi.append(self.img_vert_posi[posicion])
		j_v_posi_copy.append(self.img_vert_posi_copy[posicion])

		#posicion horizontal

		j_h.append(self.img_horiz[posicion])
		j_h_copy.append(self.img_horiz_copy[posicion])
		j_h_posi.append(self.img_horiz_posi[posicion])
		j_h_posi_copy.append(self.img_horiz_posi_copy[posicion])


		del self.img_vert[posicion]
		del self.img_vert_copy[posicion]
		del self.img_vert_posi[posicion]
		del self.img_vert_posi_copy[posicion]

		del self.img_horiz[posicion]
		del self.img_horiz_copy[posicion]
		del self.img_horiz_posi[posicion]
		del self.img_horiz_posi_copy[posicion]


	def Robar(self):
		
		if self.img_vert_posi:
			tam = len(self.jugador1_v_posi)

			if tam == 7:

				self.llenar_jugador(self.jugador1_v, self.jugador1_v_copy, self.jugador1_v_posi, self.jugador1_v_posi_copy, self.jugador1_h, self.jugador1_h_copy, self.jugador1_h_posi, self.jugador1_h_posi_copy)
				i = (len(self.jugador1_v_posi))-1
				self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i], text = i ))
				self.P_jugador1[i].place(x = self.X_J1, y = 640)
				self.X_J1 += 60
				self.P_jugador1[7].configure(command = lambda: self.asignar(7))
		
			elif tam == 8:

				self.llenar_jugador(self.jugador1_v, self.jugador1_v_copy, self.jugador1_v_posi, self.jugador1_v_posi_copy, self.jugador1_h, self.jugador1_h_copy, self.jugador1_h_posi, self.jugador1_h_posi_copy)
				i = (len(self.jugador1_v_posi))-1
				self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i], text = i ))
				self.P_jugador1[i].place(x = self.X_J1, y = 640)
				self.X_J1+=60
				self.P_jugador1[8].configure(command = lambda: self.asignar(8))

			elif tam == 9:

				self.llenar_jugador(self.jugador1_v, self.jugador1_v_copy, self.jugador1_v_posi, self.jugador1_v_posi_copy, self.jugador1_h, self.jugador1_h_copy, self.jugador1_h_posi, self.jugador1_h_posi_copy)
				i = (len(self.jugador1_v_posi))-1
				self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i], text = i ))
				self.P_jugador1[i].place(x = self.X_J1, y = 640)
				self.X_J1 += 60
				self.P_jugador1[9].configure(command = lambda: self.asignar(9))

			elif tam == 10:

				self.llenar_jugador(self.jugador1_v, self.jugador1_v_copy, self.jugador1_v_posi, self.jugador1_v_posi_copy, self.jugador1_h, self.jugador1_h_copy, self.jugador1_h_posi, self.jugador1_h_posi_copy)
				i = (len(self.jugador1_v_posi))-1
				self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i], text = i ))
				self.P_jugador1[i].place(x = self.X_J1, y = 640)
				self.X_J1 += 60
				self.P_jugador1[10].configure(command = lambda: self.asignar(10))

			elif tam == 11:

				self.llenar_jugador(self.jugador1_v, self.jugador1_v_copy, self.jugador1_v_posi, self.jugador1_v_posi_copy, self.jugador1_h, self.jugador1_h_copy, self.jugador1_h_posi, self.jugador1_h_posi_copy)
				i = (len(self.jugador1_v_posi))-1
				self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i], text = i ))
				self.P_jugador1[i].place(x = self.X_J1, y = 640)
				self.X_J1 += 60
				self.P_jugador1[11].configure(command = lambda: self.asignar(11))

			elif tam == 12:

				self.llenar_jugador(self.jugador1_v, self.jugador1_v_copy, self.jugador1_v_posi, self.jugador1_v_posi_copy, self.jugador1_h, self.jugador1_h_copy, self.jugador1_h_posi, self.jugador1_h_posi_copy)
				i = (len(self.jugador1_v_posi))-1
				self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i], text = i ))
				self.P_jugador1[i].place(x = self.X_J1, y = 640)
				self.X_J1 += 60
				self.P_jugador1[12].configure(command = lambda: self.asignar(12))

			elif tam == 13:

				self.llenar_jugador(self.jugador1_v, self.jugador1_v_copy, self.jugador1_v_posi, self.jugador1_v_posi_copy, self.jugador1_h, self.jugador1_h_copy, self.jugador1_h_posi, self.jugador1_h_posi_copy)
				i = (len(self.jugador1_v_posi))-1
				self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i], text = i ))
				self.P_jugador1[i].place(x = self.X_J1, y = 640)
				self.X_J1 += 60
				self.P_jugador1[13].configure(command = lambda: self.asignar(13))

			elif tam == 14:

				self.llenar_jugador(self.jugador1_v, self.jugador1_v_copy, self.jugador1_v_posi, self.jugador1_v_posi_copy, self.jugador1_h, self.jugador1_h_copy, self.jugador1_h_posi, self.jugador1_h_posi_copy)
				i = (len(self.jugador1_v_posi))-1
				self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i], text = i ))
				self.P_jugador1[i].place(x = self.X_J1, y = 640)
				self.X_J1 += 60
				self.P_jugador1[14].configure(command = lambda: self.asignar(14))

			elif tam == 15:

				self.llenar_jugador(self.jugador1_v, self.jugador1_v_copy, self.jugador1_v_posi, self.jugador1_v_posi_copy, self.jugador1_h, self.jugador1_h_copy, self.jugador1_h_posi, self.jugador1_h_posi_copy)
				i = (len(self.jugador1_v_posi))-1
				self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i], text = i ))
				self.P_jugador1[i].place(x = self.X_J1, y = 640)
				self.X_J1 += 60
				self.P_jugador1[15].configure(command = lambda: self.asignar(15))

			elif tam == 16:

				self.llenar_jugador(self.jugador1_v, self.jugador1_v_copy, self.jugador1_v_posi, self.jugador1_v_posi_copy, self.jugador1_h, self.jugador1_h_copy, self.jugador1_h_posi, self.jugador1_h_posi_copy)
				i = (len(self.jugador1_v_posi))-1
				self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i], text = i ))
				self.P_jugador1[i].place(x = self.X_J1, y = 640)
				self.X_J1 += 60
				self.P_jugador1[16].configure(command = lambda: self.asignar(16))

			elif tam == 17:

				self.llenar_jugador(self.jugador1_v, self.jugador1_v_copy, self.jugador1_v_posi, self.jugador1_v_posi_copy, self.jugador1_h, self.jugador1_h_copy, self.jugador1_h_posi, self.jugador1_h_posi_copy)
				i = (len(self.jugador1_v_posi))-1
				self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i], text = i ))
				self.P_jugador1[i].place(x = self.X_J1, y = 640)
				self.X_J1 += 60
				self.P_jugador1[17].configure(command = lambda: self.asignar(17))

			elif tam == 18:

				self.llenar_jugador(self.jugador1_v, self.jugador1_v_copy, self.jugador1_v_posi, self.jugador1_v_posi_copy, self.jugador1_h, self.jugador1_h_copy, self.jugador1_h_posi, self.jugador1_h_posi_copy)
				i = (len(self.jugador1_v_posi))-1
				self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i], text = i ))
				self.P_jugador1[i].place(x = self.X_J1, y = 640)
				self.X_J1 += 60
				self.P_jugador1[18].configure(command = lambda: self.asignar(18))

			elif tam == 19:

				self.llenar_jugador(self.jugador1_v, self.jugador1_v_copy, self.jugador1_v_posi, self.jugador1_v_posi_copy, self.jugador1_h, self.jugador1_h_copy, self.jugador1_h_posi, self.jugador1_h_posi_copy)
				i = (len(self.jugador1_v_posi))-1
				self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i], text = i ))
				self.P_jugador1[i].place(x = self.X_J1, y = 640)
				self.X_J1 += 60
				self.P_jugador1[19].configure(command = lambda: self.asignar(19))

			elif tam == 20:

				self.llenar_jugador(self.jugador1_v, self.jugador1_v_copy, self.jugador1_v_posi, self.jugador1_v_posi_copy, self.jugador1_h, self.jugador1_h_copy, self.jugador1_h_posi, self.jugador1_h_posi_copy)
				i = (len(self.jugador1_v_posi))-1
				self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i], text = i ))
				self.P_jugador1[i].place(x = self.X_J1, y = 640)
				self.X_J1 += 60
				self.P_jugador1[20].configure(command = lambda: self.asignar(20))

		else:
			self.mensaje = Label(self.ventana, text = "No quedan piezas para Robar, sigue su competidor")
			self.mensaje.place(x = 350,y = 500)
			self.turn = 2

	def turno(self):

		#self.turn = random.randint(1,2)
		#print(self.turn)
		Max = '0'
		Max2 = '0'
		self.turn = 0
		for i in range(7):
			aux = self.jugador1_v_posi[i]

			tipo_D = self.verifica_pieza(aux)
			#validamos piezas de el jugador 1 para asignar el turno
			#print("jugador1",tipo_D)
			if tipo_D == True:

				if int(aux[0]) >= int(Max[0]):
					#print(aux)
					Max = aux
					#print(Max)

			aux2 = self.jugador2_v_posi[i]

			tipo_D = self.verifica_pieza(aux2)
			#validamos piezas de el jugador 2 para asignar el turno
			#print("jugador2",tipo_D)
			if tipo_D == True:

				if int(aux2[0]) >= int(Max2[0]):
					#print(aux2)
					Max2 = aux2
					#print(Max2)

		if int(Max[0]) < int(Max2[0]):
			#turno para jugador 2
			self.turn = 2
			self.Jugador_two(Max2)

		else:
			#turno para jugador 1

			self.turn = 1
			self.Jugador_two('')


		#print(self.turn)

	def Jugador_two(self, Max):

		if self.ganador == '':
			if self.turn == 2:

				if Max == '':
			
					#posicion=random.randint(0,6)
					lista_posi = []
					for i in range(len(self.jugador2_v_posi)):
						aux = self.jugador2_v_posi[i]

						if aux != None:

							movimiento = self.verifica_mesa(aux, i, self.jugador2_v_posi, self.jugador2_v_posi_copy)

							if movimiento[0] != None and movimiento[1] != None:
								#print("if jugador two",aux)
								lista_posi.append(i)

							elif movimiento[0] != None or movimiento[1] != None:
								#print("if jugador two",aux)
								lista_posi.append(i)

				
					#no logra conseguir una pieza conincidente lo que hace que se vuelva infinito.
					if lista_posi:
						
						posicion = random.choice(lista_posi)
						pieza_D = self.jugador2_v_posi[posicion]
						posi_boton = posicion
						self.acum = self.ventana.after(1000,self.Jugar,pieza_D,posi_boton,self.jugador2_buton,self.jugador2_v,self.jugador2_v_copy,self.jugador2_v_posi,self.jugador2_v_posi_copy,self.jugador2_h,self.jugador2_h_copy,self.jugador2_h_posi,self.jugador2_h_posi_copy)
						self.acum = self.ventana.after(2000,self.delete_Jugador_two,posicion)
						self.acum = self.ventana.after(3000,self.Jugador_two,'')
				
					else:
						if self.img_vert_posi:
							#print(self.img_vert_posi)
							self.llenar_jugador(self.jugador2_v, self.jugador2_v_copy, self.jugador2_v_posi, self.jugador2_v_posi_copy, self.jugador2_h, self.jugador2_h_copy, self.jugador2_h_posi, self.jugador2_h_posi_copy)

							i = (len(self.jugador2_v_posi))-1
							self.jugador2_buton.append(Button(self.ventana,image = self.jugador2_v[i]))
							self.jugador2_buton[i].place(x = self.X_J2,y = 10)
							self.X_J2 += 60

							#incrementamos el tamaño de el contador
							#self.cont += 1

							#print(aux)
							self.ventana.after_cancel(self.acum)
							self.acum = self.ventana.after(1000,self.Jugador_two,'')

						else:
							self.mensaje = Label(self.ventana, text = "No quedan piezas para Robar, sigue su competidor")
							self.mensaje.place(x = 350,y = 500)

							self.turn = 1
				

				else:
					posicion = self.dev_position(Max,self.jugador2_v_posi)
					pieza_D = self.jugador2_v_posi[posicion]
					posi_boton = posicion
					self.acum = self.ventana.after(1000,self.Jugar,pieza_D,posi_boton,self.jugador2_buton,self.jugador2_v,self.jugador2_v_copy,self.jugador2_v_posi,self.jugador2_v_posi_copy,self.jugador2_h,self.jugador2_h_copy,self.jugador2_h_posi,self.jugador2_h_posi_copy)
					self.acum = self.ventana.after(2000,self.delete_Jugador_two,posicion)
					self.acum = self.ventana.after(3000,self.Jugador_two,'')
				
			else:

				self.acum=self.ventana.after(10,self.Jugador_two,'')

		else:
			print("ha ganado %s" %(self.ganador))
			if self.ganador == 'Jugador1':
	
				self.puntos_J1 += self.Puntos(self.jugador2_v_posi)
				self._J1_puntos.configure(text = self.puntos_J1)

				for i in range(len(self.jugador2_v_posi)):
					

					if self.jugador2_v_posi[i] != None:

						self.jugador2_buton[i].destroy()

				for i in range(len(self.mesa_list_posi_D)):
					self.mesa_buton_D[i].destroy()
					
				for i in range(len(self.mesa_list_posi_I)):
					self.mesa_buton_I[i].destroy()

				self.__init__()
				self.carga_img()

			elif self.ganador == 'Jugador2':

				self.puntos_J2 += self.Puntos(self.jugador1_v_posi)
				self._J2_puntos.configure(text = self.puntos_J2)

				for i in range(len(self.jugador1_v_posi)):
					

					if self.jugador1_v_posi[i] != None:

						self.P_jugador1[i].destroy()

				for i in range(len(self.mesa_list_posi_D)):
					self.mesa_buton_D[i].destroy()

				for i in range(len(self.mesa_list_posi_I)):
					self.mesa_buton_I[i].destroy()

				self.__init__()
				self.carga_img()



	def delete_Jugador_two(self,posicion):

		self.turn = 1
		self.jugador2_v[posicion] = None
		self.jugador2_v_copy[posicion] = None
		self.jugador2_v_posi[posicion] = None
		self.jugador2_v_posi_copy[posicion] = None
		self.jugador2_h[posicion] = None
		self.jugador2_h_copy[posicion] = None
		self.jugador2_h_posi[posicion] = None
		self.jugador2_h_posi_copy[posicion] = None
		self.jugador2_buton[posicion] = None
		if self.Tranca('j2')[1] == True:

			self.ganador='Jugador2'

			print("ha finalizado el juego, ha ganado el jugador 2")


		#print(self.jugador2_v_posi)
		#print("turno",self.turn)


	def Jugador_one(self,pieza_D,posi_boton):
		
		#print(posi_boton)
		if self.turn == 1:
			lista_posi = []
			if self.mesa_list_posi_D and self.mesa_list_posi_I:

				verificar = self.verifica_mesa(pieza_D, posi_boton, self.jugador1_v_posi, self.jugador1_v_posi_copy)

			else:

				verificar = '',''
			
			if verificar[0] != None or verificar[1] != None:

			
			
				self.Jugar(pieza_D,posi_boton,self.P_jugador1,self.jugador1_v,self.jugador1_v_copy,self.jugador1_v_posi,self.jugador1_v_posi_copy,self.jugador1_h,self.jugador1_h_copy,self.jugador1_h_posi,self.jugador1_h_posi_copy) 
				
				if self.borrar == 'borrar':
					self.turn = 2
					self.jugador1_v[posi_boton] = None
					self.jugador1_v_copy[posi_boton] = None
					self.jugador1_v_posi[posi_boton] = None
					self.jugador1_v_posi_copy[posi_boton] = None
					self.jugador1_h[posi_boton] = None
					self.jugador1_h_copy[posi_boton] = None
					self.jugador1_h_posi[posi_boton] = None
					self.jugador1_h_posi_copy[posi_boton] = None
					self.P_jugador1[posi_boton] = None

					if self.Tranca('j1')[1] == True:
						print("ha finalizado el juego, ha ganado el jugador 1")
				
				#print(self.jugador1_v_posi)
				#print("turno",self.turn)

			else:


				print("verifica piezas de jugador one")
				j = 0
				for i in range(self.cont2):
					aux = self.jugador1_v_posi[i]
					#print(aux)
					if aux != None:

						movimiento = self.verifica_mesa(aux, i, self.jugador1_v_posi, self.jugador1_v_posi_copy)

						if movimiento[0] != None and movimiento[1] != None:
							#print("if jugador two",aux)
							lista_posi.append(i)
							j += 1

						elif movimiento[0] != None or movimiento[1] != None:
							#print("if jugador two",aux)
							lista_posi.append(i)
							j += 1

				print("puede jugar con " +str(j)+ " piezas, elija la pieza correcta")

				if j == 0:

					print("debes robar pendejo")
					self.Robar()

		else:

			print("No es su turno, porfavor espera tu turno pendejo.")
			


	def Jugar(self, pieza_D,posi_boton,botones,jugador_v,jugador_v_copy,jugador_v_posi,jugador_v_posi_copy,jugador_h,jugador_h_copy,jugador_h_posi,jugador_h_posi_copy):
		#print("Jugar",pieza_D)
		i = self.dev_position(pieza_D,jugador_v_posi)	
		tipo_D = self.verifica_pieza(pieza_D)
		#print(i)

		if not tipo_D:
			if not self.mesa_list_posi_D and not self.mesa_list_posi_I:

				self.mesa_list_posi_D.append(jugador_v_posi[i])
				self.mesa_list_D.append(jugador_h[i])
				self.mesa_list_posi_I.append(jugador_v_posi[i])
				self.mesa_list_I.append(jugador_v[i])
				

				self.mesa_buton_D.append(Button(self.ventana,image = self.mesa_list_D[0]))
				self.mesa_buton_D[0].place(x = self.X1, y = self.Y2)

				self.mesa_buton_I.append(Button(self.ventana,image = self.mesa_list_I[0]))
				self.mesa_buton_I[(len(self.mesa_buton_I))-1].place(x = self.X1, y = self.Y1)

				self.X1 += 105
				self.aux_pixel_D = self.X1

				botones[posi_boton].destroy()
				self.borrar = 'borrar'

			else:
				juego = self.verifica_mesa(pieza_D,i,jugador_v_posi, jugador_v_posi_copy)
				#print("retorno",juego)
				#print("else")
				if juego[0] == 'I' and juego[1] == 'D':
					self.borrar = ''
					if self.turn == 1:
						#aux=random.randint(1,2)
						#if aux==1:
						self.buton_op = Button(self.ventana, text = "izquierda", command = lambda:self.opcion(juego[2],i,posi_boton,juego[0],botones,jugador_h,jugador_v_posi,jugador_v_posi_copy,jugador_h_copy,pieza_D,jugador_v,jugador_v_copy,jugador_h_posi,jugador_h_posi_copy))
						self.buton_op.place(x = 250, y = 550)
							#self.opcion(juego[2],i,posi_boton,juego[0],botones,jugador_h,jugador_v_posi,jugador_v_posi_copy,jugador_h_copy)
						self.buton_op2 = Button(self.ventana, text = "Derecha", command = lambda:self.opcion(juego[3],i,posi_boton,juego[1],botones,jugador_h,jugador_v_posi,jugador_v_posi_copy,jugador_h_copy,pieza_D,jugador_v,jugador_v_copy,jugador_h_posi,jugador_h_posi_copy))
						self.buton_op2.place(x = 410, y = 550)
						#else:
							#self.opcion(juego[3],i,posi_boton,juego[1],botones,jugador_h,jugador_v_posi,jugador_v_posi_copy,jugador_h_copy)
					
					else:
						aux = random.randint(1,2)
						if aux == 1:
							self.opcion(juego[2],i,posi_boton,juego[0],botones,jugador_h,jugador_v_posi,jugador_v_posi_copy,jugador_h_copy,pieza_D,jugador_v,jugador_v_copy,jugador_h_posi,jugador_h_posi_copy)
						else:
							self.opcion(juego[3],i,posi_boton,juego[1],botones,jugador_h,jugador_v_posi,jugador_v_posi_copy,jugador_h_copy,pieza_D,jugador_v,jugador_v_copy,jugador_h_posi,jugador_h_posi_copy)

				elif juego[0] == 'I':
					print("no doble izquierda",(len(self.mesa_list_posi_I)))

					if (len(self.mesa_list_posi_I)) < 5:
						self.X2 -= 105

						if pieza_D == juego[2]:

							self.mesa_list_posi_I.append(jugador_v_posi[i])
							self.mesa_list_I.append(jugador_h[i])
							aux = len(self.mesa_list_I)-1

							self.mesa_buton_I.append(Button(self.ventana,image = self.mesa_list_I[aux]))
							self.mesa_buton_I[(len(self.mesa_buton_I))-1].place(x = self.X2, y = self.Y2)
							botones[posi_boton].destroy()

						else:

							self.mesa_list_posi_I.append(jugador_v_posi_copy[i])
							self.mesa_list_I.append(jugador_h_copy[i])
							aux = len(self.mesa_list_I)-1

							self.mesa_buton_I.append(Button(self.ventana,image = self.mesa_list_I[aux]))
							self.mesa_buton_I[(len(self.mesa_buton_I))-1].place(x = self.X2, y = self.Y2)
							botones[posi_boton].destroy()

						self.borrar = 'borrar'

					else:
						
						print("else pixel excedido izquierda")
						if (len(self.mesa_list_posi_I)) >= 7:
							
							if pieza_D == juego[2]:
								print("if")
								self.mesa_list_posi_I.append(jugador_v_posi[i])
								self.mesa_list_I.append(jugador_h_copy[i])
								aux = len(self.mesa_list_I)-1

								self.mesa_buton_I.append(Button(self.ventana,image = self.mesa_list_I[aux]))
								self.mesa_buton_I[(len(self.mesa_buton_I))-1].place(x = self.X2+54, y = self.Y2_I)
								botones[posi_boton].destroy()
								

							else:
								print("else")
								self.mesa_list_posi_I.append(jugador_v_posi_copy[i])
								self.mesa_list_I.append(jugador_h[i])
								aux = len(self.mesa_list_I)-1

								self.mesa_buton_I.append(Button(self.ventana,image = self.mesa_list_I[aux]))
								self.mesa_buton_I[(len(self.mesa_buton_I))-1].place(x = self.X2+54, y = self.Y2_I)
								botones[posi_boton].destroy()
							
							self.X2 += 105

						else:
							
							print("debemos llamar a la funcion para cruzar")
							self.cruzar(i,pieza_D,posi_boton,botones,jugador_v,jugador_v_copy,jugador_v_posi,jugador_v_posi_copy,jugador_h,jugador_h_copy,jugador_h_posi,jugador_h_posi_copy,'')		

						self.borrar = 'borrar'
					

				elif juego[1] == 'D':
					
					print("no doble derecha", (len(self.mesa_list_posi_D)))
					if (len(self.mesa_list_posi_D)) < 5:

						if juego[3] == pieza_D:

							self.mesa_list_posi_D.append(jugador_v_posi[i])
							self.mesa_list_D.append(jugador_h[i])
							aux = len(self.mesa_list_D)-1

							self.mesa_buton_D.append(Button(self.ventana,image = self.mesa_list_D[aux]))
							self.mesa_buton_D[(len(self.mesa_buton_D))-1].place(x = self.X1, y = self.Y2)
							#self.X1 += 105
							botones[posi_boton].destroy()
					
						else:

							self.mesa_list_posi_D.append(jugador_v_posi_copy[i])
							self.mesa_list_D.append(jugador_h_copy[i])
							aux = len(self.mesa_list_D)-1

							self.mesa_buton_D.append(Button(self.ventana,image = self.mesa_list_D[aux]))
							self.mesa_buton_D[(len(self.mesa_buton_D))-1].place(x = self.X1, y = self.Y2)
							#self.X1 += 105
							botones[posi_boton].destroy()

						self.X1 += 105

						self.borrar = 'borrar'

					else:
						print("else pixel excedido derecha")
						if (len(self.mesa_list_posi_D)) >= 7:
							if juego[3] == pieza_D:

								self.mesa_list_posi_D.append(jugador_v_posi[i])
								self.mesa_list_D.append(jugador_h_copy[i])
								aux = len(self.mesa_list_D)-1
								self.X1 -= 105
								self.mesa_buton_D.append(Button(self.ventana,image = self.mesa_list_D[aux]))
								self.mesa_buton_D[(len(self.mesa_buton_D))-1].place(x = self.X1-50, y = self.Y2_D)
			
								botones[posi_boton].destroy()
								
					
							else:

								self.mesa_list_posi_D.append(jugador_v_posi_copy[i])
								self.mesa_list_D.append(jugador_h[i])
								aux = len(self.mesa_list_D)-1
								self.X1 -= 105
								self.mesa_buton_D.append(Button(self.ventana,image = self.mesa_list_D[aux]))
								self.mesa_buton_D[(len(self.mesa_buton_D))-1].place(x = self.X1-50, y = self.Y2_D)
								
								botones[posi_boton].destroy()
								

						else:

							print("debemos llamar a la funcion para cruzar")
							self.cruzar(i,pieza_D,posi_boton,botones,jugador_v,jugador_v_copy,jugador_v_posi,jugador_v_posi_copy,jugador_h,jugador_h_copy,jugador_h_posi,jugador_h_posi_copy,'')

						self.borrar = 'borrar'

		else:
			#inicializacion de primera pieza doble
			if not self.mesa_list_posi_D and not self.mesa_list_posi_I:

				self.mesa_list_posi_D.append(jugador_v_posi[i])
				self.mesa_list_D.append(jugador_v[i])
				self.mesa_list_posi_I.append(jugador_v_posi[i])
				self.mesa_list_I.append(jugador_v[i])
				

				self.mesa_buton_D.append(Button(self.ventana,image = self.mesa_list_D[0]))
				self.mesa_buton_D[(len(self.mesa_buton_D))-1].place(x = self.X1, y = self.Y1)
				
				self.mesa_buton_I.append(Button(self.ventana,image = self.mesa_list_I[0]))
				self.mesa_buton_I[(len(self.mesa_buton_I))-1].place(x = self.X1, y = self.Y1)

				self.X1 += 56
				#self.aux_pixel_D = self.X1

				botones[posi_boton].destroy()
				self.borrar = 'borrar'


			else:

				juego = self.verifica_mesa(pieza_D,i,jugador_v_posi, jugador_v_posi_copy)
				print("retorno",juego)
				#print("else")

				if juego[0] == 'I' and juego[1] == 'D':

					aux = random.choice(['I','D'])

				elif juego[1] == 'D':
					aux = juego[1]

				elif juego[0] == 'I':
					aux = juego[0]
					

				if aux == 'D':

					print("doble D")
					if (len(self.mesa_list_posi_D)) < 5:
						
						print("derecha")
						self.mesa_list_posi_D.append(jugador_v_posi[i])
						self.mesa_list_D.append(jugador_v[i])
						aux = len(self.mesa_list_D)-1

						self.mesa_buton_D.append(Button(self.ventana,image = self.mesa_list_D[aux]))
						self.mesa_buton_D[(len(self.mesa_buton_D))-1].place(x = self.X1, y = self.Y1)
						#self.X1 += 56
						botones[posi_boton].destroy()
						
						if (len(self.mesa_list_posi_D)) == 5:
							self.Y2_D+=25
							print("se ha puesto un doble al final")

						self.X1 += 56
						#self.aux_pixel_D = self.X1
						self.borrar = 'borrar'

					elif (len(self.mesa_list_posi_D)) == 5:#tipo_D es true
						
						print("derecha")
						self.mesa_list_posi_D.append(jugador_v_posi[i])
						self.mesa_list_D.append(jugador_v[i])
						aux = len(self.mesa_list_D)-1

						self.mesa_buton_D.append(Button(self.ventana,image = self.mesa_list_D[aux]))
						self.mesa_buton_D[(len(self.mesa_buton_D))-1].place(x = self.X1, y = self.Y1)
						#self.X1 += 56
						botones[posi_boton].destroy()	
						self.Y2_D+=25
						self.X1 += 56
						#self.aux_pixel_D = self.X1
						self.borrar = 'borrar'

					else:
						if (len(self.mesa_list_posi_D)) >= 7:
							
							print("cruzar derecha")
							self.mesa_list_posi_D.append(jugador_v_posi_copy[i])
							self.mesa_list_D.append(jugador_v_copy[i])
							aux = len(self.mesa_list_D)-1

							self.mesa_buton_D.append(Button(self.ventana,image = self.mesa_list_D[aux]))
							self.mesa_buton_D[(len(self.mesa_buton_D))-1].place(x = self.X1-105, y = self.Y2_D-25)
							#self.X1 += 56
							botones[posi_boton].destroy()

							self.X1 -= 56
							self.borrar = 'borrar'

						else:

							print("debes llamar a la funcion que va a cruzar")
							self.cruzar(i,pieza_D,posi_boton,botones,jugador_v,jugador_v_copy,jugador_v_posi,jugador_v_posi_copy,jugador_h,jugador_h_copy,jugador_h_posi,jugador_h_posi_copy,'')

				elif aux == 'I':

					print("doble I")
					if (len(self.mesa_list_posi_I)) < 5:
						print("izquierda")
						self.mesa_list_posi_I.append(jugador_v_posi_copy[i])
						self.mesa_list_I.append(jugador_v_copy[i])
						aux = len(self.mesa_list_I)-1

						self.mesa_buton_I.append(Button(self.ventana,image = self.mesa_list_I[aux]))
						self.mesa_buton_I[(len(self.mesa_buton_I))-1].place(x = self.X2-50, y = self.Y1)
						#self.X2 -= 50
						botones[posi_boton].destroy()
						if (len(self.mesa_list_posi_I)) == 5:
							self.Y2_I-=25
							print("se ha puesto un doble al final")


						self.X2 -= 50
						#self.aux_pixel_I = self.X2
						self.borrar = 'borrar'

					elif (len(self.mesa_list_posi_I)) == 5:#tipo_D es true
						print("izquierda")
						self.mesa_list_posi_I.append(jugador_v_posi_copy[i])
						self.mesa_list_I.append(jugador_v_copy[i])
						aux = len(self.mesa_list_I)-1

						self.mesa_buton_I.append(Button(self.ventana,image = self.mesa_list_I[aux]))
						self.mesa_buton_I[(len(self.mesa_buton_I))-1].place(x = self.X2-50, y = self.Y1)
						#self.X2 -= 50
						botones[posi_boton].destroy()
						#self.Y2_I-=25
						self.X2 -= 50
						#self.aux_pixel_I = self.X2
						self.borrar = 'borrar'

					else:
						if (len(self.mesa_list_posi_I)) >= 7:
							
							self.X2 += 50
							
							print("cruzar izquierda")
							self.mesa_list_posi_I.append(jugador_v_posi[i])
							self.mesa_list_I.append(jugador_v[i])
							aux = len(self.mesa_list_I)-1

							self.mesa_buton_I.append(Button(self.ventana,image = self.mesa_list_I[aux]))
							self.mesa_buton_I[(len(self.mesa_buton_I))-1].place(x = self.X2, y = self.Y2_I-25)
							#self.X2 -= 50
							botones[posi_boton].destroy()

							self.borrar = 'borrar'

						else:

							print("debes llamar a la funcion que va a cruzar")
							self.cruzar(i,pieza_D,posi_boton,botones,jugador_v,jugador_v_copy,jugador_v_posi,jugador_v_posi_copy,jugador_h,jugador_h_copy,jugador_h_posi,jugador_h_posi_copy,'')
	

	def cruzar(self,i,pieza_D,posi_boton,botones,jugador_v,jugador_v_copy,jugador_v_posi,jugador_v_posi_copy,jugador_h,jugador_h_copy,jugador_h_posi,jugador_h_posi_copy,direc):

		#i = self.dev_position(pieza_D,jugador_v_posi)
		juego = self.verifica_mesa(pieza_D,i,jugador_v_posi, jugador_v_posi_copy)
		#print("retorno",juego)
		#print("else")
		print("cruzar",juego)
		tipo_D = self.verifica_pieza(pieza_D)

		if not tipo_D:
			if direc == '':
				if juego[0] == 'I' and juego[1] == 'D':

					aux = random.choice(['I','D'])
		
				elif juego[1] == 'D':
					aux = juego[1]

				elif juego[0] == 'I':
					aux = juego[0]

			else:
				aux = direc

			if aux == 'D':

				if juego[3] == pieza_D:

					print("if derecha")
					self.mesa_list_posi_D.append(jugador_v_posi[i])
					self.mesa_list_D.append(jugador_v[i])
					aux = len(self.mesa_list_D)-1

					self.mesa_buton_D.append(Button(self.ventana,image = self.mesa_list_D[aux]))
					self.mesa_buton_D[(len(self.mesa_buton_D))-1].place(x = self.X1-56, y = self.Y2_D+54)
				
					botones[posi_boton].destroy()

					self.Y2_D += 105
				

				else:

					print("else derecha")
					self.mesa_list_posi_D.append(jugador_v_posi_copy[i])
					self.mesa_list_D.append(jugador_v_copy[i])
					aux = len(self.mesa_list_D)-1

					self.mesa_buton_D.append(Button(self.ventana,image = self.mesa_list_D[aux]))
					self.mesa_buton_D[(len(self.mesa_buton_D))-1].place(x = self.X1-56, y = self.Y2_D+54)
				
					botones[posi_boton].destroy()

					self.Y2_D += 105
				

			elif aux == 'I':

				if pieza_D == juego[2]:

					print("if izquierda")
					self.mesa_list_posi_I.append(jugador_v_posi[i])
					self.mesa_list_I.append(jugador_v[i])
					aux = (len(self.mesa_list_I))-1
					self.Y2_I -= 105
					self.mesa_buton_I.append(Button(self.ventana,image = self.mesa_list_I[aux]))
					self.mesa_buton_I[(len(self.mesa_buton_I))-1].place(x = self.X2, y = self.Y2_I)
					#self.X2 -= 50
					botones[posi_boton].destroy()
					

				else: 

					print("else izquierda")
					self.mesa_list_posi_I.append(jugador_v_posi_copy[i])
					self.mesa_list_I.append(jugador_v_copy[i])
					aux = (len(self.mesa_list_I))-1
					self.Y2_I -= 105
					self.mesa_buton_I.append(Button(self.ventana,image = self.mesa_list_I[aux]))
					self.mesa_buton_I[(len(self.mesa_buton_I))-1].place(x = self.X2, y = self.Y2_I)
					#self.X2 -= 50
					botones[posi_boton].destroy()
					

			self.borrar = 'borrar'

		else: 

			print("debe construirse los dobles para el cruze")


	def opcion(self,op,i,posi_boton,direc,botones,jugador_h,jugador_v_posi,jugador_v_posi_copy,jugador_h_copy,pieza_D,jugador_v,jugador_v_copy,jugador_h_posi,jugador_h_posi_copy):
		#print(op, jugador_v_posi)
		#self.buton_op.destroy()
		#self.buton_op2.destroy()
		
		if direc == 'D':
			print("D",len(self.mesa_list_posi_D))
			if (len(self.mesa_list_posi_D)) < 5:
				
				if op == jugador_v_posi[i]:
				
					print("if D funcion opcion")	
					self.mesa_list_posi_D.append(jugador_v_posi[i])
					self.mesa_list_D.append(jugador_h[i])
					aux = len(self.mesa_list_D)-1
					self.mesa_buton_D.append(Button(self.ventana,image = self.mesa_list_D[aux]))
					self.mesa_buton_D[(len(self.mesa_buton_D))-1].place(x = self.X1, y = self.Y2)
					botones[posi_boton].destroy()

				else:

					self.mesa_list_posi_D.append(jugador_v_posi_copy[i])
					self.mesa_list_D.append(jugador_h_copy[i])
					aux = len(self.mesa_list_D)-1

					self.mesa_buton_D.append(Button(self.ventana,image = self.mesa_list_D[aux]))
					self.mesa_buton_D[(len(self.mesa_buton_D))-1].place(x = self.X1, y = self.Y2)
					#self.X1 += 105
					botones[posi_boton].destroy()

				self.X1 += 105
					
			else:
				if (len(self.mesa_list_posi_D)) >= 7:
					
					if op == jugador_v_posi[i]:
						
						self.mesa_list_posi_D.append(jugador_v_posi[i])
						self.mesa_list_D.append(jugador_h_copy[i])
						aux = len(self.mesa_list_D)-1
						self.X1 -= 105
						self.mesa_buton_D.append(Button(self.ventana,image = self.mesa_list_D[aux]))
						self.mesa_buton_D[(len(self.mesa_buton_D))-1].place(x = self.X1-50, y = self.Y2_D)

						botones[posi_boton].destroy()
					else:

						self.mesa_list_posi_D.append(jugador_v_posi_copy[i])
						self.mesa_list_D.append(jugador_h[i])
						aux = len(self.mesa_list_D)-1
						self.X1 -= 105
						self.mesa_buton_D.append(Button(self.ventana,image = self.mesa_list_D[aux]))
						self.mesa_buton_D[(len(self.mesa_buton_D))-1].place(x = self.X1-50, y = self.Y2_D)
								
						botones[posi_boton].destroy()

				else:

					print("debes llamar a la funcion que va a cruzar")
					self.cruzar(i,pieza_D,posi_boton,botones,jugador_v,jugador_v_copy,jugador_v_posi,jugador_v_posi_copy,jugador_h,jugador_h_copy,jugador_h_posi,jugador_h_posi_copy,direc)

			

				
		elif direc == 'I':
			
			print("I",len(self.mesa_list_posi_I))
			if (len(self.mesa_list_posi_I)) < 5:

				print("if izquierdo funcion opcion")
				
				self.X2 -= 105

				if op == jugador_v_posi[i]:

					self.mesa_list_posi_I.append(jugador_v_posi[i])
					self.mesa_list_I.append(jugador_h[i])
					aux = len(self.mesa_list_I)-1

					self.mesa_buton_I.append(Button(self.ventana,image = self.mesa_list_I[aux]))
					self.mesa_buton_I[(len(self.mesa_buton_I))-1].place(x = self.X2, y = self.Y2)
					botones[posi_boton].destroy()

				else:

					self.mesa_list_posi_I.append(jugador_v_posi_copy[i])
					self.mesa_list_I.append(jugador_h_copy[i])
					aux = len(self.mesa_list_I)-1

					self.mesa_buton_I.append(Button(self.ventana,image = self.mesa_list_I[aux]))
					self.mesa_buton_I[(len(self.mesa_buton_I))-1].place(x = self.X2, y = self.Y2)
					botones[posi_boton].destroy()

			else:
				if (len(self.mesa_list_posi_I)) >= 7:
					
					if op == jugador_v_posi[i]:

						self.mesa_list_posi_I.append(jugador_v_posi[i])
						self.mesa_list_I.append(jugador_h_copy[i])
						aux = len(self.mesa_list_I)-1

						self.mesa_buton_I.append(Button(self.ventana,image = self.mesa_list_I[aux]))
						self.mesa_buton_I[(len(self.mesa_buton_I))-1].place(x = self.X2+54, y = self.Y2_I)
						botones[posi_boton].destroy()
						
					
					else:

						print("else")
						self.mesa_list_posi_I.append(jugador_v_posi_copy[i])
						self.mesa_list_I.append(jugador_h[i])
						aux = len(self.mesa_list_I)-1

						self.mesa_buton_I.append(Button(self.ventana,image = self.mesa_list_I[aux]))
						self.mesa_buton_I[(len(self.mesa_buton_I))-1].place(x = self.X2+54, y = self.Y2_I)
						botones[posi_boton].destroy()
							
					self.X2 += 105

				else:

					print("debes llamar a la funcion que va a cruzar")
					self.cruzar(i,pieza_D,posi_boton,botones,jugador_v,jugador_v_copy,jugador_v_posi,jugador_v_posi_copy,jugador_h,jugador_h_copy,jugador_h_posi,jugador_h_posi_copy,direc)


		if self.turn == 1:

			self.buton_op.destroy()
			self.buton_op2.destroy()

			self.turn = 2
			self.jugador1_v[posi_boton] = None
			self.jugador1_v_copy[posi_boton] = None
			self.jugador1_v_posi[posi_boton] = None
			self.jugador1_v_posi_copy[posi_boton] = None
			self.jugador1_h[posi_boton] = None
			self.jugador1_h_copy[posi_boton] = None
			self.jugador1_h_posi[posi_boton] = None
			self.jugador1_h_posi_copy[posi_boton] = None
			self.P_jugador1[posi_boton] = None
			if self.Tranca('j1')[1] == True:
				print("ha finalizado el juego, ha ganado el jugador 2")


	def verifica_pieza(self, pieza_D):

		if pieza_D[0] == pieza_D[2]:
			op = True

		else:
			op = False

		return op
			
	def dev_position(self, pieza_D,jugador_v_posi):
		#print("dev position",pieza_D)

		aux = 0
		for i in jugador_v_posi:

			if pieza_D == i:
				
				break
			
			aux += 1

		return aux
		print("")

	def verifica_mesa(self, pieza_D, i, jugador_v_posi, jugador_v_posi_copy):
		
		D = len(self.mesa_list_posi_D)
		I = len(self.mesa_list_posi_I)

		aux_D = self.mesa_list_posi_D[D-1]
		aux_I = self.mesa_list_posi_I[I-1]
		derecha = None
		izquierda = None
		aux = None
		aux2 = None
		#print(aux_D[2], pieza_D[0])
		if aux_D[2] == pieza_D[0]:
			#print('D')
			derecha = 'D'

			aux = jugador_v_posi[i]
		
		elif aux_D[2] == pieza_D[2]:
			#print('D')
			derecha = 'D'
			aux = jugador_v_posi_copy[i]

		#print(aux_D[2], pieza_D[2])

		#print(aux_I[0], pieza_D[0])
		if aux_I[0] == pieza_D[0]:
			#print('I')
			izquierda = 'I'

			aux2 = jugador_v_posi_copy[i]
		
		elif aux_I[0] == pieza_D[2]:
			#print('I')
			izquierda = 'I'
			aux2 = jugador_v_posi[i]

		#print(aux_D[0], pieza_D[2])
		
		return izquierda, derecha, aux2, aux
		print("")

	#Ganador#

	def Ganador(self):
		acum = 0
		
		for i in self.jugador1_v_posi:

			if i == None:
				acum += 1

		if acum-1 == (len(self.jugador1_v_posi)-1):
			self.ganador = 'Jugador1'
			print(self.ganador)

		acum = 0
		
		for i in self.jugador2_v_posi:

			if i == None:
				acum += 1

		if acum-1 == (len(self.jugador2_v_posi)-1):
			self.ganador = 'Jugador2'	
			print(self.ganador)

		if self.ganador == '':

			self.acum_ganador = self.ventana.after(1,self.Ganador)

		else:
			self.ventana.after_cancel(self.acum_ganador)
			return self.ganador


	def Tranca(self, j):

		izquierda = self.mesa_list_posi_I[((len(self.mesa_list_posi_I))-1)]
		derecha = self.mesa_list_posi_D[((len(self.mesa_list_posi_D))-1)]
		cont = 0
		if izquierda[0] == derecha[2] :

			for i in range((len(self.mesa_list_posi_I))-1):
				
				posi = self.mesa_list_posi_I[i]

				if izquierda[0] == posi[0]:

					cont += 1

				elif izquierda[0] == posi[2]:

					cont += 1


			for i in range((len(self.mesa_list_posi_D))-1):

				posi = self.mesa_list_posi_D[i]

				if derecha[2] == posi[0]:

					cont += 1

				elif derecha[2] == posi[2]:

					cont += 1


			cont+=2

			print("if",izquierda[0],derecha[2])

		print("cont tranca",cont)
		if cont == 7:

			tranca = True

		else:

			tranca = False

		return j, tranca


	def Puntos(self, jugador):

		acum = 0
		for i in jugador:
			if i != None:
				acum = acum + int(i[0]) + int(i[2])

		return acum
	

jugar=domino()
jugar.ventana()