from tkinter import *

from  math import *

class calcy:

    dataInput = '';newInput = ''

    def __init__(self, obj):

       self.win = obj

       self.var = StringVar()

       self.txt = Entry(self.win,textvariable=self.var,bg='gray',width=37,bd=5,font=('arial,20,bold'))

       self.txt.grid(row=0, column=0, padx=2, sticky=W)

       self.buttonframe = Frame(self.win,bg='gray')

       self.buttonframe.grid(row=2,column=0,columnspan=2)

       self.btndel=Button(self.buttonframe,text='Del',activebackground='sky blue',width=8,height=2,font=('arial,15,bold'),fg='white',bg='black',bd=5,command=self.Trimstring)

       self.btndel.grid(row=2,column=0,sticky=W,padx=2)

       self.btncancle = Button(self.buttonframe, text='Clear',activebackground='sky blue', width=8,height=2,fg='white',bg='black', font=('arial,15,bold'),bd=5,command=self.Btncancle)

       self.btncancle.grid(row=2, column=0, sticky=W,padx=90)

       self.btndivide = Button(self.buttonframe, text='/', activebackground='sky blue',width=8,height=2,fg='white',bg='black', font=('arial,15,bold'), bd=5,command=lambda :self.GetbtnInput(self.btndivide))

       self.btndivide.grid(row=2, column=0, sticky=W, padx=175)

       self.btnmul = Button(self.buttonframe, text='*',activebackground='sky blue', width=7,height=2,fg='white',bg='black', font=('arial,15,bold'),bd=5,command=lambda :self.GetbtnInput(self.btnmul))

       self.btnmul.grid(row=2, column=0, sticky=W, padx=264)

       self.btnplus = Button(self.buttonframe, text='+',activebackground='sky blue', width=8, height=2,fg='white',bg='black',font=('arial,15,bold'), bd=5,command=lambda :self.GetbtnInput(self.btnplus))

       self.btnplus.grid(row=3, column=0, sticky=W, padx=2)

       self.btnminus = Button(self.buttonframe, text='-',activebackground='sky blue', width=8,height=2,fg='white',bg='black', font=('arial,15,bold'), bd=5,command=lambda :self.GetbtnInput(self.btnminus))

       self.btnminus.grid(row=3, column=0, sticky=W, padx=90)

       self.btnsqrt = Button(self.buttonframe, text='sqrt',activebackground='sky blue', width=8, height=2,fg='white',bg='black',font=('arial,15,bold'), bd=5,command=self.squareroot)

       self.btnsqrt.grid(row=3, column=0, sticky=W, padx=175)

       self.btnx2 = Button(self.buttonframe, text='**', width=7,activebackground='sky blue', height=2,font=('arial,15,bold'),fg='white',bg='black', bd=5,command=lambda :self.GetbtnInput(self.btnx2))

       self.btnx2.grid(row=3, column=0, sticky=W, padx=264)

       self.btnone = Button(self.buttonframe, text='1',activebackground='sky blue', width=8,height=2, font=('arial,15,bold'),fg='white',bg='black', bd=5,command=lambda :self.GetbtnInput(self.btnone))

       self.btnone.grid(row=4, column=0, sticky=W, padx=2)

       self.btntwo = Button(self.buttonframe, text='2',activebackground='sky blue', width=8, height=2,font=('arial,15,bold'),fg='white',bg='black', bd=5,command=lambda :self.GetbtnInput(self.btntwo))

       self.btntwo.grid(row=4, column=0, sticky=W, padx=90)

       self.btnthree = Button(self.buttonframe, text='3',activebackground='sky blue', width=8,height=2, font=('arial,15,bold'),fg='white',bg='black', bd=5,command=lambda :self.GetbtnInput(self.btnthree))

       self.btnthree.grid(row=4, column=0, sticky=W, padx=175)

       self.btnfour = Button(self.buttonframe, text='4',activebackground='sky blue', width=7,height=2, font=('arial,15,bold'),fg='white',bg='black', bd=5,command=lambda :self.GetbtnInput(self.btnfour))

       self.btnfour.grid(row=4, column=0, sticky=W, padx=264)

       self.btnfive = Button(self.buttonframe, text='5',activebackground='sky blue', width=8, height=2,font=('arial,15,bold') ,fg='white',bg='black',bd=5,command=lambda :self.GetbtnInput(self.btnfive))

       self.btnfive.grid(row=5, column=0, sticky=W, padx=2)

       self.btnsix = Button(self.buttonframe, text='6',activebackground='sky blue', width=8, height=2,font=('arial,15,bold'),fg='white',bg='black', bd=5,command=lambda :self.GetbtnInput(self.btnsix))

       self.btnsix.grid(row=5, column=0, sticky=W, padx=90)

       self.btnseven = Button(self.buttonframe, text='7',activebackground='sky blue', width=8,height=2, font=('arial,15,bold'),fg='white',bg='black', bd=5,command=lambda :self.GetbtnInput(self.btnseven))

       self.btnseven.grid(row=5, column=0, sticky=W, padx=175)

       self.btneight = Button(self.buttonframe, text='8',activebackground='sky blue', width=7,height=2, font=('arial,15,bold'),fg='white',bg='black', bd=5,command=lambda :self.GetbtnInput(self.btneight))

       self.btneight.grid(row=5, column=0, sticky=W, padx=264)

       self.btnnine = Button(self.buttonframe, text='9',activebackground='sky blue', width=8,height=2, font=('arial,15,bold'),fg='white',bg='black', bd=5,command=lambda :self.GetbtnInput(self.btnnine))

       self.btnnine.grid(row=6, column=0, sticky=W, padx=2)

       self.btnzero = Button(self.buttonframe, text='0',activebackground='sky blue', width=8,height=2, font=('arial,15,bold'),fg='white',bg='black', bd=5,command=lambda :self.GetbtnInput(self.btnzero))

       self.btnzero.grid(row=6, column=0, sticky=W, padx=89)

       self.btnbinary = Button(self.buttonframe, text='bin',activebackground='sky blue', width=7, height=2,fg='white',bg='black', font=('arial,8,bold'), bd=5,command=self.binary)

       self.btnbinary.grid(row=6, column=0, sticky=W, padx=264)

       self.btnhex = Button(self.buttonframe, text='hex',activebackground='sky blue', width=12, height=2,fg='white',bg='black', font=('arial,15,bold'), bd=5,command=self.hexadecimal)

       self.btnhex.grid(row=7, column=0, sticky=W,padx=2)

       self.btneoct = Button(self.buttonframe, text='oct',activebackground='sky blue', width=11, height=2,fg='white',bg='black', font=('arial,8,bold'), bd=5,command=self.octal)

       self.btneoct.grid(row=7, column=0, sticky=W, padx=127)

       self.btnefactorial = Button(self.buttonframe, text='fact',activebackground='sky blue', width=9, height=2,fg='white',bg='black', font=('arial,15,bold'), bd=5,command=self.find_factorial)

       self.btnefactorial.grid(row=7, column=0, sticky=W, padx=245)

       self.btnequal = Button(self.buttonframe, text='=', width=8,activebackground='sky blue', height=2,fg='white',bg='black', font=('arial,15,bold'), bd=5,command=lambda: self.Getoperation())

       self.btnequal.grid(row=6, column=0, sticky=W, padx=175)

    def GetbtnInput(self, widget):

       if widget['text']=='1' or widget['text']=='2'or widget['text']=='3' or widget['text']=='4'or widget['text']=='5' or widget['text']=='6'or widget['text']=='6' or widget['text']=='7'or widget['text']=='8' or widget['text']=='9'or widget['text']=='0':

          self.dataInput+=widget['text']

          self.newInput+=self.dataInput

          self.var.set(self.newInput)

          self.dataInput =''

       elif widget['text']=='+' or widget['text']=='-' or widget['text'] == '*' or widget['text'] == '/' or widget['text']=='**':

          self.dataInput += widget['text']

          self.newInput += self.dataInput

          self.var.set(self.newInput)

          self.dataInput = ''


    def Getoperation(self):

        self.evaluate = eval(self.newInput)

        self.txt.delete(0, 'end')

        self.var.set(self.evaluate)

        self.newInput = ''

    def binary(self):

        self.binary = "{0:b}".format(int(self.newInput))

        self.txt.delete(0, 'end')

        self.var.set(self.binary)

        self.newInput = ''

    def octal(self):

        self.oct = "{0:o}".format(int(self.newInput))

        self.txt.delete(0, 'end')

        self.var.set(self.oct)

        self.newInput = ''

    def hexadecimal(self):

        self.hex = "{0:x}".format(int(self.newInput))

        self.txt.delete(0, 'end')

        self.var.set(self.hex)

        self.newInput = ''

    def squareroot(self):

        self.txt.delete(0, 'end')

        self.var.set(sqrt(int(self.newInput)))

        self.newInput = ''

    def find_factorial(self):

        self.fact = factorial(int(self.newInput))

        self.txt.delete(0, 'end')

        self.var.set(str(self.fact))

        self.newInput = ''

    def Btncancle(self):

       self.newInput = ''

       self.var.set(self.newInput)

    def Trimstring(self):

       l = len(self.newInput)

       self.newInputdel = self.newInput.replace(self.newInput[l-1], '')

       self.newInput = self.newInputdel

       self.var.set(self.newInput)

cal = Tk()

ob = calcy(cal)

cal.iconbitmap('calcy.ico')

cal.title('Calculator')

cal.geometry('347x368')

cal.resizable(0, 0)

cal.mainloop()