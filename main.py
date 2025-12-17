from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from tkinter import *
from tkinter import ttk,messagebox,Tk

def generate_key():
    global key
    key = get_random_bytes(32)
    key_entry.delete(0, END)
    key_entry.insert(0, key.hex())
    
    


# Шифрование
def encrypt_decrypt():
    try:
        cipher = AES.new(key, AES.MODE_EAX)
        global cliphertext
        ciphertext, tag = cipher.encrypt_and_digest(data)
        global nonce # Сохраните nonce для дешифрования
        nonce = cipher.nonce
        encrypt_entry.delete(0,END)
        encrypt_entry.insert(0,ciphertext)


        cipher = AES.new(key, AES.MODE_EAX, nonce)
        decrypted = cipher.decrypt_and_verify(ciphertext, tag)
        print("Расшифровано:", decrypted.decode('utf-8'))
    except TypeError:
        pass
        

# Дешифрование
# print("Расшифровано:", decrypted.decode('utf-8'))
# print('Key', key)

# Генерация ключа (32 байта для AES-256)
key = None
# Данные для шифрования (строку преобразуем в байты)
data = "Привет, мир!".encode('utf-8')






# настройки
root = Tk()
root["bg"] = "#479E92"
root.title("Шифровальщик AES")
root.geometry("1050x550")

main_menu = Menu()
main_menu["bg"] = "#5A858E"
file_menu = Menu()
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit")
 
main_menu.add_cascade(label="File", menu=file_menu)

 





label1 = ttk.Label(root,text="КЛЮЧ", width=200,font=("Arial","20","bold"),anchor='center',background="#95E4C1")
label1.pack(padx=6,pady=6,anchor=S)


# поле с ключом
key_entry = ttk.Entry(root, width =100, font=("Arial", 12 )) 
key_entry.pack(pady=20)
# кнопка генерировать ключ
generate_key1 = ttk.Button(root,text = "Генерировать ключ",command=generate_key)
generate_key1.pack(padx=6,pady=6,anchor=S)

label2 = ttk.Label(root,text="Зашифрованный текст", width=200,font=("Arial","20","bold"),anchor='center',background="#95E4C1")
label2.pack(padx=7,pady=7,anchor=S)

# поле с зашифрованным текстом
encrypt_entry = ttk.Entry(root, width=100,font=("font/Verdana.ttf",12))
encrypt_entry.pack(padx=8,pady=8,anchor=S)
# кнопка шифрование текста
encrypt_button = ttk.Button(root,text = "Шифровать",command=encrypt_decrypt)
encrypt_button.pack(padx=9,pady=9,anchor=S)



root.config(menu=main_menu)
root.mainloop()