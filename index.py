from tkinter import *

root = Tk()
root.title('my game')
root.geometry("400x200") 

#menu
def back():
    but_texte.pack()
    but_bin.pack()
    lab_tex.pack_forget()
    ent_tex.pack_forget()
    button_tex.pack_forget()
    lab_bin.pack_forget()
    ent_bin.pack_forget()
    button_bin.pack_forget()

menu = Button(root, text='MENU', command=back)
menu.pack(anchor=NW, padx=10, pady=10)

def hide_but_tex():
    but_texte.pack_forget()
    but_bin.pack_forget()
    lab_tex.pack(pady=10)
    ent_tex.pack(pady=5)
    button_tex.pack(pady=5)

def hide_but_bin():
    but_texte.pack_forget()
    but_bin.pack_forget()
    lab_bin.pack(pady=10)
    ent_bin.pack(pady=5)
    button_bin.pack(pady=5)

# choose a method
but_bin = Button(root, text="binary > text", command=hide_but_bin)
but_bin.pack(anchor=N)

but_texte = Button(root, text="text > binary", command=hide_but_tex)
but_texte.pack(anchor=N)

# text > bianry
binary = ''
textb = ''

def show_text():
    global textb
    global binary
    textb = ent_tex.get()
    binary = ' '.join([format(ord(c), '08b') for c in textb])
    lab_tex.config(text=f'your code: {binary}')

ent_tex = Entry(font=(15))
lab_tex = Label(root, text='your code: .....', font=('Arial', 20))
button_tex = Button(root, text="Submit", command=show_text, font=(20))

# binary > text
code_text = ''
text = ''

def show_bin():
    global text
    global code_text
    code_text = ent_bin.get()
    text = ''.join([chr(int(b, 2)) for b in code_text.split()])
    lab_bin.config(text=f'your text: {text}')

ent_bin = Entry(font=(15))
lab_bin = Label(root, text='your text: .....', font=('Arial', 20))
button_bin = Button(root, text="Submit", command=show_bin, font=(20))

root.mainloop()
