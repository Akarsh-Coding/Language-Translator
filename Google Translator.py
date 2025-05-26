from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    trans = Translator()
    trans1 = trans.translate(text, src=src, dest=dest)  # Corrected here
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = sor_txt.get(1.0, END).strip()
    if masg:
        text_get = change(text=masg, src=s, dest=d)
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, text_get)
    else:
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, "Please enter some text to translate.")

# Main window
root = Tk()
root.title("Language Translator")
root.geometry("600x700")
root.config(bg="#f0f0f0")  # Light background

# Title
lab_title = Label(root, text="Google Translator", font=("Arial", 30, "bold"), bg="#4CAF50", fg="white")
lab_title.pack(pady=20)

# Source Text Frame
frame_source = Frame(root, bg="#f0f0f0")
frame_source.pack(pady=10)

lab_source = Label(frame_source, text="Source Text", font=("Arial", 16), bg="#f0f0f0", fg="#333")
lab_source.grid(row=0, column=0, padx=10, pady=5)

sor_txt = Text(frame_source, font=("Arial", 14), wrap=WORD, height=8, width=50, borderwidth=2, relief="solid")
sor_txt.grid(row=1, column=0, padx=10, pady=5)

# Language Selection Frame
frame_languages = Frame(root, bg="#f0f0f0")
frame_languages.pack(pady=10)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame_languages, value=list_text, font=("Arial", 14), width=15)
comb_sor.grid(row=0, column=0, padx=10, pady=5)
comb_sor.set("English")  # Default source language

button_translate = Button(frame_languages, text="Translate", font=("Arial", 14, "bold"), bg="#2196F3", fg="white", command=data)
button_translate.grid(row=0, column=1, padx=20, pady=5)

comb_dest = ttk.Combobox(frame_languages, value=list_text, font=("Arial", 14), width=15)
comb_dest.grid(row=0, column=2, padx=10, pady=5)
comb_dest.set("Hindi")  # Default destination language

# Destination Text Frame
frame_dest = Frame(root, bg="#f0f0f0")
frame_dest.pack(pady=10)

lab_dest = Label(frame_dest, text="Translated Text", font=("Arial", 16), bg="#f0f0f0", fg="#333")
lab_dest.grid(row=0, column=0, padx=10, pady=5)

dest_txt = Text(frame_dest, font=("Arial", 14), wrap=WORD, height=8, width=50, borderwidth=2, relief="solid")
dest_txt.grid(row=1, column=0, padx=10, pady=5)

# Exit Button
button_exit = Button(root, text="Exit", font=("Arial", 14, "bold"), bg="#F44336", fg="white", command=root.quit)
button_exit.pack(pady=20)

root.mainloop()
