import tkinter as tk

root=tk.Tk()
root.title("Thông điệp gửi vợ")
root.geometry("720x1280")
root.configure(bg="black")

groups=[
["I love you","Vợ của anh nha","Hồng Phương","Nay là ngày đầu tiên"],
["Bước qua tháng 8","Chúc vợ may mắn","Trong tháng này nha! ❤","Yêu em nhiều lắm! 💕"]
]

labels=[]
for i in range(4):
    lbl=tk.Label(root,text="",fg="white",bg="black",font=("Arial",24))
    lbl.place(relx=0.5,y=350+i*60,anchor="center")
    labels.append(lbl)

idx=0
y=350

def show():
    global idx,y
    y=350
    for i,t in enumerate(groups[idx]):
        labels[i].config(text=t,fg="white")
        labels[i].place_configure(y=y+i*60)
    root.after(2000,animate)

def animate():
    global idx,y
    y+=8
    done=y>700
    fade=max(0,int(255-(y-350)*0.8))
    color=f"#{fade:02x}{fade:02x}{fade:02x}"
    for i,l in enumerate(labels):
        l.config(fg=color)
        l.place_configure(y=y+i*60)
    if not done:
        root.after(30,animate)
    else:
        idx=(idx+1)%2
        show()

show()
root.mainloop()
