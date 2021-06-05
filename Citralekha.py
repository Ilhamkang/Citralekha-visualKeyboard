# version 1.0 (Beta)
# GNU GENERAL PUBLIC LICENSE 3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
# This keyboard is expanded from Ganeshkavhar's project (https://github.com/ganeshkavhar/On-Screen-Keyboard-Python-Project)

import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import tkinter.messagebox
from tkinter.font import Font
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import ttk
 
root = Tk()
root.title("Citralekha 1.0 (Beta)")
root.resizable(0,0)
file_path = ''
tabControl = ttk.Notebook(root)

global selected
selected = False


# Pengaturan font
text_font = Font(
    family="Helvetica",
    size=14)


# fungsi tombol
 
def select(value):
    if value=="⌫":
        txt = TextArea.get(1.0,END)
        val = len(txt)
        TextArea.delete(1.0, END)
        TextArea.insert(1.0,txt[:val-2])    
    elif value == "⏎":
        TextArea.insert(INSERT,"\n")
    elif value=="Spasi":
        TextArea.insert(INSERT," ")
    elif value == "Tab":
        TextArea.insert(INSERT,"   ")
    else:
        TextArea.insert(INSERT,value)


# kotakdialog
def about():
    tkinter.messagebox.showinfo("Tentang","Citralekha 1.0 (Beta) dikembangkan oleh Ilham Nurwansah untuk membantu pengetikan huruf Latin dengan diakritik dalam proses transliterasi naskah-naskah Nusantara. \n ilhamnurwansah@gmail.com")

# fungsi menu 'berkas'
def set_file_path(path):
    global file_path
    file_path = path
  
def open_file():
    path = askopenfilename(filetypes=[('Berkas Teks', '*.txt')])
    with open(path, 'r') as file:
        code = file.read()
        TextArea.delete('1.0', END)
        TextArea.insert('1.0', code)
        set_file_path(path)
        
def save_as():
    path = asksaveasfilename(filetypes=[('Berkas Teks', '*.txt')])
    with open(path, 'w') as file:
        code = text_box.get('1.0', END) 
        file.write(code)
        set_file_path(path)

def save_file():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Berkas Teks', '*.txt')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = text_box.get('1.0', END) 
        file.write(code)
        set_file_path(path)
        
## Fungsi edit_bar
        
def cut_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if TextArea.selection_get():
            selected = TextArea.selection_get()
            TextArea.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)

def copy_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
        
    if TextArea.selection_get():
        selected = TextArea.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)
        
def paste_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = TextArea.index(INSERT)
            TextArea.insert(position, selected)

def clear_text():
    TextArea.delete('1.0', END)

def select_all_text(event=None):
    TextArea.tag_add('sel', '1.0', 'end')
    return "break"

    
   
# Root Widgets......
# Menu Bar
menu_bar = Menu(root)  

# File bars
file_bar = Menu(menu_bar, tearoff=0)  
# file.add_command(label='New File', command=new_file)  
file_bar.add_command(label='Open', command=open_file)  
file_bar.add_command(label='Save', command=save_file)  
file_bar.add_command(label='Save As', command=save_as)  
file_bar.add_separator()  
file_bar.add_command(label="Exit", command=exit)  
menu_bar.add_cascade(label="File", menu=file_bar)  


# Edit Bars
edit_bar = Menu(menu_bar, tearoff=0)  
edit_bar.add_command(label="Undo", command="")  
edit_bar.add_command(label="Redo", command="")  
edit_bar.add_separator()  
edit_bar.add_command(label="Cut", command=lambda: cut_text(False), accelerator="Ctrl+x")  
edit_bar.add_command(label="Copy", command=lambda: copy_text(False), accelerator="Ctrl+c")  
edit_bar.add_command(label="Paste", command=lambda: paste_text(False), accelerator="Ctrl+v")  
edit_bar.add_command(label="Select all", command=lambda: select_all_text(False), accelerator="Ctrl+a")  
edit_bar.add_command(label="Clear text", command=clear_text)  
menu_bar.add_cascade(label="Edit", menu=edit_bar)

# Help Bar 
help_bar = Menu(menu_bar, tearoff=0)  
help_bar.add_command(label="Documentation", command='') 
help_bar.add_command(label="Supported Transliteration", command='')  
help_bar.add_command(label="About", command=about)  
menu_bar.add_cascade(label="Help", menu=help_bar)

# Print bar
# print_bar = Menu(menu_bar, tearoff=0)  
# menu_bar.add_cascade(label="Print", menu=print_bar, command="")

# kotak teks
TextArea = Text(undo=True)
TextArea = scrolledtext.ScrolledText(root,width=70,height=15,wrap=WORD,padx=2,pady=4,borderwidth=1,relief=RIDGE)
TextArea.grid(row=1,columnspan=15)
TextArea.configure(font=text_font)

# Area Tombol
buttons = ['|', '‖','Ø','°','ᴗ','/','\\','(',')','[',']','§','—','=','+',
'a','ā', 'â','b','c','d','ḍ','e','é','ә','ê','⌫','1','2','3',
'f', 'g','h','ḥ','i','ī','î','ē','ĕ','ə̄','ě','⏎','4','5','6',
'j','k','ḳ','l', 'ḷ', 'm', 'ṁ', 'ṃ','n','ṅ','ñ','Tab','7','8','9',
'o','ö', 'p','q','r', 'ṛ','ṙ','s','ś','ṇ','ŋ','🠕','0','{','}',
't','ṭ','u','ū','û','v','w','ṣ','\'','"','🠔','🠗','🠖','-','*',
'Spasi','x','y','z','m̐',',','.','·',';',':','!','?']
varrow = 2
varcolumn = 0

# Fungsi Tombol
for button in buttons:
    command = lambda x=button:select(x)
    if button !='Spasi':
        Button(root, font=text_font, text=button,width=2,bg='black',fg='white',activebackground="white",activeforeground='black',
            relief='raised',padx=8,pady=2,bd=4,command=command).grid(row=varrow,column=varcolumn)
    if button =='Spasi':
        Button(root,text=button,width=2,bg='grey',fg='white',activebackground="white",activeforeground='black',
            relief='raised',padx=80,pady=2,bd=4,command=command).grid(row=8,columnspan=4)
    
    varcolumn+=1
    if varcolumn > 14 and varrow==2:
        varcolumn=0
        varrow+=1
    if varcolumn > 14 and varrow ==3:
        varcolumn=0
        varrow+=1
    if varcolumn > 14 and varrow ==4:
        varcolumn=0
        varrow+=1
    if varcolumn > 14 and varrow ==5:
        varcolumn=0
        varrow+=1
    if varcolumn > 14 and varrow ==6:
        varcolumn=0
        varrow+=1
    if varcolumn > 14 and varrow ==7:
        varcolumn=3
        varrow+=1


# Keyboard Shortcut functions (Bindings)

root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)
root.bind('<Control-Key-a>', select_all_text)

root.config(menu=menu_bar)
root.mainloop()
