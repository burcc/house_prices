from tkinter import * 
import tkinter as tk
from PIL.ImageTk import PhotoImage

root = Tk()
root.geometry("800x600")
root.title("Home Prices")

def Amsterdam():
    if room.get().isdigit() and bath.get().isdigit:
        price = 70000
        eachRoom = 20000
        eachBathroom = 10000
        numofRoom = int(room.get())
        numofBath = int(bath.get())
        price = (50000 + (numofRoom*eachRoom) + (numofBath * eachBathroom))
        result.configure(text=str((f"Total amount of the house in \n Amsterdam that you have chosen for is: {price} $")), font= "Courier 8 bold")

def Paris():
    if room.get().isdigit() and bath.get().isdigit:
        price = 90000
        eachRoom = 25000
        eachBathroom = 15000
        numofRoom = int(room.get())
        numofBath = int(bath.get())
        price = (50000 + (numofRoom*eachRoom) + (numofBath * eachBathroom))
        result.configure(text=str((f"Total amount of the house in \n Paris that you have chosen for is: {price} $")), font= "Courier 8 bold")

def newYork():
    if room.get().isdigit() and bath.get().isdigit:
        price = 120000
        eachRoom = 30000
        eachBathroom = 15000
        numofRoom = int(room.get())
        numofBath = int(bath.get())
        price = (50000 + (numofRoom*eachRoom) + (numofBath * eachBathroom))
        result.configure(text=str((f"Total amount of the house in \n New York that you have chosen for is: {price} $")), font= "Courier 8 bold")

result = tk.Label(root, text= "After you specify that how many room and bath you want \nyou can click on that which city you want to buy a house in order to find out what price is.", font= "Courier 10 bold", width= 100, justify = "center")
result.place(x=20, y = 20 )

room = tk.Entry(root, font = "courier 14 bold", width =15, justify="center")
room.place (x=330, y=70)

bath = tk.Entry(root, font = "courier 14 bold", width =15, justify="center")
bath.place (x=330, y=100)

img = PhotoImage(file = "amsterdam.jpg")
button1 = Button(root, text = "Amsterdam", command = Amsterdam, compound= TOP, image= img)
button1.place(relx = 0.1, rely = 0.3, width = 200, height = 180)
img1 = PhotoImage(file = "paris.jpg")
button2 = Button(root, text = "Paris", command = Paris, compound= TOP, image= img1)
button2.place(relx= 0.4, rely = 0.3, width = 200, height = 180 )
img2 = PhotoImage(file = "newYork.jpg")
button3 = Button(root, text = "New York", command = newYork, compound= TOP, image= img2)
button3.place(relx= 0.7, rely = 0.3, width = 200, height = 180)




root.mainloop()