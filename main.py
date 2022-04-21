from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os


def encrypt():

    messagebox.showinfo("Info", "You can only encrypt '.txt' files anything else will lead this software to error.")
    
    messagebox.showinfo("Choose", "Choose your 'txt' file to encrypt.")
    msg = askopenfilename()

    confirm = messagebox.askokcancel("Confirm", "Confirm the path.")

    if confirm == True:

        dirs = os.listdir()

        if "Keys" not in dirs:
            os.system("mkdir Keys")
            messagebox.showinfo("Missing", "There was an folder missing and it been solved now so please restart this application.")
            exit()

        if "EncryptedFiles" not in dirs:
            os.system("mkdir EncryptedFiles")
            messagebox.showinfo("Missing", "There was an folder missing and it been solved now so please restart this application.")
            exit()

        if "DecryptedFiles" not in dirs:
            os.system("mkdir DecryptedFiles")
            messagebox.showinfo("Missing", "There was an folder missing and it been solved now so please restart this application.")
            exit()

        if "Keys" in dirs and "EncryptedFiles" in dirs and "DecryptedFiles" in dirs:

            os.system(f"""
                    openssl rsautl --encrypt -inkey Keys/public.key -pubin -in {msg} -out {msg}.enc
                    mv {msg}.enc EncryptedFiles
                    """)

    
    elif confirm == False:
        messagebox.showinfo("Abort", "Cancelled")

    else:
        messagebox.showerror("There was an error.")
    






# Initialize the window
window = Tk()
window.title("File Encryption")
window.geometry("400x300")




# Widgets
title_label = Label(text="File Encryption", font=('', 20))


encrypt_btn = Button(text="Encrypt", font=('', 15), command=encrypt, activeforeground="white", activebackground="darkgray")



# Widgets settings
title_label.pack(padx=20)

encrypt_btn.pack(padx=10, pady=15)



if __name__ == "__main__":
    window.mainloop()


