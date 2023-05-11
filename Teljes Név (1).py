# Import the required libraries
from tkinter import *
import math
# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("1600x500")

class forgato:
    canvas=0
    vonalak=[]
    szog=0
    szogSebesseg=0.1
    színek=[]
    def __init__(self,canvas,vonalak):
        self.canvas=canvas
        self.vonalak=vonalak
        for i,betu in  enumerate (self.vonalak):
    
            betu += betu[:2]
            betu = self.nagyit(betu,1)
           
            self.vonalak[i]=self.eltol(betu,200,200)

        self.kozepSzamol()


    def forgat(self,pontok, szog):
        vissza = []
        for i, pont in enumerate(pontok):
            if i % 2 == 0:
                szogRadian=math.radians(szog)
                x = pontok[i]*math.cos(szogRadian) - pontok[i+1]*math.sin(szogRadian)
                
                y=pontok[i]*math.sin(szogRadian)+pontok[i+1]*math.cos(szogRadian)

                vissza.append(x)
                vissza.append(y)
        return vissza

    def eltol(self,pontok, x, y):
        vissza = []
        for e, pont in enumerate(pontok):
            if e % 2 == 0:
                vissza.append(pont + x)
            else:
                vissza.append(pont + y)
        return vissza

    def nagyit(self,pontok, meret = 1):
    
        vissza = []
        for e in pontok:
                vissza.append(e * meret)
        return vissza
    def rajzol(self):
            canvas.delete("all")
            self.szog+=self.szogSebesseg
            #szog+=0.5
            #print(szog)
            for i,betu in enumerate(self.vonalak):
                betu =self.eltol(betu,-self.kozep[0],-self.kozep[1])
                betu =self.forgat(betu,self.szog)
                betu =self.eltol(betu,self.kozep[0],self.kozep[1])
                
                self.canvas.create_line(betu, fill=self.színek[i], width=5)
    def kozepSzamol(self):        
        self.kozep=[0,0]
        db=0
        for betu in TAMAS:
            xK=betu[::2]
            yK=betu[1::2]
            self.kozep[0]+=sum(xK)
            self.kozep[1]+=sum(yK)
            db+=len(xK)
        self.kozep[0]/=db
        self.kozep[1]/=db   

# Create a canvas widget
canvas=Canvas(win, width=1600, height=500)
canvas.pack()
TAMAS=[[30,10,150,10,150,40,105,40,105,250,75,250,75,40,30,40,30,10],
       [250,10,350,10,400,240,360,240,320,40,280,40,250,240,210,240,250,10],
       [450,10,510,10,530,70,550,10,610,10,610,240,575,240,575,50,550,110,510,110,485,50,485,240,450,240,450,10],
       [710,10,810,10,860,240,820,240,780,40,740,40,710,240,670,240,710,10],
       [730,110,795,110,800,140,725,140],
       [910,10,1030,10,1030,40,950,40,950,145,1030,145,1030,240,910,240,910,210,990,210,990,180,910,180,910,10,]]
# Add a line in canvas widget
#T


#A
#canvas.create_line(, fill="black", width=5)
#canvas.create_line(270,110,335,110,340,140,265,140, fill="black", width=5)

#M
#canvas.create_line(450,10,510,10,530,70,550,10,610,10,610,240,575,240,575,50,550,110,510,110,485,50,485,240,450,240,450,10, fill="black", width=5)
#A2

#canvas.create_line(710,10,810,10,860,240,820,240,780,40,740,40,710,240,670,240,710,10, fill="black", width=5)
#canvas.create_line(730,110,795,110,800,140,725,140, fill="black", width=5)

#S
#A
#canvas.create_line(910,10,1030,10,1030,40,950,40,950,145,1030,145,1030,240,910,240,910,210,990,210,990,180,910,180,910,10, fill="black", width=5)
elso=forgato(canvas,TAMAS)

while True:
    elso.rajzol()
    win.update_idletasks()
    win.update()

#Z
#T

#canvas.create_line(0,100,150,500, fill="blue", width=10)
#canvas.create_line(0,100,100,100, fill="red", width=10)
#print(TAMAS)

