import qrcode
from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import asksaveasfilename



### Programming side

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
    qr_window.iconbitmap("appIcon.ico")
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



### Graphical side

#Main window
window = Tk()

#The config of the main window
window.title("QRCore")
window.geometry("500x500")
window.minsize(480, 360)
window.iconbitmap("appIcon.ico")
window.config(background="#2b2b2b")

#Title part
frame_title = Frame(window, bg="#2b2b2b")

title = Label(frame_title, text="QRCore", font="Courrier, 30", bg="#2b2b2b", fg="#ffffff")
title.pack()
subtitle = Label(frame_title, text="a QRCode Generator", font="Courrier, 10", bg="#2b2b2b", fg="#a0a0a0")
subtitle.pack()

frame_title.pack(expand="YES")

#Main body of the app
frame_body = Frame(window, bg="#2b2b2b")

instructions = Label(frame_body, text="Enter a link to generate QRCode :", font="Courrier, 15", bg="#2b2b2b", fg="#ffffff")
instructions.pack()
link_input = Entry(frame_body, font="Courrier, 15", bg="#2b2b2b", fg="#ffffff")
link_input.pack(pady=10)
send_button = Button(frame_body, text="Send", font="Courrier, 15", bg="#2b2b2b", fg="#ffffff", command=generate_qrcode)
send_button.pack(pady=25, fill=X)

frame_body.pack(expand="YES")

#Footer (mainly for aesthetic purposes)
frame_footer = Frame(window, bg="#2b2b2b")

mark = Label(frame_footer, text="Shortwire - 2025", font="Courrier, 10", bg="#2b2b2b", fg="#a0a0a0")
mark.pack()

frame_footer.pack(expand="YES")

#Create the window
window.mainloop()
