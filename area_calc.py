from tkinter import *
def set0():
    src.set(0)
    src2.set(0)
    src3.set(0)
    src4.set(0)
    src5.set(0)
    src6.set(0)
    dest.set(0)
def remover():
    global sq,rect,tri,cir,lbl1,lbl2,lbl3,lbl4,lbl5,lbl6,entMsg,entMsg2,entMsg3,entMsg4,entMsg5,entMsg6
    if sq==True:
        lbl1.grid_remove()
        entMsg.grid_remove()
        sq=False
    elif rect==True:
        lbl2.grid_remove()
        entMsg2.grid_remove()
        lbl3.grid_remove()
        entMsg3.grid_remove()
        rect=False
    elif cir==True:
        lbl4.grid_remove()
        entMsg4.grid_remove()
        cir=False
    elif tri==True:
        lbl5.grid_remove()
        entMsg5.grid_remove()
        lbl6.grid_remove()
        entMsg6.grid_remove()
        tri=False
def square():
    remover()
    set0()
    global sq
    lbl1.grid()
    entMsg.grid()
    sq=True
def rectangle():
    remover()
    set0()
    global rect
    lbl2.grid()
    lbl3.grid()
    entMsg2.grid()
    entMsg3.grid()
    rect=True
def circle():
    remover()
    set0()
    lbl4.grid()
    entMsg4.grid()
    global cir
    cir=True
def triangle():
    set0()
    remover()
    global tri
    lbl5.grid()
    entMsg5.grid()
    lbl6.grid()
    entMsg6.grid()
    tri=True
def calsq():
    side = src.get()
    length = src2.get()
    breadth = src3.get()
    radius=src4.get()
    height=src5.get()
    base=src6.get()
    if side!=0:
        area = side * side
    elif length!=0 and breadth!=0:
        area = length * breadth
        print(2)
    elif radius!=0:
        area = 3.14 * radius
    elif height!=0 and base!=0:
        area = 1/2 * base * height
    else:
        area = 0
    dest.set(area)
    remover()
root=Tk()
root.title('Area Calculator')
root.geometry("900x700")
root['bg']='pink'

label=Label(root)
label["text"]="Choose shape whose area you want to find"
label["font"]=14
label['width']=150
label.grid(row=0,column=0,columnspan=4,pady=(10,20))

src = IntVar()
src2 = IntVar()
src3 = IntVar()
src4 = IntVar()
src5 = IntVar()
src6 = IntVar()

btnsqaure=Button(root)
btnsqaure["text"]="Square"
btnsqaure["font"]=20
btnsqaure["bg"]="brown"
btnsqaure['fg']='white'
btnsqaure["width"]=20
btnsqaure["height"]=3
btnsqaure["command"]=square
btnsqaure.grid(row=1,column=0,columnspan=1,padx=(135,10))

sq=False
lbl1=Label(root)
lbl1['text']="ENTER SIDE OF SQUARE"
lbl1['font']=14
lbl1['width']=83
lbl1.grid(row=3,column=0,columnspan=4,pady=(20,20))
lbl1.grid_remove()
entMsg = Entry(root)
entMsg["textvariable"] = src
entMsg["font"] = 1
entMsg["width"] = 83
entMsg.grid(row=4, column=0, columnspan=4)
entMsg.grid(pady=(10, 50))
entMsg.grid_remove()

btnrect=Button(root)
btnrect['text']='Rectangle'
btnrect['font']=20
btnrect['bg']='blue'
btnrect['fg']='white'
btnrect['width']=20
btnrect['height']=3
btnrect['command']=rectangle
btnrect.grid(row=1,column=0,columnspan=3,padx=(30,10))

rect=False
lbl3=Label(root)
lbl3['text']="ENTER THE LENGTH OF RECTANGLE"
lbl3['font']=14
lbl3['width']=83
lbl3.grid(row=3,column=0,columnspan=4,pady=(20,20))
entMsg3 = Entry(root)
entMsg3["textvariable"] = src2
entMsg3["font"] = 1
entMsg3["width"] = 83
entMsg3.grid(row=4, column=0, columnspan=4)
entMsg3.grid(pady=(10, 50))
lbl2=Label(root)
lbl2['text']="ENTER THE BREADTH OF RECTANGLE"
lbl2['font']=14
lbl2['width']=83
lbl2.grid(row=5,column=0,columnspan=4,pady=(20,20))
entMsg2 = Entry(root)
entMsg2["textvariable"] = src3
entMsg2["font"] = 1
entMsg2["width"] = 83
entMsg2.grid(row=6, column=0, columnspan=4)
entMsg2.grid(pady=(10, 50))
lbl2.grid_remove()
lbl3.grid_remove()
entMsg2.grid_remove()
entMsg3.grid_remove()

btncir=Button(root)
btncir['text']='Circle'
btncir['font']=20
btncir['bg']='orange'
btncir['fg']='white'
btncir['width']=20
btncir['height']=3
btncir['command']=circle
btncir.grid(row=1,column=0,columnspan=6,padx=(220,0))

cir=False
lbl4=Label(root)
lbl4['text']="ENTER RADIUS OF CIRCLE"
lbl4['font']=14
lbl4['width']=83
lbl4.grid(row=3,column=0,columnspan=4,pady=(20,20))
entMsg4 = Entry(root)
entMsg4["textvariable"] = src4
entMsg4["font"] = 1
entMsg4["width"] = 83
entMsg4.grid(row=4, column=0, columnspan=4)
entMsg4.grid(pady=(10, 50))
lbl4.grid_remove()
entMsg4.grid_remove()

btntri=Button(root)
btntri['text']='Triangle'
btntri['font']=20
btntri['bg']='grey'
btntri['fg']='white'
btntri['width']=20
btntri['height']=3
btntri['command']=triangle
btntri.grid(row=1,column=0,columnspan=7,padx=(750,0))

tri=False
lbl5=Label(root)
lbl5['text']="ENTER THE HEIGHT OF TRIANGLE"
lbl5['font']=14
lbl5['width']=83
lbl5.grid(row=3,column=0,columnspan=4,pady=(20,20))
entMsg5 = Entry(root)
entMsg5["textvariable"] = src5
entMsg5["font"] = 1
entMsg5["width"] = 83
entMsg5.grid(row=4, column=0, columnspan=4)
entMsg5.grid(pady=(10, 50))
lbl6=Label(root)
lbl6['text']="ENTER THE BASE OF TRIANGLE"
lbl6['font']=14
lbl6['width']=83
lbl6.grid(row=5,column=0,columnspan=4,pady=(20,20))
entMsg6 = Entry(root)
entMsg6["textvariable"] = src6
entMsg6["font"] = 1
entMsg6["width"] = 83
entMsg6.grid(row=6, column=0, columnspan=4)
entMsg6.grid(pady=(10, 50))
lbl5.grid_remove()
lbl6.grid_remove()
entMsg5.grid_remove()
entMsg6.grid_remove()

btncalculate=Button(root)
btncalculate["text"]="Calculate"
btncalculate["font"]=20
btncalculate["bg"]="yellow"
btncalculate["width"]=20
btncalculate["height"]=3
btncalculate["command"]=calsq
btncalculate.grid(row=100,column=0,columnspan=4)
btncalculate.grid(padx=(15,15),pady=(50,10))

dest = IntVar()
entconvMsg = Entry(root, textvariable=dest, font=1, width=83)
entconvMsg.grid(row=99, column=0, columnspan=4)
entconvMsg.grid(pady=(50, 20))
lbldest=Label(root)
lbldest['text']='AREA WILL APPEAR HERE'
lbldest['font']=20
lbldest['width']=83
lbldest.grid(row=98,column=0,columnspan=4,pady=(50,20))
root.mainloop()