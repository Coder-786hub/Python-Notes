"""Tkinter buttons (GUI Programming)
Buttons are standard widgets in a GUI. They come with the default Tkinter module and you can place them in your window.

A Python function or method can be associated with a button. This function or method is named the callback function. If you click the button, the callback function is called.

A note on buttons: a tkinter button can only show text in a single font. The button text can be multi line. That means that this widget won’t show icons next to the text, for that you’d need another widget.
"""

# Example
# You can create and position a button with these lines:

# exitButton = Button(self, text="Exit", command=self.clickExitButton)
# exitButton.place(x=0, y=0)
# The callback method is clickExitButton, which is assigned in the above line (command=).
# This is a simple method:

# def clickExitButton(self):
#         exit()
# Without a callback method, a button is shown but clicking it won’t do anything.

# This window should show up: