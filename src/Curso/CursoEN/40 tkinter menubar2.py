from tkinter import *
from PIL import Image, ImageTk

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self,master)

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title('GUI') #Texto da janela
        self.pack(fill= BOTH, expand=1)

        quitButton = Button(self, text='Quit', command=self.client_exit)
        quitButton.place(x=0, y=0)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label='Save')
        file.add_command(label='Exit', command=self.client_exit) #Botao em si
        menu.add_cascade(label= 'File', menu=file) #Cascade DIVISAO


        edit = Menu(menu)
        edit.add_command(label='Show Image', command= self.showImg) #command= self.showImg() se chamar a funcao ela sera iniciada assim que rodar o codigo
        edit.add_command(label='Show Text', command=self.showTxt)
        menu.add_cascade(label='Edit', menu=edit)

    def showTxt(self):
        text = Label(self, text='Ola tudo bem ')
        text.pack()


    def showImg(self):
        load = Image.open('ready.png')
        render = ImageTk.PhotoImage(load)

        img = Label(self,image=render)
        img.image = render
        img.place (x=0,y=0)




    def client_exit(self):
        exit()


root = Tk()
root.geometry('550x550')

app = Window(root)

root.mainloop()