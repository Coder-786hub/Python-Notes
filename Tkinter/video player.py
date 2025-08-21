from tkinter import *
from tkinter import filedialog, messagebox
from tkvideo import tkvideo
import threading
from moviepy import VideoFileClip

# Initialize Tkinter root
root = Tk()
root.title('Video Player')
root.geometry('700x400')
root.resizable(0, 0)
root.configure(background='white')

# Variables
video_path = ""
player = None
paused = False

# Functions
def open_file():
    global video_path, player
    video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov;*.mkv")])
    if video_path:
        stop_video()  # Stop any currently playing video
        player = tkvideo(video_path, video_label, loop=1, size=(700, 300))
        play_video()

def play_video():
    global player, paused
    if player:
        if paused:
            paused = False
            label_status.config(text="Video Playing...")
        else:
            player.play()
            threading.Thread(target=play_audio, daemon=True).start()
            label_status.config(text="Video Playing...")

def play_audio():
    try:
        clip = VideoFileClip(video_path)
        clip.audio.preview()  # Plays the audio
    except Exception as e:
        messagebox.showerror("Error", f"Unable to play audio: {e}")

def pause_video():
    global paused
    paused = True
    label_status.config(text="Pause not supported in this implementation.")
    # Pause functionality can be implemented with other advanced libraries.

def stop_video():
    global player
    if player:
        video_label.config(image="")
        player = None
        label_status.config(text="Video Stopped")

def about():
    messagebox.showinfo("About", "Video Player Created by YourName")

# UI Components
menu_bar = Menu(root)
root.configure(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Exit", command=root.destroy)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

video_label = Label(root, bg="black")
video_label.place(x=0, y=0, width=700, height=300)

label_status = Label(root, text="Select a Video to Play", bg="black", fg="white", font=("Arial", 12))
label_status.pack(side=BOTTOM, fill=X)

control_frame = Frame(root, bg="white")
control_frame.pack(side=BOTTOM, pady=10)

Button(control_frame, text="Play", bd=0, bg="white", command=play_video, font=("Arial", 10)).pack(side=LEFT, padx=10)
Button(control_frame, text="Pause", bd=0, bg="white", command=pause_video, font=("Arial", 10)).pack(side=LEFT, padx=10)
Button(control_frame, text="Stop", bd=0, bg="white", command=stop_video, font=("Arial", 10)).pack(side=LEFT, padx=10)

# Run Application
root.mainloop()
