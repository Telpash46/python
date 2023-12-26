import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.geometry("600x600")
WinTitle = "GUI-001"
root.title(WinTitle)

def change_title_sc1():
    global WinTitle
    if WinTitle == "GUI-001":
        WinTitle = "Title 2!"
        root.title(WinTitle)
        btn.config(text="Press me again (screen 1)", bg="green", fg="yellow")
    else:
        WinTitle = "GUI-001"
        root.title(WinTitle)
        btn.config(text="Press me (screen 1)", bg="yellow", fg="green")



def go_sc_2():
    global WinTitle
    btn.place_forget()
    btn2.place_forget()
    dialog_btn = tkinter.Button(root, text="Show dialog", command=lambda: messagebox.showinfo("Dialog", "- Hello! What is your name?\n\n- Hello. My name is Button, and you?\n\n- My name is Agent-007, nice to meet you!\n\n- Nice to meet you too!\n\n- Where we are?\n\n- We are in the Tkinter window!\n\n- OK, goodbye!\n\n- Goodbye!"), bg='orange', fg='green', width=20, height=10)
    dialog_btn.place(relx=0.1, rely=0.5) 


def quit_from_win():
    global WinTitle
    close = messagebox.askyesno(WinTitle, "Do you really want to exit?")
    if close:
        root.destroy()
btn = tkinter.Button(root, text="Press me (screen 1)", command=change_title_sc1, bg="yellow", fg="green", width=30, height=10)
btn.place(relx=0.5, rely=0.1)


btn2 = tkinter.Button(root, text="Go to screen 2 ►►►", command=go_sc_2, bg="red", fg="yellow", width=30, height=10)
btn2.place(relx=0.5, rely=0.5)

root.protocol("WM_DELETE_WINDOW", quit_from_win)
root.mainloop()