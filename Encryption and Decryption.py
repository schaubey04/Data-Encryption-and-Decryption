from tkinter import*
from tkinter import messagebox
import base64

shiva=Tk()
shiva.title("Encryption and Decryption")
shiva.geometry("420x420")
shiva.resizable(False,False)
shiva.configure(bg="gray")


def encrypt():
    password=code.get()

    if password=="8485":
        messagebox.showinfo("right","Password is correct")
        root=Toplevel(shiva)
        root.title("Encryption")
        root.geometry("400x250")
        root.configure(bg="pink")

        msg=text1.get(1.0,END)
        msg_encode=msg.encode("ascii")
        base64_bytes=base64.b64encode(msg_encode)
        encrypt=base64_bytes.decode("ascii")

        Label(root,text="Your Code is encrypted").place(x=5,y=6)
        text2=Text(root,font="30",bd=4,wrap=WORD)
        text2.place(x=2,y=30,width=390,height=180)
        text2.insert(1.0,encrypt)


        #icon
        icon=PhotoImage(file="icon.png")
        root.iconphoto(False,icon)
    else:
        messagebox.showerror("Invalid","Please Enter Correct Password")



def decrypt():
    password=code.get()
    
    if password=="8485":
        messagebox.showinfo("right","Password is correct")
        root1=Toplevel(shiva)
        root1.title("Decryption")
        root1.geometry("400x250")
        root1.configure(bg="green")

        msg=text1.get(1.0,END)
        msg_decode=msg.encode("ascii")
        base64_bytes=base64.b64decode(msg_decode)
        decrypt=base64_bytes.decode("ascii")

        Label(root1,text="your code is decrypted").place(x=5,y=6)
        text3=Text(root1,font="30",bd=4,wrap=WORD)
        text3.place(x=2,y=30,width=390,height=180)
        text3.insert(1.0,decrypt)

        #icon
        icon=PhotoImage(file="icon.png")
        root1.iconphoto(False,icon)
    else:
        messagebox.showerror("Invalid","Please Enter Correct Password")

def reset():
    text1.delete(1.0,END)
    entry.delete(0,END)
    



#icon
img_icon=PhotoImage(file="icon.png")
shiva.iconphoto(False,img_icon)


Label(shiva,text="Enter the text for Encryption and Decryption",font="imapack 14",bg="white",fg="black").pack(side=TOP,fill=BOTH)

#Text

text1=Text(shiva,bd=0,relief=GROOVE,bg="white",font="impack 13")
text1.place(x=5,y=45,width=410,height=120)

Label(shiva,text="Enter the Secret key",font="impack 10",fg="black").place(x=135,y=180)

#Entry
code=StringVar()

entry=Entry(shiva,width=15,font="imapack",textvariable=code,show="*")
entry.place(x=115,y=210)

#Button

button_encrypt=Button(shiva,text="Encrypt",font="impack 13",bg="green",activeforeground="pink",width=15,command=encrypt)
button_encrypt.place(x=50,y=270)

button_decrypt=Button(shiva,text="Decrypt",font="impack 13",bg="blue",activeforeground="pink",width=15,command=decrypt)
button_decrypt.place(x=250,y=270)

button_reset=Button(shiva,text="Reset",font="impack 13",bg="red",activeforeground="pink",width=15,command=reset)
button_reset.place(x=155,y=320)




shiva.mainloop()