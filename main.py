import qrcode as qr
import tkinter as tk
from tkinter import filedialog
from PIL import Image,ImageTk 

class Qrcode_generator:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Qr code generator")
        self.root.geometry("450x500")

        self.url_label=tk.Label(self.root,text="Enter the Url below").pack()
        self.url_entry=tk.Entry(self.root)
        self.url_entry.pack(pady=5)

        #creating the convert button
        
        self.convert_button=tk.Button(self.root,text="Convert into QR",command=self.convert)
        self.convert_button.pack(pady=1)

        #hold the qr code
        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)

        #label of "save as"
        self.label_save=tk.Button(self.root,text="Save as ",command=self.save_as)
        self.label_save.pack(pady=2)

    


        self.root.mainloop()


    def convert(self):
         url = self.url_entry.get()
         self.qr_code = qr.make(url)
         self.qr_code.save("qr_code.png")

       
         original_image = Image.open("qr_code.png")
         resized_image = original_image.resize((200, 200))  # Resize if needed
         tk_image = ImageTk.PhotoImage(resized_image)
 
         self.image_label.config(image=tk_image)
         self.image_label.image = tk_image

    def save_as(self):
    
        
         self.file_path=filedialog.asksaveasfilename(
             defaultextension=".png",
             filetypes=[("PNG files","*.png")],
             title="Save Qr code as"
         )
         if self.file_path:
             self.qr_code.save(self.file_path)
             self.display_sace=tk.Label(self.root,text=f"QR code saved at {self.file_path}").pack(pady=1)

         else:
             self.display_not_saved=tk.Label(self.root,text="Not saved anywhere").pack(pady=1)

if __name__=="__main__":
    Qrcode_generator()




