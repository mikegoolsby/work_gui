import tkinter as tk
from datetime import date
import random

today = date.today()
reps = ["Ryan","Max","Julian","Ethan", "Nick", "Chris","Aaron","Connor","Joe"]

# Create a window object
window = tk.Tk()
window.title("ADSK TL")

time = tk.Label(
    text=f"Today's date is {today}",
    foreground="#fa8d3e",
    background="black",
    height=8,
    width=25
    )


def handle_click(event):
    random_rep = random.sample(reps, 1)
    print(random_rep)

button = tk.Button(
    text="Random rep",
    foreground="white",
    background="red",
    width=25)

button.bind("<Button-1>", handle_click)



time.pack()
button.pack()

# Run the event loop
window.mainloop()
