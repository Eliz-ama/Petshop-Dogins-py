from tkinter import *
from PIL import Image, ImageTk
OC=Tk()
import subprocess

taskBarHeight = 40

#Configurações da tela
OC.title("Acesso ao Petshop Dogin's")
OC.resizable(False, False)

width_screen = OC.winfo_screenwidth()
height_screen = OC.winfo_screenheight() - taskBarHeight

width = 1240
height = 700

posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

OC.maxsize(width, height)
OC.minsize(width, height)

OC.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
OC.configure(bg='#fff')

#titulo operação concluida com sucesso
txt_titulo = Label(OC,text="Operação concluída com sucesso!" ,bg = "#FFF", font=("Helvetica 20 bold"))
txt_titulo.place(relx = .495, rely = .10, anchor = "n")
logo_cora= Image.open("images/heart-icon.png")
cora = logo_cora.resize((20, 15), Image.ANTIALIAS)
logo_coracao = ImageTk.PhotoImage(cora)
coracao = Label(OC, image = logo_coracao , bg="#fff")
coracao.place(relx = .700, rely = .11, anchor = "n")

#Imagem do dog
image= Image.open("images/dog.png")
dog = image.resize((500 , 350), Image.ANTIALIAS)
logo_dog= ImageTk.PhotoImage(dog)
doguinho = Label(OC , image = logo_dog , bg="#fff")
doguinho.place(relx= .500, rely = .25, anchor = "n")

# botão fechar
btn_fechar=Button(OC,text="Fechar", bg="#85d3ff", command=lambda:quit())
btn_fechar.place(relx = .490, rely = .80, anchor = "n",  width="110" , height="30" )




OC.mainloop()