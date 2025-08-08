import os
import sys
import qrcode
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from pyzbar.pyzbar import decode
from tkinter.filedialog import asksaveasfilename, askopenfilename



### ------------------------------------------------------- Programming side

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def generate_qrcode():
    link = link_input.get()
    if len(link) == 0:
        return

    # Generate the QRCOde thx to the qrcode lib
    qr_img = qrcode.make(link)

    # Resize it
    qr_img = qr_img.resize((300, 300))

    # Convert the image to Tkinter
    qr_photo = ImageTk.PhotoImage(qr_img)

    # New window
    qr_window = Toplevel(window)
    qr_window.title("QRCore")
    qr_window.geometry("300x350")
    qr_window.minsize(300, 350)
    qr_window.iconbitmap(resource_path("appIcon.ico"))
    qr_window.config(background="#2b2b2b")

    # Keep references to avoid garbage collection
    qr_window.qr_img = qr_img
    qr_window.qr_photo = qr_photo

    canvas = Canvas(qr_window, width=300, height=300, bg="#2b2b2b", highlightthickness=0)
    canvas.create_image(150, 150, image=qr_photo)
    canvas.pack()

    # Save function
    def save_qr():
        file_path = asksaveasfilename(defaultextension=".png",
                                       filetypes=[("PNG files", "*.png")],
                                       title="Save your generated QR Code")
        if file_path:
            qr_window.qr_img.save(file_path)

    # Save button
    save_button = Button(qr_window, text="Save", font="Courrier, 12", bg="#444444", fg="white", command=save_qr)
    save_button.pack(pady=10)

def read_qrcode():
    global canvas, text_content

    qrcore_file_path = askopenfilename(
        title="Choisir un fichier",
        filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp *.gif"), ("Tous les fichiers", "*.*")]
    )
    if qrcore_file_path:
        path.config(text=f"The path to this QRcode is : {qrcore_file_path}")
        send_button.config(text="Choose another")

        if 'canvas' in globals():
            canvas.destroy()
        if 'text_content' in globals():
            text_content.destroy()

        qr_img = Image.open(qrcore_file_path)
        qr_img = qr_img.resize((300, 300))
        qr_photo = ImageTk.PhotoImage(qr_img)

        frame_body.qr_img = qr_img
        frame_body.qr_photo = qr_photo

        canvas = Canvas(frame_body, width=300, height=300, bg="#2b2b2b", highlightthickness=0)
        canvas.create_image(150, 150, image=qr_photo)
        canvas.pack(pady=20)

        decoded = decode(qr_img)
        if len(decoded) < 1:
            text = 'The QRCode is empty...'
        else:
            message = decoded[0][0].decode('UTF-8')
            text = f'The QRCode content is : "{message}"'

        text_content = Label(frame_body, text=text, font="Courrier, 10", bg="#2b2b2b", fg="#ffffff")
        text_content.pack()


### ------------------------------------------------------- Graphical side

#Main window
window = Tk()

#The config of the main window
window.title("QRCore")
window.geometry("500x700")
window.minsize(480, 360)
window.iconbitmap(resource_path("appIcon.ico"))
window.config(background="#2b2b2b")

notebook = ttk.Notebook(window)
tab_generate = Frame(notebook, bg="#2b2b2b")
tab_read = Frame(notebook, bg="#2b2b2b")
notebook.add(tab_generate, text="Generate")
notebook.add(tab_read, text="Read")
notebook.pack(expand=1, fill="both")

## ------------------------------------------------------- Generate a QRCode
#Title part
frame_title = Frame(tab_generate, bg="#2b2b2b")

title = Label(frame_title, text="QRCore", font="Courrier, 30", bg="#2b2b2b", fg="#ffffff")
title.pack()
subtitle = Label(frame_title, text="a QRCode Generator", font="Courrier, 10", bg="#2b2b2b", fg="#a0a0a0")
subtitle.pack()

frame_title.pack(expand="YES")

#Main body of the app
frame_body = Frame(tab_generate, bg="#2b2b2b")

instructions = Label(frame_body, text="Enter a link to generate QRCode :", font="Courrier, 15", bg="#2b2b2b", fg="#ffffff")
instructions.pack()
link_input = Entry(frame_body, font="Courrier, 15", bg="#2b2b2b", fg="#ffffff")
link_input.pack(pady=10)
send_button = Button(frame_body, text="Send", font="Courrier, 15", bg="#2b2b2b", fg="#ffffff", command=generate_qrcode)
send_button.pack(pady=25, fill=X)

frame_body.pack(expand="YES")

#Footer (mainly for aesthetic purposes)
frame_footer = Frame(tab_generate, bg="#2b2b2b")

mark = Label(frame_footer, text="Shortwire - 2025", font="Courrier, 10", bg="#2b2b2b", fg="#a0a0a0")
mark.pack()

frame_footer.pack(expand="YES")

## ------------------------------------------------------- Read a QRCode
#Title part
frame_title = Frame(tab_read, bg="#2b2b2b")

title = Label(frame_title, text="QRCore", font="Courrier, 30", bg="#2b2b2b", fg="#ffffff")
title.pack()
subtitle = Label(frame_title, text="a QRCode Generator", font="Courrier, 10", bg="#2b2b2b", fg="#a0a0a0")
subtitle.pack()

frame_title.pack(expand="YES")

#Main body of the app
frame_body = Frame(tab_read, bg="#2b2b2b")

instructions = Label(tab_read, text="Select the QRCode to be read :", font="Courrier, 15", bg="#2b2b2b", fg="#ffffff")
instructions.pack()
send_button = Button(frame_body, text="Choose", font="Courrier, 15", bg="#2b2b2b", fg="#ffffff", command=read_qrcode)
send_button.pack(pady=10, fill=X)

path = Label(tab_read, text=f"You didn't pick a QRCode yet...", font="Courrier, 10", bg="#2b2b2b", fg="#ffffff")
path.pack()

frame_body.pack(expand="YES")

#Footer (mainly for aesthetic purposes)
frame_footer = Frame(tab_read, bg="#2b2b2b")

mark = Label(frame_footer, text="Shortwire - 2025", font="Courrier, 10", bg="#2b2b2b", fg="#a0a0a0")
mark.pack()

frame_footer.pack(expand="YES")



#Create the window
window.mainloop()
