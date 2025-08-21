# Reading Images with Tkinter
# Images can be shown with tkinter. Images can be in a variety of formats including jpeg images. A bit counterintuitive, but you can use a label to show an image.

# To open an image use the method Image.open(filename). This will look for images in the programs directory, for other directories add the path to the filename.



"""Example
introduction
This example loads and shows an image on a label. It’s as simple as showing text on the tkinter window, but instead of text we show an image.

You should install the Python Imaging Library (PIL) to load images. This is required and the module is available in PyPi. Install that module with the pip package manager.

It can open various image formats including PPM, PNG, JPEG, GIF, TIFF, and BMP.

To load an image:

load = Image.open("parrot.jpg")
render = ImageTk.PhotoImage(load)
Then associate it with the label:

img = Label(image=render)
img.image = render
img.place(x=0, y=0)"""