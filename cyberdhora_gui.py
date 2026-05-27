import tkinter as tk
from tkinter import filedialog
import webbrowser
import requests
import os
import sys
from PIL import Image, ImageTk
import io

class CyberDhoraApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CyberDhora - Digital Investigation Toolkit")
        self.geometry("500x400")
        self.configure(bg="#1a1a2e")
        
        # Load logo
        self.logo = self.load_logo()
        
        # Title with logo
        title_frame = tk.Frame(self, bg="#1a1a2e")
        title_frame.pack(pady=10)
        
        logo_label = tk.Label(title_frame, image=self.logo, bg="#1a1a2e")
        logo_label.pack(side=tk.LEFT, padx=10)
        
        title_label = tk.Label(
            title_frame,
            text="CyberDhora Investigation Portal",
            bg="#1a1a2e",
            fg="#00eeff",
            font=("Arial", 16, "bold")
        )
        title_label.pack(side=tk.LEFT)
        
        # Main frame
        main_frame = tk.Frame(self, bg="#1a1a2e")
        main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Buttons with CyberDhora styling
        button_style = {
            "width": 20,
            "height": 2,
            "bg": "#4a4a8a",
            "fg": "white",
            "activebackground": "#6a6aaa",
            "font": ("Arial", 10)
        }
        
        tk.Button(main_frame, text="APK Exploit", command=self.send_apk, **button_style).pack(pady=10)
        tk.Button(main_frame, text="PDF Malware", command=self.send_pdf, **button_style).pack(pady=10)
        tk.Button(main_frame, text="Image Payload", command=self.send_image, **button_style).pack(pady=10)
        tk.Button(main_frame, text="YouTube Attack", command=self.open_youtube, **button_style).pack(pady=10)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready for investigation...")
        status_bar = tk.Label(
            self,
            textvariable=self.status_var,
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg="#1a1a2e",
            fg="#00eeff"
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def load_logo(self):
        try:
            logo = Image.open("cyberdhora_logo.png")
            logo = logo.resize((50, 50))
            return ImageTk.PhotoImage(logo)
        except:
            return None

    def send_apk(self):
        file_path = filedialog.askopenfilename(filetypes=[("APK Files", "*.apk")])
        if file_path:
            self.status_var.set(f"APK Sent: {file_path}")
            self.deliver_payload(file_path, "APK")

    def send_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.status_var.set(f"PDF Sent: {file_path}")
            self.deliver_payload(file_path, "PDF")

    def send_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg")])
        if file_path:
            self.status_var.set(f"Image Sent: {file_path}")
            self.deliver_payload(file_path, "Image")

    def deliver_payload(self, file_path, payload_type):
        try:
            # Call external delivery script with proper arguments
            cmd = f"python payload_delivery.py {file_path} {payload_type}"
            os.system(cmd)
            self.status_var.set(f"{payload_type} delivery completed!")
        except Exception as e:
            self.status_var.set(f"Error: {str(e)}")

    def open_youtube(self):
        try:
            webbrowser.open("https://www.youtube.com/watch?v=malicious_video")
            self.status_var.set("YouTube attack launched!")
        except Exception as e:
            self.status_var.set(f"Error: {str(e)}")

if __name__ == "__main__":
    app = CyberDhoraApp()
    app.mainloop()
