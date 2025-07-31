import qrcode as qr
import tkinter as tk
from PIL import Image,ImageTk 

class Qrcode_generator:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Qr code generator")
        self.root.geometry("300x250")

        self.url_label=tk.Label(self.root,text="Enter the Url below").pack()
        self.url_entry=tk.Entry(self.root)
        self.url_entry.pack(pady=5)

        #creating the convert button
        
        self.convert_button=tk.Button(self.root,text="Convert into QR",command=self.convert)
        self.convert_button.pack(pady=1)

        #hold the qr code
        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)

        self.root.mainloop()


    def convert(self):
         url = self.url_entry.get()
         qr_code = qr.make(url)
         qr_code.save("qr_code.png")

       
         original_image = Image.open("qr_code.png")
         resized_image = original_image.resize((60, 60))  # Resize if needed
         tk_image = ImageTk.PhotoImage(resized_image)
 
         self.image_label.config(image=tk_image)
         self.image_label.image = tk_image
 

        

if __name__=="__main__":
    Qrcode_generator()




