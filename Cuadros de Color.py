from tkinter import *
global A,B,boton,c,r
r=2
c=2
B="White"
A="Blue"
boton=[[B,B,B,B,B],[B,B,B,B,B],[B,B,A,B,B],[B,B,B,B,B],[B,B,B,B,B]]
def up ():
    global c,r
    if(r!=0):
        r=r-1
    else:
        r=4
    change()
def left ():
    global c,r
    if(c!=0):
        c=c-1
    else:
        c=4
    change()
def down ():
    global c,r
    if(r!=4):
        r=r+1
    else:
        r=0
    change()
def right ():
    global c,r
    if(c!=4):
        c=c+1
    else:
        c=0
    change()
def change ():
    global A,B,boton,c,r
    ren=0
    col=0
    for ren in [0,1,2,3,4]:
        for col in [0,1,2,3,4]:
            if(ren==r and col==c):
                boton[ren][col]=A
            else:
                boton[ren][col]=B

    B00=Button(ventana,bg=boton[0][0],state="disable",text="       ")
    B00.grid(column=0,row=0)
    B01=Button(ventana,bg=boton[0][1],state="disable",text="       ")
    B01.grid(column=1,row=0)
    B02=Button(ventana,bg=boton[0][2],state="disable",text="       ")
    B02.grid(column=2,row=0)
    B03=Button(ventana,bg=boton[0][3],state="disable",text="       ")
    B03.grid(column=3,row=0)
    B03=Button(ventana,bg=boton[0][4],state="disable",text="       ")
    B03.grid(column=4,row=0)
    
    B10=Button(ventana,bg=boton[1][0],state="disable",text="       ")
    B10.grid(column=0,row=1)
    B11=Button(ventana,bg=boton[1][1],state="disable",text="       ")
    B11.grid(column=1,row=1)
    B12=Button(ventana,bg=boton[1][2],state="disable",text="       ")
    B12.grid(column=2,row=1)
    B13=Button(ventana,bg=boton[1][3],state="disable",text="       ")
    B13.grid(column=3,row=1)
    B13=Button(ventana,bg=boton[1][4],state="disable",text="       ")
    B13.grid(column=4,row=1)
    
    B20=Button(ventana,bg=boton[2][0],state="disable",text="       ")
    B20.grid(column=0,row=2)
    B21=Button(ventana,bg=boton[2][1],state="disable",text="       ")
    B21.grid(column=1,row=2)
    B22=Button(ventana,bg=boton[2][2],state="disable",text="       ")
    B22.grid(column=2,row=2)
    B03=Button(ventana,bg=boton[2][3],state="disable",text="       ")
    B03.grid(column=3,row=2)
    B03=Button(ventana,bg=boton[2][4],state="disable",text="       ")
    B03.grid(column=4,row=2)

    B30=Button(ventana,bg=boton[3][0],state="disable",text="       ")
    B30.grid(column=0,row=3)
    B31=Button(ventana,bg=boton[3][1],state="disable",text="       ")
    B31.grid(column=1,row=3)
    B32=Button(ventana,bg=boton[3][2],state="disable",text="       ")
    B32.grid(column=2,row=3)
    B33=Button(ventana,bg=boton[3][3],state="disable",text="       ")
    B33.grid(column=3,row=3)
    B33=Button(ventana,bg=boton[3][4],state="disable",text="       ")
    B33.grid(column=4,row=3)
    
    B40=Button(ventana,bg=boton[4][0],state="disable",text="       ")
    B40.grid(column=0,row=4)
    B41=Button(ventana,bg=boton[4][1],state="disable",text="       ")
    B41.grid(column=1,row=4)
    B42=Button(ventana,bg=boton[4][2],state="disable",text="       ")
    B42.grid(column=2,row=4)
    B43=Button(ventana,bg=boton[4][3],state="disable",text="       ")
    B43.grid(column=3,row=4)
    B43=Button(ventana,bg=boton[4][4],state="disable",text="       ")
    B43.grid(column=4,row=4)
def Arriba ():
    ventana.bin("Up",up)

ventana=Tk()

B0=Button(ventana,bg=boton[0][0],command=up,text="↑",background=("Red"))
B0.grid(column=9,row=0)
B1=Button(ventana,bg=boton[0][1],command=down,text="↓",background=("Red"))
B1.grid(column=9,row=1)
B2=Button(ventana,bg=boton[0][2],command=right,text="→",background=("Red"))
B2.grid(column=10,row=1)
B2=Button(ventana,bg=boton[0][2],command=left,text="←",background=("Red"))
B2.grid(column=8,row=1)
change()


ventana.mainloop()
