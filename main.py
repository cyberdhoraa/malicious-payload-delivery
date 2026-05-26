import tkinter as tk
from tkinter import filedialog
import webbrowser

class PayloadDeliveryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Payload Delivery")
        self.geometry("300x200")
        
        # Buttons for different payloads
        tk.Button(self, text="APK", command=self.send_apk).pack()
        tk.Button(self, text="PDF", command=self.send_pdf).pack()
        tk.Button(self, text="Image", command=self.send_image).pack()
        tk.Button(self, text="YouTube Link", command=self.open_youtube).pack()

    def send_apk(self):
        file_path = filedialog.askopenfilename(filetypes=[("APK Files", "*.apk")])
        if file_path:
            print(f"Sending APK: {file_path}")

    def send_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            print(f"Sending PDF: {file_path}")

    def send_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg")])
        if file_path:
            print(f"Sending Image: {file_path}")

    def open_youtube(self):
        webbrowser.open("https://www.youtube.com/watch?v=malicious_video")

if __name__ == "__main__":
    app = PayloadDeliveryApp()
    app.mainloop()
