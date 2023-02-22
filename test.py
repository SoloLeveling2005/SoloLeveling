# import tkinter as tk
#
# # Create the main window
# root = tk.Tk()
#
# # Create two frames
# frame1 = tk.Frame(root)
# frame2 = tk.Frame(root)
#
# # Add the frames to the window
# frame1.pack(side="left")
# frame2.pack(side="right")
#
# # Add widgets to each frame
# tk.Label(frame1, text="Page 1").pack()
# tk.Label(frame2, text="Page 2").pack()
#
# # Run the main loop
# root.mainloop()


# # Import tkinter and webview libraries
# from tkinter import *
# import webview
#
# # define an instance of tkinter
# tk = Tk()
#
#
# #  size of the window where we show our website
# tk.geometry("800x450")
#
from flask import Flask
import webview

server = Flask(__name__, static_folder='./assets', template_folder='./templates')
webview.create_window('Flask example', server)
webview.start()