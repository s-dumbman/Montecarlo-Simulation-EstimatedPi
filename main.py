import tkinter as tk
import random
from math import *
# 함수
def MonteDOT():
    total_points = scale.get()
    inside_circle = 0
    canvas.delete("all")
    for _ in range(total_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x ** 2 + y ** 2
        if distance <= 1:
            inside_circle += 1
            canvas.create_oval(x * 200, y * 200, x * 200 + 2, y * 200 + 2, fill="red")
        else:
            canvas.create_oval(x * 200, y * 200, x * 200 + 2, y * 200 + 2, fill="blue")
    estimated_pi = (inside_circle / total_points) * 4
    if estimated_pi > 0:
        if (pi / estimated_pi) * 100 > 100:
            esp = 100 - ((pi / estimated_pi) * 100 - 100)
        else:
            esp = (pi / estimated_pi) * 100
    else:
        esp = "undefined"
    result_label.config(text=f"π: {estimated_pi}")
    percentage_label.config(text=f"정확성: {esp}%")
# tkinter 설정
win = tk.Tk()
win.geometry("400x400")
win.title("몬테카를로 시뮬레이션")
canvas = tk.Canvas(win, width=200, height=200)
canvas.pack()
scale = tk.Scale(win, from_=100000, to=1, length=200, orient="horizontal")
scale.pack(pady=10)
btn = tk.Button(win, text="실행", command=MonteDOT)
btn.pack()
result_label = tk.Label(win, text="")
result_label.pack()
percentage_label = tk.Label(win, text="")
percentage_label.pack()
btn2 = tk.Button(win, text="닫기", command=win.quit)
btn2.pack(pady=10)
# win 실행
win.mainloop()
