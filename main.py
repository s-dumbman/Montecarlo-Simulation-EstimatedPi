import tkinter as tk
import random
from math import *
def MonteDOT():
    total_points = scale.get()
    inside_circle = 0

    for _ in range(total_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x ** 2 + y ** 2

        if distance <= 1:
            inside_circle += 1
    estimated_pi = (inside_circle / total_points) * 4
    result_label.config(text=f"π: {estimated_pi}")
win = tk.Tk()
win.geometry("300x200")
win.title("몬테카를로 시뮬레이션")
scale = tk.Scale(win, from_=pow(2,25), to=1, length=200, orient="horizontal")
scale.pack(pady=10)
btn = tk.Button(win, text="실행", command=MonteDOT)
btn.pack()
result_label = tk.Label(win, text="")
result_label.pack()
btn2 = tk.Button(win, text="닫기", command=win.quit)
btn2.pack(pady=10)
win.mainloop()
