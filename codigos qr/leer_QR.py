from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox, filedialog
from pyzbar.pyzbar import decode, ZBarSymbol
import cv2
import pyautogui
import numpy as np
import threading
from PIL import Image, ImageTk, ImageDraw
import os
from generate_qr import *
 
class App:
    def __init__(self,font_video=0):
        self.active_camera = False
        self.info = []
        self.codelist = []
        self.appName = 'QR Code Reader'
        self.windows = Tk()
        self.windows.title(self.appName)
        self.color = "#33DDFF"
        self.windows['bg']=self.color
        self.font_video=font_video
        self.windows.geometry("815x600")
        self.windows.resizable(0,0)
        

        self.code = StringVar()
        self.name = StringVar()
        self.tipo = StringVar()
        self.precio = IntVar()
        self.comentario = StringVar()
        self.cap = ' '

        self.label=Label(self.windows,text=self.appName,font=15,bg='blue',
                         fg='white').pack(side=TOP,fill=BOTH)
        self.btnSave = Button(self.windows,text="GUARDAR INFO",bg='light blue',command=self.guardar)
        self.btnSave.place(x = 300, y = 630)
 
        self.display=scrolledtext.ScrolledText(self.windows,width=86,background='snow3'
                                        ,height=4,padx=10, pady=10,font=('Arial', 10))
        self.display.place(x = 5, y = 540)
 
        self.canvas=Canvas(self.windows,bg='black',width=640,height=0)
        self.canvas.place(x = 5, y = 30)
        self.btnLoad = Button(self.windows,text="CARGAR ARCHIVO",width=29,bg='goldenrod2',
                    activebackground='red',command=self.abrir)
        self.btnLoad.place(x = 5,y = 510)
        self.btnCamera = Button(self.windows,text="INICIAR LECTURA POR CAMARA",width=30,bg='goldenrod2',
                                activebackground='red',command=self.active_cam)
        self.btnCamera.place(x = 217,y = 510)
        self.btnScreen = Button(self.windows,text="DETECTAR EN PANTALLA",width=29,bg='goldenrod2',
                                activebackground='red',command=self.screen_shot)
        self.btnScreen.place(x = 434,y = 510)


        label = Label(self.windows, text = 'Codigo del Producto', bg = self.color)
        label.place(x = 650, y = 35)

        entry = Entry(self.windows,textvariable = self.code)
        entry.place(x = 650, y = 60)

        #nombre de producto
        label2 = Label(self.windows, text = 'Nombre', bg = self.color)
        label2.place(x = 650, y = 80)

        entry2 = Entry(self.windows,textvariable = self.name)
        entry2.place(x = 650, y = 100)

        #Tpo de producto
        label = Label(self.windows, text = 'Tipo de producto', bg = self.color)
        label.place(x = 650, y = 120)

        entry = Entry(self.windows,textvariable = self.tipo)
        entry.place(x = 650, y = 140)

        #Precio
        label = Label(self.windows, text = 'Precio', bg = self.color)
        label.place(x = 650, y = 160)

        entry = Entry(self.windows,textvariable = self.precio)
        entry.place(x = 650, y = 180)

        #comentario
        label = Label(self.windows, text = 'comentario', bg = self.color)
        label.place(x = 650, y = 200)

        entry = Entry(self.windows,textvariable = self.comentario)
        entry.place(x = 650, y = 220)

        #boton ir
        buton = Button(self.windows,text = 'Create QR', command = self.save_code, bg='goldenrod2', activebackground='red')
        buton.place(x = 725, y = 260)

        buton = Button(self.windows,text = 'Create DB', command = lambda: conection_DB(self.code, self.name, self.tipo, self.precio, self.comentario), bg='goldenrod2', activebackground='red')
        buton.place(x = 650, y = 260)

        buton = Button(self.windows,text = 'Leer DB', command = lambda: leer(self.code, self.name, self.tipo, self.precio, self.comentario), bg='goldenrod2', activebackground='red')
        buton.place(x = 650, y = 290)

        buton = Button(self.windows,text = 'Limpiar', command = self.limpiarCampo, bg='goldenrod2', activebackground='red')
        buton.place(x = 725, y = 290)

        buton = Button(self.windows,text = 'Usar QR', command = lambda: Usar_QR(self.code), bg='goldenrod2', activebackground='red')
        buton.place(x = 725, y = 320)
        
        self.BarraMenu()
 
        self.windows.mainloop()

    def view_qr(self):

        print("aqui veremos el qr generado")
        File = str(self.code.get())+'.png'
        print(File)

        Qr_generated = Label(self.windows, text = "Codigo QR Generado")
        Qr_generated.place(x = 650, y = 400)
        self.img = PhotoImage(file = 'media/'+File).subsample(3)
        self.label_img=Label(self.windows,image = self.img)
        self.label_img.place(x = 650, y = 450)

    def save_code(self):
        save(self.code, self.name, self.tipo, self.precio, self.comentario)
        self.view_qr()

    def limpiarCampo(self):

        self.code.set("")
        self.name.set("")
        self.tipo.set("")
        self.precio.set(0)
        self.comentario.set("")
 
    def guardar(self):
        if len(self.display.get('1.0',END))>1:
            documento = filedialog.asksaveasfilename(initialdir="/",
                        title="Guardar en",defaultextension='.txt')
            if documento != "":
                archivo_guardar = open(documento,"w",encoding="utf-8")
                linea=""
                for c in str(self.display.get('1.0',END)):
                    linea=linea+c
                archivo_guardar.write(linea)
                archivo_guardar.close()
                messagebox.showinfo("GUARDADO","INFORMACIÓN GUARDADA EN \'{}\'".format(documento))
 
    def abrir(self):
        ruta = filedialog.askopenfilename(initialdir="/",title="SELECCIONAR ARCHIVO",
                    filetypes =(("png files","*.png") ,("jpg files","*.jpg")))
        if ruta != "":
            archivo = cv2.imread(ruta)
            self.info = decode(archivo)
            if self.info != []:
                self.display.delete('1.0',END)
                for i in self.info:
                    self.display.insert(END,(i[0].decode('utf-8'))+'\n')
            else:
                messagebox.showwarning("ARCHIVO NO VÁLIDO","NO SE DETECTÓ CÓDIGO QR.")
        
        #print(self.display)


    def screen_shot(self):
        pyautogui.screenshot("QRsearch_screenshoot.jpg")
        archivo = cv2.imread("QRsearch_screenshoot.jpg")
        self.info = decode(archivo)
        if self.info != []:
            self.display.delete('1.0',END)
            for i in self.info:
                self.display.insert(END,(i[0].decode('utf-8'))+'\n')
        else:
            messagebox.showwarning("QR NO ENCONTRADO","NO SE DETECTÓ CÓDIGO")
        os.remove("QRsearch_screenshoot.jpg")
 
    def visor(self):
        ret, frame=self.get_frame()
        if ret:
            #try:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0,0,image=self.photo,anchor=NW)
            self.windows.after(15,self.visor)
            
            """except:
                self.ventana.after(15,self.visor)"""
 
    def active_cam(self):
        if self.active_camera == False:
            self.active_camera = True
            self.VideoCaptura()
            self.visor()
        else:
            self.active_camera = False
            self.codelist = []
            self.btnCamera.configure(text="INICIAR LECTURA POR CAMARA")
            self.vid.release()
            self.canvas.delete('all')
            self.canvas.configure(height=0)
 
    def capta(self,frm):
        self.info = decode(frm)
        aux = ' '
        cv2.putText(frm, "Muestre el codigo delante de la camara para su lectura", (84, 37), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        if self.info != []:
            self.display.delete('1.0',END)

            for code in self.info:
                if code not in self.codelist:
                    #print(code)
                    self.codelist.append(code)
                    self.cap = (code[0].decode('utf-8'))+'\n'
                    self.display.insert(END,(code[0].decode('utf-8'))+'\n')
                self.draw_rectangle(frm)
        
        if self.cap != ' ':

            self.code.set(self.cap)


    def get_frame(self):
        if self.vid.isOpened():
            verif,frame=self.vid.read()
            if verif:
                self.btnCamera.configure(text="CERRAR CAMARA")
                self.capta(frame)
                return(verif,cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                messagebox.showwarning("CAMARA NO DISPONIBLE","""La cámara está siendo utilizada por otra aplicación.
                Cierrela e intentelo de nuevo.""")
                self.active_cam()
                return(verif,None)
        else:
            verif=False
            return(verif,None)
 
    def draw_rectangle(self,frm):
        codes = decode(frm)
        for code in codes:
            data = code.data.decode('ascii')
            x, y, w, h = code.rect.left, code.rect.top, \
                        code.rect.width, code.rect.height
            cv2.rectangle(frm, (x,y),(x+w, y+h),(255, 0, 0), 6)
            cv2.putText(frm, code.type, (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 50, 255), 2)
 
    def VideoCaptura(self):
        self.vid = cv2.VideoCapture(self.font_video)
        if self.vid.isOpened():
            self.width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
            self.height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
            self.canvas.configure(width=self.width,height=self.height)
        else:
            messagebox.showwarning("CAMARA NO DISPONIBLE","El dispositivo está desactivado o no disponible")
            self.display.delete('1.0',END)
            self.active_camera = False
 
    def __del__(self):
        if self.active_camera == True:
            self.vid.release()

    def BarraMenu(self):

        barra_Menu=Menu(self.windows)

        self.windows.config(menu=barra_Menu, width=300, height=300)
        
        archivoMenu=Menu(barra_Menu, tearoff=0)
        archivoMenu.add_command(label="Nuevo", command=lambda:Nuevo(self.windows, self.aux))
        archivoMenu.add_command(label="Guardar")
        archivoMenu.add_command(label="Guardar como")
        archivoMenu.add_separator()
        archivoMenu.add_command(label="Cerrar")
        archivoMenu.add_command(label="Salir")

        archivoEdicion=Menu(barra_Menu, tearoff=0)
        archivoEdicion.add_command(label="modificar factura")
        archivoEdicion.add_command(label="Factura")
        archivoEdicion.add_command(label="Cotizacion")
        #archivoEdicion.add_command(label="Pegar")
        #archivoEdicion.add_command(label="Cortar")

        archivoHerramientas=Menu(barra_Menu, tearoff=0)
        archivoHerramientas.add_command(label="Numero-Factura")
        archivoHerramientas.add_command(label="Crear-Archivo")
        archivoHerramientas.add_command(label="Tamaño de Factura")
        
        Colores=Menu(archivoHerramientas, tearoff=0)
        Colores.add_command(label="Normal")
        Colores.add_command(label="Color1")
        Colores.add_command(label="Color2")
        Colores.add_command(label="Color3")
        Colores.add_command(label="Color4")
        Colores.add_command(label="Color5")
        Colores.add_command(label="Color6")
        Colores.add_command(label="Color7")
        Colores.add_command(label="Color8")
        
        archivoAyuda=Menu(barra_Menu, tearoff=0)
        archivoAyuda.add_command(label="Licencia")
        archivoAyuda.add_command(label="Documentacion")
        archivoAyuda.add_command(label="Acerca de...")

        barra_Menu.add_cascade(label="Archivo", menu=archivoMenu)

        barra_Menu.add_cascade(label="Edicion", menu=archivoEdicion)

        barra_Menu.add_cascade(label="Herramientas", menu=archivoHerramientas)

        barra_Menu.add_cascade(label="Ayuda", menu=archivoAyuda)

        archivoHerramientas.add_cascade(label="Colores",menu=Colores)


if __name__=="__main__":
    App()