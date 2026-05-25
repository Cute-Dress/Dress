# 导入所需的库
import mido
import time
import tkinter as tk
import tkinter.ttk as ttk

mid = mido.MidiFile("example.mid")

top = tk.Tk()
top.geometry("800x450+10+10")

v_note = ttk.Treeview(top)
v_note["columns"] = range(1,88)

for i in range(1,88):
    v_note.column(str(i),width=6)
    v_note.heading(str(i),text=str(i))

v_note.insert("",0,text="88k Piano",values=[i for i in range(1,88)])



v_note.pack(side="top")
top.update()
top.mainloop()



# for msg in mid:
#     time.sleep(msg.time)
#     if not msg.is_meta:
#         print(msg)

