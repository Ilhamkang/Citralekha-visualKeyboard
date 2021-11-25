from locale import setlocale, LC_ALL
from tkinter import scrolledtext
import webbrowser
from tkinter.font import Font
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.scrolledtext import ScrolledText
from typing import Optional

root = Tk()
file_path = ''

global selected
selected = False

# font setting
text_font = Font(size=12, family="Helvetica")


# button functions

def select(value: str) -> None:
    if value == "⌫":
        txt = TextArea.get(1.0, END)
        val = len(txt)
        TextArea.delete(1.0, END)
        TextArea.insert(1.0, txt[:val - 2])
    elif value == "↵":
        TextArea.insert(INSERT, "\n")
    elif value == "Spasi":
        TextArea.insert(INSERT, " ")
    elif value == "⇥":
        TextArea.insert(INSERT, "    ")
    elif value == "⇧":
        caps_buttons = ['|', '‖', 'Ø', '°', 'ᴗ', '/', '\\', '(', ')', '[', ']', '§', '-', '—', '=', '+',
                        'A', 'Ā', 'Â', 'Å', 'B', 'C', 'D', 'Ḍ', 'E', 'É', 'Ә', 'Ê', '⌫', '1', '2', '3',
                        'F', 'G', 'H', 'Ḥ', 'I', 'Ī', 'Î', 'J', 'Ē', 'Ĕ', 'Ə̄', 'Ě', '↵', '4', '5', '6',
                        'K', 'Ḳ', 'L', 'Ḷ', 'L̥', 'M', 'Ṁ', 'Ṃ', 'N', 'Ṇ', 'Ṅ', 'Ŋ', '⇥', '7', '8', '9',
                        'O', 'Ö', 'P', 'Q', 'R', 'Ṛ', 'R̥', 'Ṙ', 'S', 'Ś', 'Ṣ', 'Ñ', '⬆', '0', '{', '}',
                        'T', 'Ṭ', 'U', 'Ū', 'Û', 'V', 'W', 'X', 'Y', 'Z', 'Ẓ', 'Ż', '#', '*', '<', '>',
                        'Spasi', 'M̐', '˜', '’', '‘', '\'', '"', '.', '·', ';', ':', '!', '?'
                        ]
        varrow = 2
        varcolumn = 0

        for button in caps_buttons:
            command = lambda x=button: select(x)
            if button != 'Spasi':
                Button(button_frame, font=text_font, text=button, width=2, bg='black', fg='white',
                       activebackground="white", activeforeground='black', relief='raised', padx=4, pady=2, bd=4,
                       command=command).grid(row=varrow, column=varcolumn)
            if button == 'Spasi':
                Button(button_frame, text=button, width=2, bg='brown', fg='white', activebackground="white",
                       activeforeground='black', relief='raised', padx=62, pady=2, bd=4, command=command).grid(row=8,
                                                                                                               columnspan=4)
            if button == '⌫':
                Button(button_frame, text=button, width=2, bg='brown', fg='white', activebackground="white",
                       activeforeground='black',
                       relief='raised', padx=4, pady=2, bd=4, command=command).grid(row=3, column=12)
            if button == '↵':
                Button(button_frame, text=button, width=2, bg='brown', fg='white', activebackground="white",
                       activeforeground='black',
                       relief='raised', padx=4, pady=2, bd=4, command=command).grid(row=4, column=12)
            if button == '⇥':
                Button(button_frame, text=button, width=2, bg='brown', fg='white', activebackground="white",
                       activeforeground='black',
                       relief='raised', padx=4, pady=2, bd=4, command=command).grid(row=5, column=12)
            if button == '⬆':
                Button(button_frame, text=button, width=2, bg='brown', fg='white', activebackground="white",
                       activeforeground='black',
                       relief='raised', padx=4, pady=2, bd=4, command=command).grid(row=6, column=12)
            varcolumn += 1
            if varcolumn > 15 and varrow == 2:
                varcolumn = 0
                varrow += 1
            if varcolumn > 15 and varrow == 3:
                varcolumn = 0
                varrow += 1
            if varcolumn > 15 and varrow == 4:
                varcolumn = 0
                varrow += 1
            if varcolumn > 15 and varrow == 5:
                varcolumn = 0
                varrow += 1
            if varcolumn > 15 and varrow == 6:
                varcolumn = 0
                varrow += 1
            if varcolumn > 15 and varrow == 7:
                varcolumn = 3
                varrow += 1

    elif value == "⬆":
        varrow = 2
        varcolumn = 0

        for button in buttons:
            command = lambda x=button: select(x)
            if button != 'Spasi':
                Button(button_frame, font=text_font, text=button, width=2, bg='black', fg='white',
                       activebackground="white", activeforeground='black', relief='raised', padx=4, pady=2, bd=4,
                       command=command).grid(row=varrow, column=varcolumn)
            if button == 'Spasi':
                Button(button_frame, text=button, width=2, bg='brown', fg='white', activebackground="white",
                       activeforeground='black', relief='raised', padx=62, pady=2, bd=4, command=command).grid(row=8,
                                                                                                               columnspan=4)
            if button == '⌫':
                Button(button_frame, text=button, width=2, bg='brown', fg='white', activebackground="white",
                       activeforeground='black',
                       relief='raised', padx=4, pady=2, bd=4, command=command).grid(row=3, column=12)
            if button == '↵':
                Button(button_frame, text=button, width=2, bg='brown', fg='white', activebackground="white",
                       activeforeground='black',
                       relief='raised', padx=4, pady=2, bd=4, command=command).grid(row=4, column=12)
            if button == '⇥':
                Button(button_frame, text=button, width=2, bg='brown', fg='white', activebackground="white",
                       activeforeground='black',
                       relief='raised', padx=4, pady=2, bd=4, command=command).grid(row=5, column=12)
            if button == '⇧':
                Button(button_frame, text=button, width=2, bg='brown', fg='white', activebackground="white",
                       activeforeground='black',
                       relief='raised', padx=4, pady=2, bd=4, command=command).grid(row=6, column=12)

            varcolumn += 1
            if varcolumn > 15 and varrow == 2:
                varcolumn = 0
                varrow += 1
            if varcolumn > 15 and varrow == 3:
                varcolumn = 0
                varrow += 1
            if varcolumn > 15 and varrow == 4:
                varcolumn = 0
                varrow += 1
            if varcolumn > 15 and varrow == 5:
                varcolumn = 0
                varrow += 1
            if varcolumn > 15 and varrow == 6:
                varcolumn = 0
                varrow += 1
            if varcolumn > 15 and varrow == 7:
                varcolumn = 3
                varrow += 1

    else:
        TextArea.insert(INSERT, value)


# Menu bar functions 'berkas' (file)
def set_file_path(path) -> None:
    global file_path
    file_path = path


def open_file(e: bool) -> None:
    path = askopenfilename(filetypes=[('Berkas Teks', '*.txt')])
    if path:
        with open(path, 'r') as file:
            code = file.read()
            TextArea.delete('1.0', END)
            TextArea.insert('1.0', code)


def save_as() -> None:
    path = asksaveasfilename(filetypes=[('Berkas Teks', '*.txt')])
    with open(path, 'w') as file:
        code = TextArea.get('1.0', END)
        file.write(code)
        set_file_path(path)


def save_file(e: bool) -> None:
    if file_path == 'path':
        path = asksaveasfilename(filetypes=[('Berkas Teks', '*.txt')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = TextArea.get('1.0', END)
        file.write(code)
        set_file_path(path)


def endProgram() -> None:
    root.destroy()


## Edit bar functions (sunting)

def cut_text(e: Event) -> None:
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if TextArea.selection_get():
            selected = TextArea.selection_get()
            TextArea.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)


def copy_text(e: Event) -> None:
    global selected
    if e:
        selected = root.clipboard_get()

    if TextArea.selection_get():
        selected = TextArea.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)


def paste_text(e: Event) -> None:
    global selected
    if e:
        selected = root.clipboard_get()
    elif selected:
        position = TextArea.index(INSERT)
        TextArea.insert(position, selected)


def clear_text() -> None:
    TextArea.delete('1.0', END)


def select_all_text(event: Optional[Event] = None) -> str:
    TextArea.tag_add('sel', '1.0', 'end')
    return "break"


def find_text(event: Optional[Event] = None) -> str:
    search_toplevel = Toplevel(root)
    search_toplevel.title('Pencarian')
    search_toplevel.transient(root)

    Label(search_toplevel, text="Teks:").grid(row=0, column=0, sticky='e')

    search_entry_widget = Entry(
        search_toplevel, width=25)
    search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
    search_entry_widget.focus_set()
    ignore_case_value = IntVar()
    Checkbutton(
        search_toplevel, text='Abaikan huruf kapital', variable=ignore_case_value,
    ).grid(
        row=1, column=1, sticky='e', padx=2, pady=2
    )
    Button(
        search_toplevel, text="Cari", underline=0,
        command=lambda: search_output(
            search_entry_widget.get(), ignore_case_value.get() == 1,
            TextArea, search_toplevel, search_entry_widget,
        )
    ).grid(row=0, column=2, sticky='e' + 'w', padx=2, pady=2)

    def close_search_window() -> None:
        TextArea.tag_remove('match', '1.0', END)
        search_toplevel.destroy()

    search_toplevel.protocol('WM_DELETE_WINDOW', close_search_window)
    return "break"


def search_output(
    needle: str, if_ignore_case: bool, text_area: ScrolledText,
    search_toplevel: Toplevel, search_box: Entry,
) -> None:
    text_area.tag_remove('sesuai', '1.0', END)
    ditemukan = 0
    if needle:
        start_pos = '1.0'
        while True:
            start_pos = text_area.search(
                needle, start_pos, nocase=if_ignore_case, stopindex=END,
            )
            if not start_pos:
                break
            end_pos = '{}+{}c'.format(start_pos, len(needle))
            text_area.tag_add('sesuai', start_pos, end_pos)
            ditemukan += 1
            start_pos = end_pos
        text_area.tag_config(
            'sesuai', foreground='red', background='yellow')
    search_box.focus_set()
    search_toplevel.title('{} ditemukan'.format(ditemukan))


def open_guide() -> None:
    webbrowser.open('https://kairaga.com/keyboard/citralekha', new=1)


# def open_angket():
#    webbrowser.open('https://kairaga.com/keyboard/citralekha/masukan',new=2)

def about_window() -> None:
    about_window = Toplevel(root)
    about_window.geometry("450x180")
    about_window.title("Tentang Citralekha")
    about_window.resizable(False, False)
    lbl = Label(about_window,
                text="Citralekha 1.0 (Beta) \n\n Program keyboard visual ini dikembangkan untuk membantu pengetikan huruf Latin dengan diakritik dalam proses transliterasi naskah dan prasasti di Nusantara. \n\n (c) 2021 Ilham Nurwansah \n\n GNU General Public License v3.0 ",
                wraplength=400, justify="center")
    lbl.pack()


def supported_convention() -> None:
    convention_window = Toplevel(root)
    convention_window.geometry("400x300")
    convention_window.title("Tentang Citralekha")
    convention_window.resizable(False, False)
    lbl = Label(convention_window,
                text="Keyboard ini mendukung sistem transliterasi berikut: \n \nInternational Alphabet of Sanskrit Transliteration (IAST) \nOld Javanese - English Dictionary \nDHARMA \nJavanese General System of Transliteration (JGST) \nPanduan transliterasi Arab-Latin Kementerian Agama RI \n\nSistem transkripsi: \nBahasa Sunda (Palangeran Éjahan Basa Sunda) \nBahasa Jawa (PUJL) \nBahasa Aceh",
                wraplength=370, justify="left")
    lbl.pack()


menu_bar = Menu(root)
file_bar = Menu(menu_bar, tearoff=0)
edit_bar = Menu(menu_bar, tearoff=0)
help_bar = Menu(menu_bar, tearoff=0)
text_frame = Frame(root)
TextArea = scrolledtext.ScrolledText(text_frame, width=65, height=18, wrap=WORD, borderwidth=1, relief=RIDGE)
button_frame = Frame(root)

buttons = ['|', '‖', 'Ø', '°', 'ᴗ', '/', '\\', '(', ')', '[', ']', '§', '-', '—', '=', '+',
           'a', 'ā', 'â', 'å', 'b', 'c', 'd', 'ḍ', 'e', 'é', 'ә', 'ê', '⌫', '1', '2', '3',
           'f', 'g', 'h', 'ḥ', 'i', 'ī', 'î', 'j', 'ē', 'ĕ', 'ə̄', 'ě', '↵', '4', '5', '6',
           'k', 'ḳ', 'l', 'ḷ', 'l̥', 'm', 'ṁ', 'ṃ', 'n', 'ṇ', 'ṅ', 'ŋ', '⇥', '7', '8', '9',
           'o', 'ö', 'p', 'q', 'r', 'ṛ', 'r̥', 'ṙ', 's', 'ś', 'ṣ', 'ñ', '⇧', '0', '{', '}',
           't', 'ṭ', 'u', 'ū', 'û', 'v', 'w', 'x', 'y', 'z', 'ẓ', 'ż', '#', '*', '<', '>',
           'Spasi', 'm̐', '˜', '’', '‘', '\'', '"', '.', '·', ';', ':', '!', '?']


def main() -> None:
    indonesian_bcf47 = 'id_ID'
    setlocale(LC_ALL, (indonesian_bcf47, 'UTF-8'))

    root.title("Citralekha 1.0 (Beta)")
    root.resizable(0, 0)
    root.geometry()

    # file.add_command(label='New File', command=new_file)
    file_bar.add_command(label='Buka', command=lambda: open_file(False), accelerator="Ctrl+o")
    file_bar.add_command(label='Simpan', command=lambda: save_file(False), accelerator="Ctrl+s")
    file_bar.add_command(label='Simpan sebagai', command=save_as)
    file_bar.add_separator()
    file_bar.add_command(label="Keluar", command=endProgram)
    menu_bar.add_cascade(label="Berkas", menu=file_bar)

    # edit_bar.add_command(label="Undo", command="")
    # edit_bar.add_command(label="Redo", command="")
    # edit_bar.add_separator()
    edit_bar.add_command(label="Potong", command=lambda: cut_text(False), accelerator="Ctrl+x")
    edit_bar.add_command(label="Salin", command=lambda: copy_text(False), accelerator="Ctrl+c")
    edit_bar.add_command(label="Tempel", command=lambda: paste_text(False), accelerator="Ctrl+v")
    edit_bar.add_command(label="Pilih semua", command=lambda: select_all_text(False), accelerator="Ctrl+a")
    edit_bar.add_separator()
    edit_bar.add_command(label="Cari teks", command=lambda: find_text(False), accelerator="Ctrl+f")
    edit_bar.add_separator()
    edit_bar.add_command(label="Bersihkan teks", command=clear_text)
    menu_bar.add_cascade(label="Sunting", menu=edit_bar)

    help_bar.add_command(label="Dokumentasi", command=open_guide)
    help_bar.add_command(label="Sistem Transliterasi", command=supported_convention)
    # help_bar.add_command(label="[Beri Masukan]", command=open_angket)
    help_bar.add_command(label="Tentang", command=about_window)
    menu_bar.add_cascade(label="Bantuan", menu=help_bar)

    # Print bar
    # print_bar = Menu(menu_bar, tearoff=0)
    # menu_bar.add_cascade(label="Print", menu=print_bar, command="")

    # Text Frame
    text_frame.grid(row=0, columnspan=16, padx=1, pady=1)

    TextArea.configure(font=text_font)
    TextArea.grid(row=0, columnspan=156)

    # Button Frame
    button_frame.grid(row=1, columnspan=16, padx=1, pady=1)

    varrow = 2
    varcolumn = 0

    # Button functions
    for button in buttons:
        command = lambda x=button: select(x)
        if button != 'Spasi':
            Button(button_frame, font=text_font, text=button, width=2, bg='black', fg='white', activebackground="white",
                   activeforeground='black',
                   relief='raised', padx=4, pady=2, bd=4, command=command).grid(row=varrow, column=varcolumn)
        if button == 'Spasi':
            Button(button_frame, text=button, width=2, bg='brown', fg='white', activebackground="white",
                   activeforeground='black',
                   relief='raised', padx=62, pady=2, bd=4, command=command).grid(row=8, columnspan=4)
        if button == '⌫':
            Button(button_frame, text=button, width=2, bg='brown', fg='white', activebackground="white",
                   activeforeground='black',
                   relief='raised', padx=4, pady=2, bd=4, command=command).grid(row=3, column=12)
        if button == '↵':
            Button(button_frame, text=button, width=2, bg='brown', fg='white', activebackground="white",
                   activeforeground='black',
                   relief='raised', padx=4, pady=2, bd=4, command=command).grid(row=4, column=12)
        if button == '⇥':
            Button(button_frame, text=button, width=2, bg='brown', fg='white', activebackground="white",
                   activeforeground='black',
                   relief='raised', padx=4, pady=2, bd=4, command=command).grid(row=5, column=12)
        if button == '⇧':
            Button(button_frame, text=button, width=2, bg='brown', fg='white', activebackground="white",
                   activeforeground='black',
                   relief='raised', padx=4, pady=2, bd=4, command=command).grid(row=6, column=12)

        varcolumn += 1
        if varcolumn > 15 and varrow == 2:
            varcolumn = 0
            varrow += 1
        if varcolumn > 15 and varrow == 3:
            varcolumn = 0
            varrow += 1
        if varcolumn > 15 and varrow == 4:
            varcolumn = 0
            varrow += 1
        if varcolumn > 15 and varrow == 5:
            varcolumn = 0
            varrow += 1
        if varcolumn > 15 and varrow == 6:
            varcolumn = 0
            varrow += 1
        if varcolumn > 15 and varrow == 7:
            varcolumn = 3
            varrow += 1

    # Keyboard Shortcut functions (Bindings)

    root.bind('<Control-Key-x>', cut_text)
    root.bind('<Control-Key-c>', copy_text)
    root.bind('<Control-Key-v>', paste_text)
    root.bind('<Control-Key-a>', select_all_text)
    root.bind('<Control-Key-f>', find_text)
    root.bind('<Control-Key-o>', open_file)
    root.bind('<Control-Key-s>', save_file)

    root.config(menu=menu_bar)
    root.mainloop()


if __name__ == '__main__':
    main()
