from tkinter import*
from PIL import Image, ImageTk
Login=Tk()
import subprocess
taskBarHeight = 40

#Configurações da tela
Login.title("Acesso ao Petshop Dogin's")
Login.resizable(False, False)

width_screen = Login.winfo_screenwidth()
height_screen = Login.winfo_screenheight() - taskBarHeight

width = 1240
height = 700

posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

Login.maxsize(width, height)
Login.minsize(width, height)

Login.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
Login.configure(bg='#fff')

#Estilização do Logo
logo_dogins_origin = Image.open("images/mainLogo.png")
logo_resize = logo_dogins_origin.resize((140, 50), Image.ANTIALIAS)
logoDogins = ImageTk.PhotoImage(logo_resize)
logo_dog = Label(Login, image = logoDogins , bg="#fff")
logo_dog.place(relx = .150, rely = .10, anchor = "n")

#botao voltar ao menu
def abrir_tela_menu():
    subprocess.run(["python", "Menu.py"])
btn_menu = Button(Login, text = "Voltar ao menu", bd = 0, bg = "#FFF", fg = "#777777", font = "Helvetica 10 underline", activebackground = "#FFF", activeforeground = "#777" , command=abrir_tela_menu)
btn_menu.place(relx = .830, rely = .10, anchor = "n")


#titulo dos serviços
txt_titulo = Label(Login,text="Cadastro dos Serviços" ,bg = "#FFF", font=("Helvetica 20 bold"))
txt_titulo.place(relx = .450, rely = .20, anchor = "n")
logo_cora= Image.open("images/heart-icon.png")
cora = logo_cora.resize((20, 15), Image.ANTIALIAS)
logo_coracao = ImageTk.PhotoImage(cora)
coracao = Label(Login, image = logo_coracao , bg="#fff")
coracao.place(relx = .585, rely = .21, anchor = "n")

#campo codigo do serviço
txt_codigo = Label(Login,text="Código do Serviço" ,bg = "#FFF", font=("Helvetica 10"))
txt_codigo.place(relx = .350, rely = .30, anchor = "n")
lbl_codigo = Entry(Login)
lbl_codigo.place(relx = .360, rely = .33, anchor = "n" ,  width="130" , height="20")

#campo nome
txt_nome = Label(Login,text="Nome" ,bg = "#FFF", font=("Helvetica 10"))
txt_nome.place(relx = .500, rely = .30, anchor = "n")
lbl_nome = Entry(Login)
lbl_nome.place(relx = .560, rely = .33, anchor = "n" ,  width="190" , height="20")

#campo valor
txt_valor = Label(Login,text="Valor" ,bg = "#FFF", font=("Helvetica 10"))
txt_valor.place(relx = .320, rely = .40, anchor = "n")
lbl_valor = Entry(Login)
lbl_valor.place(relx = .345, rely = .43, anchor = "n",  width="90" , height="20")

#campo tempo de duração
txt_duracao = Label(Login,text="Tempo de duração" ,bg = "#FFF", font=("Helvetica 10"))
txt_duracao.place(relx = .525, rely = .40, anchor = "n")
lbl_duracao = Entry(Login)
lbl_duracao.place(relx = .530, rely = .43, anchor = "n",  width="120" , height="20")

#Descrição
txt_descricao = Label(Login,text="Descrição" ,bg = "#FFF", font=("Helvetica 10"))
txt_descricao.place(relx = .335, rely = .50, anchor = "n")
lbl_descricao = Entry(Login)
lbl_descricao.place(relx = .470, rely = .53, anchor = "n" ,  width="400" , height="50")

#botões de salvar alterar e excluir
btn_salvar=Button(Login,text="Salvar", bg="#85d3ff")
btn_salvar.place(relx = .330, rely = .75, anchor = "n",  width="80" , height="25")
btn_alterar = Button(Login, text="Alterar")
btn_alterar.place(relx= .480, rely=.75, anchor= "n",  width="80" , height="25")
btn_excluir = Button(Login,text="Excluir")
btn_excluir.place(relx= .630, rely=.75 , anchor= "n",  width="80" , height="25")



Login.mainloop()