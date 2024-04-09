import tkinter as tk
import time
from datetime import datetime

timertxt = "A"
setcolor = "blue"
settxtclr = "black"
setfont = 'arial'
currentPage = ""
x= ""
y = ""
z = ""
cleanx = ""
cleany = ""
cleanz = ""
isint = True
ischecking = False


def changePage(root, pageName, timerpage, modifypage):
    global currentPage
    if pageName == "timerpage":
        modifypage.pack_forget()
        timerpage.pack(fill='both', expand=True)
        currentPage = "timerpage"
        textclr(root)


    elif pageName == "modifypage":
        timerpage.pack_forget()
        modifypage.pack(fill='both', expand=True)
        currentPage = "modifypage"
        textclr(root)

def getext(root):
    global isint, ischecking
    x = textbox1.get("1.0", tk.END)
    y = textbox3.get("1.0", tk.END)
    z = textbox5.get("1.0", tk.END)
    cleanx = x.strip()
    cleany = y.strip()
    cleanz = z.strip()
    try:
        int(cleanx)
        int(cleany)
        int(cleanz)
        isint = True
    except:
        isint = False

    if isint == True and int(cleanx) < 25 and int(cleany) < 61 and int(cleanz) < 61 and ischecking == False:
        isint = True
    else:
        isint = False

    if isint == True:
        curtime = str(cleanx) + str(cleany) + str(cleanz)
        print(curtime)
        textbox1.delete("1.0", tk.END)
        textbox3.delete("1.0", tk.END)
        textbox5.delete("1.0", tk.END)
        timenow(root, curtime)
    else:
        textbox1.delete("1.0", tk.END)
        textbox3.delete("1.0", tk.END)
        textbox5.delete("1.0", tk.END)
    
def timenow(root, time):
    global ischeking
    ischeking = True
    now = datetime.now()
    current_time = now.strftime("%H%M%S")
    print(current_time)
    while True:
        if current_time < time:
            now = datetime.now()
            current_time = now.strftime("%H%M%S")
            print(current_time)
            textbox1.delete("1.0", tk.END)
            textbox3.delete("1.0", tk.END)
            textbox5.delete("1.0", tk.END)
            continue
        elif current_time >= time:
            print("now")
            ischeking = False
            modifypage.pack_forget()
            timerpage.pack_forget()
            timenowpage.pack(fill="both", expand=True)
            break

def backnow(root, timing):
    if timing == True:
        timenowpage.pack_forget()
        timerpage.pack(fill="both", expand=True)
        timing = False
    else:
        print("Timing error")


def textclr(root):
    textbox1.delete("1.0", tk.END)
    textbox3.delete("1.0", tk.END)
    textbox5.delete("1.0", tk.END)

def changeColor(root, colortype, modifypage, timerpage, BgColor, TXTColor, Fonts, textbox2, textbox4):
    global setcolor, settxtclr, setfont
    modifypage.pack_forget()
    if colortype == "bg1":
        setcolor = "blue"
    elif colortype == "bg2":
        setcolor = "green"
    elif colortype == "bg3":
        setcolor = "red"
    elif colortype == "bg4":
        setcolor = "black"
    elif colortype == "txt1":
        settxtclr = "blue"
    elif colortype == "txt2":
        settxtclr = "green"
    elif colortype == "txt3":
        settxtclr = "red"
    elif colortype == "txt4":
        settxtclr = "black"
    elif colortype == "f1":
        setfont = 'arial'
    elif colortype == "f2":
        setfont = 'times new roman'
    elif colortype == "f3":
        setfont = 'impact'
    elif colortype == "f4":
        setfont = 'webdings'
    modifypage.pack(fill='both', expand=True)
    root.configure(bg=setcolor)
    modifypage.configure(bg=setcolor)
    timerpage.configure(bg=setcolor)
    timenowpage.configure(bg=setcolor)
    BgColor.configure(bg=setcolor, font=(setfont, 15, 'bold'), fg=settxtclr)
    TXTColor.configure(bg=setcolor, font=(setfont, 15, 'bold'), fg=settxtclr)
    Fonts.configure(bg=setcolor, font=(setfont, 15, 'bold'), fg=settxtclr)
    textbox1.configure(font=(setfont, 100, 'bold'), fg=settxtclr)
    textbox2.configure(bg=setcolor, font=(setfont, 100, 'bold'), fg=settxtclr)
    textbox3.configure(font=(setfont, 100, 'bold'), fg=settxtclr)
    textbox4.configure(bg=setcolor, font=(setfont, 100, 'bold'), fg=settxtclr)
    textbox5.configure(font=(setfont, 100, 'bold'), fg=settxtclr)
    label.configure(bg=setcolor, font=(setfont, 22, 'bold'), fg=settxtclr)
    label2.configure(bg=setcolor, font=(setfont, 80, 'bold'), fg=settxtclr)
    timerpagebtn.configure(font=(setfont, 18), fg=settxtclr)
    timerbtn.configure(font=(setfont, 18), fg=settxtclr)
    modifybtn.configure(font=(setfont, 18), fg=settxtclr)
    timerpagebtn.configure(font=(setfont, 18), fg=settxtclr)
    backbtn.configure(font=(setfont, 18), fg=settxtclr)
    txt1.configure(font=(setfont, 18))
    txt2.configure(font=(setfont, 18))
    txt3.configure(font=(setfont, 18))
    txt4.configure(font=(setfont, 18))
    f1.configure(fg=settxtclr)
    f2.configure(fg=settxtclr)
    f3.configure(fg=settxtclr)
    f4.configure(fg=settxtclr)
    




root = tk.Tk()
timerpage = tk.Frame()
modifypage = tk.Frame()
timenowpage = tk.Frame()

root.geometry("1200x620")
root.title("Custom Time Manager")
root.configure(bg=setcolor)



label = tk.Label(root, text="CTM", font=(setfont, 22, 'bold'), bg=setcolor)
label.pack(padx=20, pady=20)




timerpage = tk.Frame(root)
timerpage.columnconfigure(0, weight=1)
timerpage.columnconfigure(1, weight=1)
timerpage.columnconfigure(2, weight=1)
timerpage.columnconfigure(3, weight=1)
timerpage.columnconfigure(4, weight=1)
timerpage.rowconfigure(0, weight=1)
timerpage.rowconfigure(1, weight=1)
timerpage.configure(bg=setcolor)

modifypage = tk.Frame(root)
modifypage.columnconfigure(0, weight=1)
modifypage.columnconfigure(1, weight=1)
modifypage.columnconfigure(2, weight=1)
modifypage.rowconfigure(0, weight=1)
modifypage.rowconfigure(1, weight=1)
modifypage.rowconfigure(2, weight=1)
modifypage.rowconfigure(3, weight=1)
modifypage.rowconfigure(4, weight=1)
modifypage.rowconfigure(5, weight=1)
modifypage.configure(bg=setcolor)


timenowpage = tk.Frame(root)
timenowpage.columnconfigure(0, weight=1)
timenowpage.rowconfigure(0, weight=1)
timenowpage.rowconfigure(1, weight=1)
timenowpage.rowconfigure(2, weight=1)
timenowpage.configure(bg=setcolor)


label2 = tk.Label(timenowpage, text="It is time", font=(setfont, 80, 'bold'), bg=setcolor)
label2.grid(row=0, column=0)

backbtn = tk.Button(timenowpage, text="Back", command=lambda : backnow (root, True), font=(setfont, 18))
backbtn.grid(row=2, column=0, sticky=tk.W+tk.E)



modifybtn = tk.Button(timerpage, text="Modify", command=lambda : changePage (root,"modifypage", timerpage, modifypage), font=(setfont, 18))
modifybtn.grid(row=1, column=4, sticky=tk.W+tk.E)

timerbtn = tk.Button(timerpage, text="SetTimer", command=lambda : getext (root), font=(setfont, 18))
timerbtn.grid(row=1, column=0, sticky=tk.W+tk.E)



timerpagebtn = tk.Button(modifypage, text="Timer", command=lambda : changePage (root,"timerpage", timerpage, modifypage), font=(setfont, 18))
timerpagebtn.grid(row=5, column=1, sticky=tk.W+tk.E)

BgColor = tk.Text(modifypage, height=1, width=8, font=(setfont, 15, 'bold'), bg=setcolor, fg=settxtclr)
BgColor.grid(row=0, column=0)
BgColor.insert(tk.END, "Bg Color")
BgColor.config(state='disabled')

TXTColor = tk.Text(modifypage, height=1, width=9, font=(setfont, 15, 'bold'), bg=setcolor, fg=settxtclr)
TXTColor.grid(row=0, column=1)
TXTColor.insert(tk.END, "TXT Color")
TXTColor.config(state='disabled')

Fonts = tk.Text(modifypage, height=1, width=4, font=(setfont, 15, 'bold'), bg=setcolor, fg=settxtclr)
Fonts.grid(row=0, column=2)
Fonts.insert(tk.END, "Font")
Fonts.config(state='disabled')

bg1 = tk.Button(modifypage, text="", command=lambda : changeColor (root,"bg1", modifypage, timerpage, BgColor, TXTColor, Fonts, textbox2, textbox4), font=(setfont, 18), bg="blue")
bg1.grid(row=1, column=0, sticky=tk.W+tk.E)

bg2 = tk.Button(modifypage, text="", command=lambda : changeColor (root,"bg2", modifypage, timerpage, BgColor, TXTColor, Fonts, textbox2, textbox4), font=(setfont, 18), bg="green")
bg2.grid(row=2, column=0, sticky=tk.W+tk.E)

bg3 = tk.Button(modifypage, text="", command=lambda : changeColor (root,"bg3", modifypage, timerpage, BgColor, TXTColor, Fonts, textbox2, textbox4), font=(setfont, 18), bg="red")
bg3.grid(row=3, column=0, sticky=tk.W+tk.E)

bg4 = tk.Button(modifypage, text="", command=lambda : changeColor (root,"bg4", modifypage, timerpage, BgColor, TXTColor, Fonts, textbox2, textbox4), font=(setfont, 18), bg="black")
bg4.grid(row=4, column=0, sticky=tk.W+tk.E)



txt1 = tk.Button(modifypage, text="Example", command=lambda : changeColor (root,"txt1", modifypage, timerpage, BgColor, TXTColor, Fonts, textbox2, textbox4), font=(setfont, 18), fg="blue")
txt1.grid(row=1, column=1, sticky=tk.W+tk.E)

txt2 = tk.Button(modifypage, text="Example", command=lambda : changeColor (root,"txt2", modifypage, timerpage, BgColor, TXTColor, Fonts, textbox2, textbox4), font=(setfont, 18), fg="green")
txt2.grid(row=2, column=1, sticky=tk.W+tk.E)

txt3 = tk.Button(modifypage, text="Example", command=lambda : changeColor (root,"txt3", modifypage, timerpage, BgColor, TXTColor, Fonts, textbox2, textbox4), font=(setfont, 18), fg="red")
txt3.grid(row=3, column=1, sticky=tk.W+tk.E)

txt4 = tk.Button(modifypage, text="Example", command=lambda : changeColor (root,"txt4", modifypage, timerpage, BgColor, TXTColor, Fonts, textbox2, textbox4), font=(setfont, 18), fg="black")
txt4.grid(row=4, column=1, sticky=tk.W+tk.E)


f1 = tk.Button(modifypage, text="Arial", command=lambda : changeColor (root,"f1", modifypage, timerpage, BgColor, TXTColor, Fonts, textbox2, textbox4), font=('arial', 18))
f1.grid(row=1, column=2, sticky=tk.W+tk.E)

f2 = tk.Button(modifypage, text="Times New Roman", command=lambda : changeColor (root,"f2", modifypage, timerpage, BgColor, TXTColor, Fonts, textbox2, textbox4), font=('times new roman', 18))
f2.grid(row=2, column=2, sticky=tk.W+tk.E)

f3 = tk.Button(modifypage, text="Impact", command=lambda : changeColor (root,"f3", modifypage, timerpage, BgColor, TXTColor, Fonts, textbox2, textbox4), font=('impact', 16))
f3.grid(row=3, column=2, sticky=tk.W+tk.E)

f4 = tk.Button(modifypage, text="Webdings", command=lambda : changeColor (root,"f4", modifypage, timerpage, BgColor, TXTColor, Fonts, textbox2, textbox4), font=('webdings', 18))
f4.grid(row=4, column=2, sticky=tk.W+tk.E)






textbox1 = tk.Text(timerpage, height=1, width=2, font=(setfont, 100, 'bold'), fg=settxtclr)
textbox1.grid(row=0, column=0)
textbox1.config(state='normal')

textbox2 = tk.Text(timerpage, height=1, width=1, font=(setfont, 100, 'bold'), bg=setcolor, fg=settxtclr)
textbox2.grid(row=0, column=1)
textbox2.insert(tk.END, ":")
textbox2.config(state='disabled')

textbox3 = tk.Text(timerpage, height=1, width=2, font=(setfont, 100, 'bold'), fg=settxtclr)
textbox3.grid(row=0, column=2)
textbox3.config(state='normal')

textbox4 = tk.Text(timerpage, height=1, width=1, font=(setfont, 100, 'bold'), bg=setcolor, fg=settxtclr)
textbox4.grid(row=0, column=3)
textbox4.insert(tk.END, ":")
textbox4.config(state='disabled')

textbox5 = tk.Text(timerpage, height=1, width=2, font=(setfont, 100, 'bold'), fg=settxtclr)
textbox5.grid(row=0, column=4)
textbox5.config(state='normal')

timerpage.pack(fill="both", expand=True)

root.mainloop()