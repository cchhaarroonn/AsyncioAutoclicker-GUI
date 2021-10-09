from tkinter import *
import threading, pyglet, keyboard, pyautogui, pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)
rat = engine.getProperty("rate")
engine.setProperty("rate", 170)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

speak("Hello, welcome to Asyncio. Thank you for using our clicker. Application will start automatically after this message!")

def clicker():
    hotkey = entry0.get()
    while True:
        if keyboard.is_pressed(hotkey):
            pyautogui.doubleClick()

thread = threading.Thread(target=clicker)
thread.daemon = True 
thread.start

def stopclicker():
    exit()

window = Tk()
window.title('Asyncio')
window.geometry("363x409")
window.configure(bg = "#28313b")

window_height = 409
window_width = 363

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

canvas = Canvas(
    window,
    bg = "#28313b",
    height = 409,
    width = 363,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    181.5, 194.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#28313b",
    highlightthickness = 0)

entry0.place(
    x = 76, y = 184,
    width = 211,
    height = 19)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = thread.start,
    relief = "flat")

b0.place(
    x = 57, y = 285,
    width = 118,
    height = 52)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = stopclicker,
    relief = "flat")

b1.place(
    x = 189, y = 285,
    width = 118,
    height = 52)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    181.0, 202.5,
    image=background_img)

window.resizable(False, False)
window.mainloop()
