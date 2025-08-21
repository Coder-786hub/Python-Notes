from tkinter import *
import os
import time
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
from mutagen.mp3 import MP3
from PIL import Image, ImageTk



# Initialize mixer
mixer.init()

# Initialize Tkinter root
root = Tk()
root.title('Music_Player')
root.geometry('700x400')
root.resizable(0, 0)
root.configure(background='white')

img = Image.open("music1.jpg")
img = img.resize((700,400))
img = ImageTk.PhotoImage(img)

bg = Label(root, image = img)
bg.place(x = 0, y = 0)

# Variables
filename = ""
paused = False

# Open File function
def Openfile():
    global filename
    filename = filedialog.askopenfilename()

# About Message function
def About():
    tkinter.messagebox.showinfo('About Us', 'Music Player Created By Aftab Alam')

# Song Info function
def songinf():
    if filename:
        filelabel['text'] = 'Current Music: ' + os.path.basename(filename)

# Length bar function
def length_bar():
    if mixer.music.get_busy():
        current_time = mixer.music.get_pos() / 1000
        convert_current_time = time.strftime('%M:%S', time.gmtime(current_time))

        song_mut = MP3(filename)
        song_mut_length = song_mut.info.length
        convert_song_mut_length = time.strftime('%M:%S', time.gmtime(song_mut_length))

        lengthbar.config(text=f'Total Length: {convert_current_time}/{convert_song_mut_length}')
        lengthbar.after(1000, length_bar)

# Play Music function
def playmusic():
    global paused
    try:
        if paused:
            mixer.music.unpause()
            label1['text'] = 'Music Playing..'
        else:
            mixer.music.load(filename)
            mixer.music.play()
            label1['text'] = 'Music Playing..'
            songinf()
            length_bar()
    except Exception as e:
        tkinter.messagebox.showerror('Error', 'File not found. Please try again.')

# Pause Music function
def pausemusic():
    global paused
    paused = True
    mixer.music.pause()
    label1['text'] = 'Music Paused'

# Stop Music function
def stopmusic():
    mixer.music.stop()
    label1['text'] = 'Music Stopped'

# Mute function
def mute():
    scale.set(0)
    mute_button.config(text="Unmute", command=unmute)
    label1['text'] = 'Music Muted'

# Unmute function
def unmute():
    scale.set(30)
    mute_button.config(text="Mute", command=mute)
    label1['text'] = 'Music Playing'

# Volume control function
def volume_(vol):
    volume = int(vol) / 100
    mixer.music.set_volume(volume)

# Menu Bar
menubar = Menu(root)
root.configure(menu=menubar)

submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=submenu)
submenu.add_command(label='Open', command=Openfile)
submenu.add_command(label='Exit', command=root.destroy)

submenu2 = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=submenu2)
submenu2.add_command(label='About', command=About)

# Labels
filelabel = Label(text='Select And Play', bg='black', fg='white', font=22)
filelabel.place(x=5, y=30)

lengthbar = Label(root, text='Total Length: 00:00', font=20, bg='black', fg='white')
lengthbar.place(x=5, y=270)

label1 = Label(root, text='Let’s Play It.', bg='black', fg='white', font=20)
label1.pack(side=BOTTOM, fill=X)



# Buttons
play_img = Image.open("play.jpg")
play_img = play_img.resize((30, 30))
play_img = ImageTk.PhotoImage(play_img)
Button(root, image = play_img, bd=0, bg='white', command=playmusic).place(x=5, y=300)


pause_img = Image.open("pause.png")
pause_img = pause_img.resize((30, 30))
pause_img = ImageTk.PhotoImage(pause_img)
Button(root, image = pause_img, bd=0, bg='white', command=pausemusic).place(x=85, y=300)

stop_img = Image.open("stop.png")
stop_img = stop_img.resize((30, 30))
stop_img = ImageTk.PhotoImage(stop_img)
Button(root, image = stop_img, bd=0, bg='white', command=stopmusic).place(x=165, y=300)

mute_img = Image.open("mute.png")
mute_img = mute_img.resize((30, 30))
mute_img = ImageTk.PhotoImage(mute_img)
mute_button = Button(root, image = mute_img, command=mute, bg='white', bd=0)
mute_button.place(x=280, y=300)

# Volume Bar
scale = Scale(root, from_=0, to=100, bg='cyan', orient=HORIZONTAL, length=120, command=volume_)
scale.set(30)
scale.place(x=330, y=290)


cd_image = Image.open("cd1.jpg")
cd_image = cd_image.resize((200, 150))
cd_image = ImageTk.PhotoImage(cd_image)
cd_label = Label(root, image = cd_image)
cd_label.place(x = 20, y = 90)


# Run the application
root.mainloop()
