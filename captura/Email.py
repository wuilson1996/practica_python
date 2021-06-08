from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
import smtplib
from tkinter import *
from tkinter import filedialog

def enviar(Email_send,Password,Email_receiver,Affair,Text):

	msg=MIMEMultipart()

	#mensaje=texto			#mensaje de el correo

	#password = Passw						#contraseña
	msg['From'] = Email_send				#correo para el logeo
	msg['To'] = Email_receiver				#correoa quien se envia
	msg['Subject'] = Affair					#asunto de el envio de correo

	msg.attach(MIMEText(Text, 'plain'))	#carga de texto
	#print(self.files)
		
	server=smtplib.SMTP('smtp.gmail.com: 587')
	server.starttls()
	server.login(msg['From'],Password)
	server.sendmail(msg['From'],msg['To'],msg.as_string())
	server.quit()
	print("correo fue enviado con exito a %s:" % (msg['To']))


	