from customtkinter import *

window = CTk()

result = CTkEntry(window, height=30)
result.pack(fill="x")

frame = CTkFrame(window)
frame.pack()


button_1 = CTkButton(frame, text="1")
button_1.grid(row=0,column=0)

button_2 = CTkButton(frame, text="2")
button_2.grid(row=0,column=1)

button_3 = CTkButton(frame, text="3")
button_3.grid(row=0,column=2)

button_4 = CTkButton(frame, text="/")
button_4.grid(row=0,column=3)

button_5 = CTkButton(frame, text="4")
button_5.grid(row=1,column=0)

button_6 = CTkButton(frame, text="5")
button_6.grid(row=1,column=1)

button_0 = CTkButton(frame, text="6")
button_0.grid(row=1,column=2)

button_7 = CTkButton(frame, text="*")
button_7.grid(row=1,column=3)

button_8 = CTkButton(frame, text="7")
button_8.grid(row=2,column=0)

button_9 = CTkButton(frame, text="8")
button_9.grid(row=2,column=1)

button_10 = CTkButton(frame, text="9")
button_10.grid(row=2,column=2)

button_10 = CTkButton(frame, text="-")
button_10.grid(row=2,column=3)

button_11 = CTkButton(frame, text=".")
button_11.grid(row=3,column=0)

button_12 = CTkButton(frame, text="0")
button_12.grid(row=3,column=1)

button_13 = CTkButton(frame, text=",")
button_13.grid(row=3,column=2)

button_13 = CTkButton(frame, text="+")
button_13.grid(row=3,column=3)


window.mainloop()
