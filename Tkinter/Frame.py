# # # tkinter frame
# # # A frame in Tk lets you organize and group widgets. It works like a container. Its a rectangular area in which widges can be placed.

# # # If you make a GUI app, you’ll be using different widgets. Those widgets need to be organized somehow, that’s where a frame comes in.

# # # Related course: Python Desktop Apps with Tkinter

# # # tkinter frame button
# # # The tkinter program below demonstrates the use of a frame. It includes a button with a callback function. A frame can have padding.

# # from tkinter import *

# # def say_hi():
# #     print("hello ~ !")

# # root = Tk()
# # root.geometry("500x400")
# # frame1 = Frame(root)
# # frame2 = Frame(root)
# # root.title("tkinter frame")

# # label= Label(frame1,text="Label",justify=LEFT)
# # label.pack(side=LEFT)

# # label= Label(frame1,text="Label")
# # label.pack()

# # hi_there = Button(frame2,text="say hi~",command=say_hi)
# # hi_there.pack()

# # hi_there = Button(frame2,text="say hi~",command=say_hi)
# # hi_there.pack()

# # frame1.pack(padx=1,pady=1)
# # frame2.pack(padx=10,pady=10)

# # root.mainloop()
# # # tkinter frame button

# # # tkinter frame photo
# # # Different types of widgets can be added. The example has a tkinter frame photo. It also has a label. You can add any kind of widget to your frame.

# # # from tkinter import *

# # # root = Tk()

# # # textLabel = Label(root,
# # #                   text="Label",
# # #                   justify=LEFT,
# # #                   padx=10)
# # # textLabel.pack(side=LEFT)

# # # photo = PhotoImage(file="cat.png")
# # # imgLabel = Label(root, image=photo)
# # # imgLabel.pack(side=RIGHT)

# # # mainloop()
# # # tkinter frame photo

# # # tkinter frame
# # # The tkinter program below adds sevearl frames of a different color. They all have the same width and height. In other words, you can change the style of the frame.

# # # from tkinter import *  
# # # root = Tk()  

# # # for fm in ['blue','red','yellow','green','white','black']:  
# # #     Frame(height = 20,width = 640,bg = fm).pack()  
# # # root.mainloop() 



# from tkinter import *

# app = Tk()
# app.geometry("800x600")

# frame = Frame(app, width = 400, height = 400, bg = "green")
# frame.place(x = 100, y = 50, width = 400, height = 400)

# lbl1 = Label(frame, text = "Label")
# # lbl1.place(x = 10, y = 10)
# lbl1.grid(row = 0, column = 0)


# lbl1 = Label(frame, text = "Label2")
# # lbl1.place(x = 10, y = 50)
# lbl1.grid(row = 1, column = 0)

# lbl1 = Label(frame, text = "Label3")
# # lbl1.place(x = 10, y = 100)
# lbl1.grid(row = 2, column = 0)

# lbl1 = Label(frame, text = "Label4")
# # lbl1.place(x = 10, y = 150)
# lbl1.grid(row = 3, column = 0)

# lbl1 = Label(frame, text = "Label")
# # lbl1.place(x = 10, y = 10)
# lbl1.grid(row = 0, column = 3, padx = 20, pady = 20)


# lbl1 = Label(frame, text = "Label2")
# # lbl1.place(x = 10, y = 50)
# lbl1.grid(row = 1, column = 3, padx = 20, pady = 20)

# lbl1 = Label(frame, text = "Label3")
# # lbl1.place(x = 10, y = 100)
# lbl1.grid(row = 2, column = 3, padx = 20, pady = 20)

# lbl1 = Label(frame, text = "Label4")
# # lbl1.place(x = 10, y = 150)
# lbl1.grid(row = 3, column = 3, padx = 20, pady = 20)

# app.mainloop()

