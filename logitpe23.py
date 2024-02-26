from tkinter import *
from math import *
import time
raam = Tk()
raam.title("Kell")
w = 500
h = 500
tahvel = Canvas(raam, width=w, height=h, bg="black")
tahvel.create_oval(10,10,w-10,h-10,fill="white")
tahvel.create_oval(w/2-5,h/2-5,w/2+5,h/2+5,fill="white")
sek_id = tahvel.create_line(w/2,h/2,w/2,20,fill="red")
min_id = tahvel.create_line(w/2,h/2,w/2,20,fill="blue")
h_id = tahvel.create_line(w/2,h/2,w/2,100,fill="blue")
def uuenda():
        sekundid = time.localtime().tm_sec
        r = min(w/2,h/2)-20
        x = r*cos(pi/2-sekundid/60.0*2*pi)
        y = -r*sin(pi/2-sekundid/60.0*2*pi)
        tahvel.coords(sek_id, 0, 0, x, y)
        tahvel.move(sek_id, w/2, h/2)
        
        minutid = time.localtime().tm_min
        r = min(w/2,h/2)-20
        x = r*cos(pi/2-minutid/60.0*2*pi)
        y = -r*sin(pi/2-minutid/60.0*2*pi)
        tahvel.coords(min_id, 0, 0, x, y)
        tahvel.move(min_id, w/2, h/2)
        
        tunnid = time.localtime().tm_hour
        r = min(w/2,h/2)-90
        x = r*cos(pi/2-tunnid/60.0*2*pi)
        y = -r*sin(pi/2-tunnid/60.0*2*pi)
        tahvel.coords(h_id, 0, 0, x, y)
        tahvel.move(h_id, w/2, h/2)
        raam.after(1000, uuenda)

uuenda()
tahvel.pack()
raam.mainloop()