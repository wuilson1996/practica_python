from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
import smtplib
from tkinter import *
from tkinter import filedialog

class App_envio_emails(): 

	def __init__(self):
		
		self.ventana=Tk()
		self.ventana.title("mensajeria de correo")
		self.ventana.iconbitmap("icono.ico")
		self.ventana.geometry("500x400")
		self.ventana.resizable(0,0)
		
		self.entrada()
		
		self.ventana.mainloop()

	def entrada(self):
		
		#variables
		self.filesImg=''
		self.filesAudio=''

		asunto=StringVar()
		texto=StringVar()
		correo_envia=StringVar()
		correo_recibe=StringVar()
		passw=StringVar()
		cant=IntVar()
		color="#85ea7d"

		self.image=PhotoImage(file="fondo.png")
		self.fondo=Label(self.ventana,image=self.image).place(x=-2,y=-2)
		
		self.frame=Frame(self.ventana,bg=color)
		self.frame.place(x=150,y=10)

		#mensajes y entradas de datos
		self.Tcorreo_envia=Label(self.frame,text="Correo-Emisor").grid(row=0,column=0, padx=10,pady=10)
		self.correo_Entry=Entry(self.frame,textvariable=correo_envia).grid(row=0,column=1,padx=10,pady=10)

		self.Tpassw_envia=Label(self.frame,text="password-correo-Emisor").grid(row=1,column=0,padx=10,pady=10)
		self.passw_Entry=Entry(self.frame,show="*",textvariable=passw).grid(row=1,column=1,padx=10,pady=10)

		self.Tcorreo_recibe=Label(self.frame,text="Correo-receptor").grid(row=2,column=0,padx=10,pady=10)
		self.correo_recibe_Entry=Entry(self.frame,textvariable=correo_recibe).grid(row=2,column=1,padx=10,pady=10)

		self.Tasunto=Label(self.frame,text="Asunto").grid(row=3,column=0,padx=10,pady=10)
		self.asunto_Entry=Entry(self.frame,textvariable=asunto).grid(row=3,column=1,padx=10,pady=10)

		self.Ttexto=Label(self.frame,text="Texto_mensaje").grid(row=4,column=0,padx=10,pady=10)
		self.texto_Entry=Entry(self.frame,textvariable=texto).grid(row=4,column=1,padx=10,pady=10)

		self.boton_enviar=Button(self.frame,text="cargar imagen",command=self.carga_image)
		self.boton_enviar.grid(row=5,column=0,padx=10,pady=10)

		self.boton_enviar=Button(self.frame,text="cargar musica",command=self.carga_audio)
		self.boton_enviar.grid(row=6,column=0,padx=10,pady=10)

		self.Ttexto=Label(self.frame,text="Cantidad-Correos").grid(row=7,column=0,padx=10,pady=10)
		self.texto_Entry=Entry(self.frame,textvariable=cant).grid(row=7,column=1,padx=10,pady=10)
		
		self.boton_enviar=Button(self.frame,text="Envia",command= lambda:self.enviar(correo_envia.get(),passw.get(),correo_recibe.get(),asunto.get(),texto.get(),cant.get()))
		self.boton_enviar.grid(row=8,column=1,padx=10,pady=10)

		self.boton_salir=Button(self.ventana, text="Salir",command=self.salir).place(x=0,y=0)


	def enviar(self,Correo_envia,Passw,Correo_recibe,Asunto,Texto,cant):

		
		for i in range(cant):
		
			msg=MIMEMultipart()

			#mensaje=texto			#mensaje de el correo

			password = Passw						#contraseña
			msg['From'] = Correo_envia				#correo para el logeo
			msg['To'] = Correo_recibe				#correoa quien se envia
			msg['Subject'] = Asunto				#asunto de el envio de correo

			msg.attach(MIMEText(Texto, 'plain'))	#carga de texto
			#print(self.files)
		

			if(self.filesImg!=''):

				for i in self.filesImg:
					print(i)
					fileImg = open(i,"rb")
					msg.attach(MIMEImage(fileImg.read()))

			if(self.filesAudio!=''):

				for i in self.filesAudio:
					print(i)
					fileAudio = open(i,"rb")
					msg.attach(MIMEImage(fileAudio.read()))

			server=smtplib.SMTP('smtp.gmail.com: 587')

			server.starttls()

			server.login(msg['From'],password)

			server.sendmail(msg['From'],msg['To'],msg.as_string())

			server.quit()

			print("correo",i," enviado con exito a %s:" % (msg['To']))


		self.entrada()
		


	def carga_image(self):

		self.filesImg=filedialog.askopenfilenames(title="selecciona un archivo",filetypes=(("Image File", "*.jpg"),("Image File", "*.png"),("Image File", "*.gif")))

	def carga_audio(self):

		self.filesAudio=filedialog.askopenfilenames(title="selecciona un archivo",filetypes=(''))


	def salir(self):

		self.ventana.destroy()


enviar_email=App_envio_emails()