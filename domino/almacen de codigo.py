"""
pyimage2
pyimage4
pyimage6
pyimage8
pyimage10
pyimage12
pyimage14
pyimage16
pyimage18
pyimage20
pyimage22
pyimage24
pyimage26
pyimage28
pyimage30
pyimage32
pyimage34
pyimage36
pyimage38
pyimage40
pyimage42
pyimage44
pyimage46
pyimage48
pyimage50
pyimage52
pyimage54
pyimage56
"""
"""def verificador(self, i=0):

		if i < 7:
			#print(i)
			self.posi=self.jugador1_posi[i]
			self.aux = self.ventana.after(1,self.verificador,i+1)

		else:

			self.ventana.after_cancel(self.aux)
			self.aux = self.ventana.after(1,self.verificador)"""



"""del self.jugador1_v[i]
				del self.jugador1_v_copy[i]
				del self.jugador1_v_posi[i]
				del self.jugador1_v_posi_copy[i]"""
"""del self.jugador1_h[i]
				del self.jugador1_h_copy[i]
				del self.jugador1_h_posi[i]
				del self.jugador1_h_posi_copy[i]"""

"""del self.jugador1_v[i]
				del self.jugador1_v_copy[i]
				del self.jugador1_v_posi[i]
				del self.jugador1_v_posi_copy[i]"""
"""del self.jugador1_h[i]
				del self.jugador1_h_copy[i]
				del self.jugador1_h_posi[i]
				del self.jugador1_h_posi_copy[i]"""

"""for i in range(28):
			print(self.img_vert[i])
			print(self.img_vert_posi[i])
			print(self.img_vert_posi_copy[i])
			Button(self.ventana,image = self.img_vert[i]).place(x = x, y = 540)
			self.pieza=Button(self.ventana,image = self.img_vert_copy[i])
			self.pieza.place(x = x, y = 440)
			x += 60"""

		#D_00=Label(self.ventana,image = img_D_v_00).place(x = 40, y = 40)

"""i=0
			#self.verificador()

			self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i],text = 0, command = lambda: self.Jugador_one(self.jugador1_v_posi[0],0)))
			self.P_jugador1[0].place(x = x, y = 540)
			#self.pieza=Button(self.ventana,image = self.img_vert_copy[i])
			#self.pieza.place(x = x, y = 440)
			x+=60
			i+=1 
			#print(self.jugador1)
			#print(self.jugador1_copy)
			#print(self.jugador1_posi)
			#print(self.jugador1_posi_copy)
			


			self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i], text = 1 ,command = lambda: self.Jugador_one(self.jugador1_v_posi[1],1)))
			self.P_jugador1[1].place(x = x, y = 540)
			x+=60
			i+=1

			self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i],text = 2, command = lambda: self.Jugador_one(self.jugador1_v_posi[2],2)))
			self.P_jugador1[2].place(x = x, y = 540)
			x+=60
			i+=1

			self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i],text = 3, command = lambda: self.Jugador_one(self.jugador1_v_posi[3],3)))
			self.P_jugador1[3].place(x = x, y = 540)
			x+=60
			i+=1

			self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i],text = 4, command = lambda: self.Jugador_one(self.jugador1_v_posi[4],4)))
			self.P_jugador1[4].place(x = x, y = 540)
			x+=60
			i+=1

			self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i],text = 5, command = lambda: self.Jugador_one(self.jugador1_v_posi[5],5)))
			self.P_jugador1[5].place(x = x, y = 540)
			x+=60
			i+=1

			self.P_jugador1.append(Button(self.ventana,image = self.jugador1_v[i],text = 6, command = lambda: self.Jugador_one(self.jugador1_v_posi[6],6)))
			self.P_jugador1[6].place(x = x, y = 540)
			x+=60
			i+=1"""

posicion = random.randint(0,aux)
self.jugador1_v.append(self.img_vert[posicion])
			self.jugador1_v_copy.append(self.img_vert_copy[posicion])
			self.jugador1_v_posi.append(self.img_vert_posi[posicion])
			self.jugador1_v_posi_copy.append(self.img_vert_posi_copy[posicion])

			#posicion horizontal

			self.jugador1_h.append(self.img_horiz[posicion])
			self.jugador1_h_copy.append(self.img_horiz_copy[posicion])
			self.jugador1_h_posi.append(self.img_horiz_posi[posicion])
			self.jugador1_h_posi_copy.append(self.img_horiz_posi_copy[posicion])


			del self.img_vert[posicion]
			del self.img_vert_copy[posicion]
			del self.img_vert_posi[posicion]
			del self.img_vert_posi_copy[posicion]

			del self.img_horiz[posicion]
			del self.img_horiz_copy[posicion]
			del self.img_horiz_posi[posicion]
			del self.img_horiz_posi_copy[posicion]

aux-=1
			posicion = random.randint(0,aux)

			#posicion vertical

			self.jugador2_v.append(self.img_vert[posicion])
			self.jugador2_v_copy.append(self.img_vert_copy[posicion])
			self.jugador2_v_posi.append(self.img_vert_posi[posicion])
			self.jugador2_v_posi_copy.append(self.img_vert_posi_copy[posicion])

			#posicion horizontal

			self.jugador2_h.append(self.img_horiz[posicion])
			self.jugador2_h_copy.append(self.img_horiz_copy[posicion])
			self.jugador2_h_posi.append(self.img_horiz_posi[posicion])
			self.jugador2_h_posi_copy.append(self.img_horiz_posi_copy[posicion])

			#print(aux)
			del self.img_vert[posicion]
			del self.img_vert_copy[posicion]
			del self.img_vert_posi[posicion]
			del self.img_vert_posi_copy[posicion]

			del self.img_horiz[posicion]
			del self.img_horiz_copy[posicion]
			del self.img_horiz_posi[posicion]
			del self.img_horiz_posi_copy[posicion]

			def Captura_mouse(self):

		self.canvas1=Canvas(self.ventana, width = 400, height = 400)
		self.canvas1.create_image(500,333,image=self.img_D)
		self.canvas1.bind("<Motion>", self.mover_mouse)
		self.canvas1.bind("<Button-1>", self.presion_mouse)
		self.canvas1.place(x=0, y=530)
		print("canvas")
	
	def presion_mouse(self, evento):
		self.canvas1.create_oval(evento.x-5,evento.y-5,evento.x+5,evento.y+5, fill="red")

	def mover_mouse(self, evento):        
		self.ventana.title(str(evento.x)+"-"+str(evento.y))
		print(str(evento.x))

tam=(len(self.img_vert_posi))-1
						#print(tam)
						posicion=random.randint(0,tam)

						print("entro a la exception")
						self.jugador2_v.append(self.img_vert[posicion])
						self.jugador2_v_copy.append(self.img_vert_copy[posicion])
						self.jugador2_v_posi.append(self.img_vert_posi[posicion])
						self.jugador2_v_posi_copy.append(self.img_vert_posi_copy[posicion])

						#posicion horizontal

						self.jugador2_h.append(self.img_horiz[posicion])
						self.jugador2_h_copy.append(self.img_horiz_copy[posicion])
						self.jugador2_h_posi.append(self.img_horiz_posi[posicion])
						self.jugador2_h_posi_copy.append(self.img_horiz_posi_copy[posicion])

						tam=(len(self.img_vert_posi))-1
						#print(tam)
						posicion=random.randint(0,tam)

						print("entro a la exception")
						self.jugador2_v.append(self.img_vert[posicion])
						self.jugador2_v_copy.append(self.img_vert_copy[posicion])
						self.jugador2_v_posi.append(self.img_vert_posi[posicion])
						self.jugador2_v_posi_copy.append(self.img_vert_posi_copy[posicion])

						#posicion horizontal

						self.jugador2_h.append(self.img_horiz[posicion])
						self.jugador2_h_copy.append(self.img_horiz_copy[posicion])
						self.jugador2_h_posi.append(self.img_horiz_posi[posicion])
						self.jugador2_h_posi_copy.append(self.img_horiz_posi_copy[posicion])
del self.img_vert[posicion]
						del self.img_vert_copy[posicion]
						del self.img_vert_posi[posicion]
						del self.img_vert_posi_copy[posicion]

						del self.img_horiz[posicion]
						del self.img_horiz_copy[posicion]
						del self.img_horiz_posi[posicion]
						del self.img_horiz_posi_copy[posicion]

						
			#print(self.jugador2_buton)
			#print(self.jugador1_v_posi)
			
			#jugador1_buton=[]
			"""for i in range(7):

				self.P_jugador1.append(jugador1_buton)"""

				#if self.turn == 1:
				#if aux==1:
							self.buton_op = Button(self.ventana, text = "izquierda", command = lambda:self.opcion(juego[2],i,posi_boton,juego[0],botones,jugador_h,jugador_v_posi,jugador_v_posi_copy,jugador_h_copy))
							self.buton_op.place(x = 250, y = 550)
							#self.opcion(juego[2],i,posi_boton,juego[0],botones,jugador_h,jugador_v_posi,jugador_v_posi_copy,jugador_h_copy)
							self.buton_op2 = Button(self.ventana, text="Derecha", command = lambda:self.opcion(juego[3],i,posi_boton,juego[1],botones,jugador_h,jugador_v_posi,jugador_v_posi_copy,jugador_h_copy))
							self.buton_op2.place(x = 410, y = 550)
						#else:
							#self.opcion(juego[3],i,posi_boton,juego[1],botones,jugador_h,jugador_v_posi,jugador_v_posi_copy,jugador_h_copy)
					
					else:
						aux = random.randint(1,2)
						if aux == 1:
							self.opcion(juego[2],i,posi_boton,juego[0],botones,jugador_h,jugador_v_posi,jugador_v_posi_copy,jugador_h_copy)
						else:
							self.opcion(juego[3],i,posi_boton,juego[1],botones,jugador_h,jugador_v_posi,jugador_v_posi_copy,jugador_h_copy)

							#self.aux_pixel_D = self.X1

				"""else:
					self.X1 -= 56

					print("derecha")
					self.mesa_list_posi_D.append(jugador_v_posi_copy[i])
					self.mesa_list_D.append(jugador_v_copy[i])
					aux = len(self.mesa_list_D)-1

					self.mesa_buton_D.append(Button(self.ventana,image = self.mesa_list_D[aux]))
					self.mesa_buton_D[(len(self.mesa_buton_D))-1].place(x = self.X1, y = self.Y1+200)
					#self.X1 += 56
					botones[posi_boton].destroy()"""

				#self.borrar = 'borrar'

				#self.X1 += 56
				#print("doble D",self.pixel_D, self.aux_pixel_D)
				#if self.pixel_D > self.aux_pixel_D:

if juego[1] == 'D':

				print("derecha")
				self.mesa_list_posi_D.append(jugador_v_posi[i])
				self.mesa_list_D.append(jugador_v[i])
				aux = len(self.mesa_list_D)-1

				self.mesa_buton_D.append(Button(self.ventana,image = self.mesa_list_D[aux]))
				self.mesa_buton_D[(len(self.mesa_buton_D))-1].place(x = self.X1, y = self.Y2_D)
				
				botones[posi_boton].destroy()

				self.Y2_D += 105

			elif juego[0] == 'I':
								
				print("izquierda")
				self.mesa_list_posi_I.append(jugador_v_posi_copy[i])
				self.mesa_list_I.append(jugador_v_copy[i])
				aux = (len(self.mesa_list_I))-1

				self.mesa_buton_I.append(Button(self.ventana,image = self.mesa_list_I[aux]))
				self.mesa_buton_I[(len(self.mesa_buton_I))-1].place(x = self.X2, y = self.Y2_I)
				#self.X2 -= 50
				botones[posi_boton].destroy()

				self.Y2_I -= 105

			self.borrar = 'borrar'

if juego[1] == 'D':
						

						print("doble D",self.pixel_D, self.aux_pixel_D)
						if self.pixel_D > self.aux_pixel_D:

							print("derecha")
							self.mesa_list_posi_D.append(jugador_v_posi[i])
							self.mesa_list_D.append(jugador_v[i])
							aux = len(self.mesa_list_D)-1

							self.mesa_buton_D.append(Button(self.ventana,image = self.mesa_list_D[aux]))
							self.mesa_buton_D[(len(self.mesa_buton_D))-1].place(x = self.X1, y = self.Y1)
							#self.X1 += 56
							botones[posi_boton].destroy()

							self.X1 += 56
							self.aux_pixel_D = self.X1

						else:
							self.X1 -= 56

							print("derecha")
							self.mesa_list_posi_D.append(jugador_v_posi_copy[i])
							self.mesa_list_D.append(jugador_v_copy[i])
							aux = len(self.mesa_list_D)-1

							self.mesa_buton_D.append(Button(self.ventana,image = self.mesa_list_D[aux]))
							self.mesa_buton_D[(len(self.mesa_buton_D))-1].place(x = self.X1, y = self.Y1+200)
							#self.X1 += 56
							botones[posi_boton].destroy()

						#self.borrar = 'borrar'

					elif juego[0] == 'I':

						print("doble I",self.pixel_I, self.aux_pixel_I)
						if self.pixel_I < self.aux_pixel_I:
							
							print("izquierda")
							self.mesa_list_posi_I.append(jugador_v_posi_copy[i])
							self.mesa_list_I.append(jugador_v_copy[i])
							aux = len(self.mesa_list_I)-1

							self.mesa_buton_I.append(Button(self.ventana,image = self.mesa_list_I[aux]))
							self.mesa_buton_I[(len(self.mesa_buton_I))-1].place(x = self.X2-50, y = self.Y1)
							#self.X2 -= 50
							botones[posi_boton].destroy()

							self.X2 -= 50
							self.aux_pixel_I = self.X2

						else:

							print("izquierda")
							self.mesa_list_posi_I.append(jugador_v_posi[i])
							self.mesa_list_I.append(jugador_v[i])
							aux = len(self.mesa_list_I)-1

							self.mesa_buton_I.append(Button(self.ventana,image = self.mesa_list_I[aux]))
							self.mesa_buton_I[(len(self.mesa_buton_I))-1].place(x = self.X2-50, y = self.Y1+200)
							#self.X2 -= 50
							botones[posi_boton].destroy()

							self.X2 += 50

						#self.borrar = 'borrar'

					self.borrar = 'borrar'

				print(self.pixel_I, self.aux_pixel_I)


				else:
				
				print("else D funcion opcion")
				if (len(self.mesa_list_posi_D)) < 5:
					
					self.mesa_list_posi_D.append(jugador_v_posi_copy[i])
					self.mesa_list_D.append(jugador_h_copy[i])
					aux = len(self.mesa_list_D)-1
					self.mesa_buton_D.append(Button(self.ventana,image = self.mesa_list_D[aux]))
					self.mesa_buton_D[(len(self.mesa_buton_D))-1].place(x = self.X1, y = self.Y2)
				
					self.X1 += 105
					
					botones[posi_boton].destroy()
				
				else:
					if (len(self.mesa_list_posi_D)) >= 7:

						self.mesa_list_posi_D.append(jugador_v_posi_copy[i])
						self.mesa_list_D.append(jugador_h[i])
						aux = len(self.mesa_list_D)-1

						self.X1 -= 105

						self.mesa_buton_D.append(Button(self.ventana,image = self.mesa_list_D[aux]))
						self.mesa_buton_D[(len(self.mesa_buton_D))-1].place(x = self.X1-55, y = self.Y2_D)

						botones[posi_boton].destroy()

					else: 

						print("debes llamar a la funcion que va a cruzar")
						self.cruzar(i,pieza_D,posi_boton,botones,jugador_v,jugador_v_copy,jugador_v_posi,jugador_v_posi_copy,jugador_h,jugador_h_copy,jugador_h_posi,jugador_h_posi_copy)

						
			else:

				print("else I funcion opcion")
				if (len(self.mesa_list_posi_I)) < 5:
					
					self.mesa_list_posi_I.append(jugador_v_posi_copy[i])
					self.mesa_list_I.append(jugador_h_copy[i])
					aux = len(self.mesa_list_I)-1

					self.X2 -= 105
					
					self.mesa_buton_I.append(Button(self.ventana,image = self.mesa_list_I[aux]))
					self.mesa_buton_I[(len(self.mesa_buton_I))-1].place(x = self.X2, y = self.Y2)
					botones[posi_boton].destroy()

				else:
					if (len(self.mesa_list_posi_I)) >= 7:

						self.mesa_list_posi_I.append(jugador_v_posi_copy[i])
						self.mesa_list_I.append(jugador_h[i])
						aux = len(self.mesa_list_I)-1

						self.mesa_buton_I.append(Button(self.ventana,image = self.mesa_list_I[aux]))
						self.mesa_buton_I[(len(self.mesa_buton_I))-1].place(x = self.X2+54, y = self.Y2_I)
						botones[posi_boton].destroy()
						self.X2 += 105

					else:

						print("debes llamar a la funcion que va a cruzar")
						self.cruzar(i,pieza_D,posi_boton,botones,jugador_v,jugador_v_copy,jugador_v_posi,jugador_v_posi_copy,jugador_h,jugador_h_copy,jugador_h_posi,jugador_h_posi_copy)
