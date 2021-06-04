# version 1.0 (Beta)
# GNU GENERAL PUBLIC LICENSE 3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
# This keyboard is modified from Ganeshkavhar's project (https://github.com/ganeshkavhar/On-Screen-Keyboard-Python-Project)


# ============ the code ================

import tkinter
import tkinter.scrolledtext as scrolledtext
import tkinter.messagebox
import tkinter.font as font
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import font
 
root = Tk()
root.title("Citralekha 1.0 (Beta)")
root.resizable(0,0)

# Pengaturan font
font1 = font.Font(name='TkCaptionFont', exists=True)
font1.config(family='Arial', size=10)

buttonFont = font.Font(family='Tahoma', size=20, underline=1)


# fungsi tombol
 
def select(value):
    if value=="⌫":
        txt = text.get(1.0,END)
        val = len(txt)
        TextArea.delete(1.0,END)
        text.insert(1.0,txt[:val-2])
    elif value == "⏎":
        TextArea.insert(END,"\n")
    elif value=="Spasi":
        TextArea.insert(END," ")
    elif value == "Tab":
        v.insert(END,"   ")
    else:
        TextArea.insert(END,value)


# kotakdialog
def about():
    tkinter.messagebox.showinfo("Tentang Transliterasi Nusantara","Program ini dikembangkan oleh Ilham Nurwansah untuk membantu pengetikan huruf Latin dengan diakritik dalam proses transliterasi naskah-naskah Nusantara. \n ilhamnurwansah@gmail.com")

# fungsi menu 'berkas'
def set_file_path(path):
    global file_path
    file_path = path

def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Transliterasi', '*.txt')])
    else:
        path = file_path
    with open(path, 'w', encoding='utf-8') as file:
#        code = .get('1.0, END') 
        file.write(code)
        set_file_path(path)
        
        
# Fungsi Menu Sunting
def new_file():
    global TextArea
    root.title("Tanpanama")
    file = None
    TextArea.delete(1.0, END)

def open_file():
    global TextArea
    file = filedialog.askopenfilename(filetype=[("Berkas teks", "*.txt")])
    file = file.name
    
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Teks")
        TextArea.delete(1.0, END)
        file = open(file, "rb")
        TextArea.insert(1.0, file.read())
        file.close()
   
# Root Widgets......
menubar = Menu(root)  
file = Menu(menubar, tearoff=0)  
file.add_command(label='New', command=new_file)  
file.add_command(label='Open', command=open_file)  
file.add_command(label='Save', command="")  
  
  
file.add_separator()  
  
file.add_command(label="Exit", command=exit)  
  
menubar.add_cascade(label="File", menu=file)  
edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")  
  
edit.add_separator()  
  
edit.add_command(label="Cut")  
edit.add_command(label="Cope")  
edit.add_command(label="Paste")  
edit.add_command(label="Delet")  
edit.add_command(label="Select all")  
  
menubar.add_cascade(label="Edit", menu=edit)  
help = Menu(menubar, tearoff=0)  
help.add_command(label="About", command=about)  
menubar.add_cascade(label="Help", menu=help)  

# kotak teks
TextArea = scrolledtext.ScrolledText(root,width=90,height=20,wrap=WORD,padx=2,pady=4,borderwidth=1,relief=RIDGE)
TextArea.grid(row=1,columnspan=16)

# Tab wiget pilihan layer tombol


# Tombol
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
        Button(root,text=button,width=2,bg='black',fg='white',activebackground="white",activeforeground='black',
            relief='raised',padx=10,pady=2,bd=4,command=command).grid(row=varrow,column=varcolumn)
    if button =='Spasi':
        Button(root,text=button,width=2,bg='grey',fg='white',activebackground="white",activeforeground='black',
            relief='raised',padx=110,pady=2,bd=4,command=command).grid(row=8,columnspan=5)
    
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

root.config(menu=menubar)
root.mainloop()

