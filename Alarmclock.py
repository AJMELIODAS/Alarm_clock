from tkinter import *
import time as t
import pygame as pg

pg.mixer.init()

#def clock()
def clock():
    h='%I'
    m='%M'
    s="%S"
    am_pm="%p"
    #ct= current time
    ct=t.strftime(str(h)+''+':'+str(m)+''+':'+str(s)+''+':'+str(am_pm))
    c.configure(text=ct)
    c.after(1000,clock)

# GUI
b = Tk()
b.geometry('500x550')
b.title('Alarm clock')
b.iconbitmap('C:/Users/new/Downloads/icon.ico')
b.config(bg='white')
b.resizable(0,0)

# Set Alarm method
def setalarm():
    lbl.config(text='ALARM IS SET!')
    h='%I'
    m='%M'
    present=int(t.strftime('%S'))
    newh=hrs.get()
    newm=mins.get()
    if hrs.get()<10:
        newh='0'+str(newh)
    else:
        newh=str(newh)
    if mins.get()<10:
        newm='0'+str(newm)
    else:
        newm=str(newm)
    check.after(1000,setalarm)
    if newh==str(t.strftime(h)) and newm==str(t.strftime(m)) and ap.get()==t.strftime('%p'):
        pg.mixer.music.load('C:/Users/new/Downloads/'+str(sel_music.get())+'.mp3')
        pg.mixer.music.play(0)

 # Stop alarm method
def stopalarm():
    pg.mixer.music.stop()
    b.destroy()
    

# clock frame
c_frame=Frame(b,width=200,height=200)
c_frame.pack(pady=10,padx=10)

#clock
c = Label(c_frame,font=("Turret Road",50),text='',fg='blue',bg="black")
c.pack(pady=10,padx=10)

#calling clock()
clock()

#Alaram frame
a_frame=Frame(b,width=200,height=200)
a_frame.pack(pady=10,padx=10)

#Alarm setting gui
hrs=IntVar()
mins=IntVar()
ap=StringVar()
sel_music=StringVar()

# default set for AM/PM based on current time
ap.set(str(t.strftime('%p')))

#dummy Label to check the alarm logic in set alarm method
check=Label(b,text='')

# AM/PM 
am_pmset=['AM','PM']

# Hours
Label(a_frame,text='Hrs',fg='green',font=('sans-serif',20)).grid(row=0,column=0,padx=10,pady=10)
hour=Scale(a_frame,from_=1,to=12,bd=0,bg='black',font=('sans-serif',15),fg='white',variable=hrs)
hour.grid(row=1,column=0,padx=10,pady=10)
hour.config(bd=0)

# Minutes
Label(a_frame,text='Min',fg='green',font=('sans-serif',20)).grid(row=0,column=1,padx=10,pady=10)
minutes=Scale(a_frame,from_=0,to=59,bd=0,bg='black',fg='white',font=('sans-serif',15),variable=mins)
minutes.grid(row=1,column=1,padx=10,pady=10)
minutes.config(bd=0)

# AM or PM
Label(a_frame,text='AM/PM',fg='green',font=('sans-serif',20)).grid(row=0,column=2,padx=10,pady=10)
apm=OptionMenu(a_frame,ap,*am_pmset)
apm.grid(row=1,column=2,padx=10,pady=10)
apm.config(bg='black',fg='white',font=('sans-serif',20))
apm.config(bd=0)

#Alarm sounds
music=['alarm_clock','alarm_classic','alarm_alarm_alarm']
sel_music.set(str(music[0]))
m_list=OptionMenu(a_frame,sel_music,*music)
m_list.grid(row=2,column=1,padx=10,pady=10)
m_list.config(bg='black',fg='white',font=('sans-serif',20))
m_list.config(bd=0)

#Label for alarm set
lbl=Label(b,text='',bg='white',fg='green',font=('sans-serif',20))
lbl.pack(pady=10,padx=10)

#Alarm set button
aset=Button(a_frame,text='Set Alarm',bg='black',fg='white',bd=0,command=setalarm,font=('sans-serif',15))
aset.grid(row=3,column=1,padx=10,pady=10)
aset.config(bd=0)

#Alarm stop button
astop=Button(a_frame,text='Stop Alarm',bg='black',fg='white',bd=0,command=stopalarm,font=('sans-serif',15))
astop.grid(row=4,column=1,padx=10,pady=10)
astop.config(bd=0)

#Mainloop of GUI
b.mainloop()
