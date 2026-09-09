import random
from tkinter import PhotoImage, Tk, Toplevel, Label
import asyncio
import pygame
import os

def resource_path(relative_path):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)

async def jumpscare():
    global window
    window.deiconify()
    window.attributes("-fullscreen", True)

    await asyncio.gather(*[playGif(), playSound()])

    window.attributes("-fullscreen", False)
    window.withdraw()

async def playSound():
    pygame.mixer.init()
    pygame.mixer.music.load(resource_path("content/Xscream3.wav"))
    pygame.mixer.music.play()

async def playGif():
    for i in range(14):
        frame = frames[i]
        videoPlayer.config(image = frame)
        window.update()
        await asyncio.sleep(0.1)

def randomJumpscare():
    if random.randint(1, 10000) == 1:
        asyncio.run(jumpscare())

    root.after(500, randomJumpscare)

pygame.init()
root = Tk()

frames = [PhotoImage(file= resource_path("content/foxy-jump.gif") ,format = 'gif -index %i' %(i)) for i in range(14)]

window = Toplevel(root)
window.title("VideoPlayer")
window.withdraw()

videoPlayer = Label(window)
videoPlayer.pack()

root.update()

root.bind("<e>", lambda _: asyncio.run(jumpscare()))
root.after(500, randomJumpscare)
root.mainloop()