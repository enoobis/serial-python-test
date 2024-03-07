import serial
from serial import Serial
import tkinter as tk
from tkinter import ttk
import requests
import api_request
from PIL import Image, ImageTk
from io import BytesIO

################
"""FUNCTIONS"""
################

# balance
def update_balance():
    balance = api_request.fetch_balance()
    balance_label.config(text=f"Текущий баланс: {balance}")
    root.after(5000, update_balance)

def deduct_balance():
    current_balance = api_request.fetch_balance()
    updated_balance = max(0, current_balance - 20) 
    balance_label.config(text=f"Текущий баланс: {updated_balance}")

def turn_on_led():
    ser.write("turn_on_led\n".encode())

def turn_off_led():
    ser.write("turn_off_led\n".encode())

# image qr code
def display_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()

#########
"""APP"""
#########

# arduino 
ser = serial.Serial('COM7', 9600)
root = tk.Tk()
root.title("app")

# buttons
button_on = tk.Button(root, text="Вычесть 20", command=turn_on_led, )
button_on.pack()

deduct_button = ttk.Button(root, text="Вычесть 20", command=deduct_balance)
deduct_button.pack(pady=5)

button_off = tk.Button(root, text="Turn Off LED", command=turn_off_led)
button_off.pack()

# qr image
image_url = "https://test4-mwallet.dengi.kg/qr.php?wl=nur&type=emvQr&data=00020101021132490011qr.dengi.kg0102201112938714053163120211130212520473995303417540105917test%20Etno%20Tattuu%206304AD43"
display_image(image_url)

#balance
balance_label = ttk.Label(root, text="Текущий баланс: 0")
balance_label.pack(pady=10)


#End
update_balance()
root.mainloop()
ser.close()
