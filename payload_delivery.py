import tkinter as tk
from tkinter import filedialog
import webbrowser

class CyberDhoraApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CyberDhora - Digital Investigation Toolkit")
        self.geometry("400x300")
        self.configure(bg="#1a1a2e")  # Dark blue background
        
        # Title label
        title_label = tk.Label(
            self, 
            text="CyberDhora Investigation Portal",
            bg="#1a1a2e",
            fg="#00eeff",
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=20)

        # Frame for buttons
        button_frame = tk.Frame(self, bg="#1a1a2e")
        button_frame.pack(pady=20)

        # Buttons with CyberDhora branding
        tk.Button(
            button_frame,
            text="APK Exploit",
            command=self.send_apk,
            width=15,
            height=2,
            bg="#4a4a8a",
            fg="white",
            activebackground="#6a6aaa"
        ).pack(pady=10)

        tk.Button(
            button_frame,
            text="PDF Malware",
            command=self.send_pdf,
            width=15,
            height=2,
            bg="#4a4a8a",
            fg="white",
            activebackground="#6a6aaa"
        ).pack(pady=10)

        tk.Button(
            button_frame,
            text="Image Payload",
            command=self.send_image,
            width=15,
            height=2,
            bg="#4a4a8a",
            fg="white",
            activebackground="#6a6aaa"
        ).pack(pady=10)

        tk.Button(
            button_frame,
            text="YouTube Attack",
            command=self.open_youtube,
            width=15,
            height=2,
            bg="#4a4a8a",
            fg="white",
            activebackground="#6a6aaa"
        ).pack(pady=10)

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

    def send_apk(self):
        file_path = filedialog.askopenfilename(filetypes=[("APK Files", "*.apk")])
        if file_path:
            self.status_var.set(f"APK Sent: {file_path}")
            print(f"Sending APK: {file_path}")

    def send_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.status_var.set(f"PDF Sent: {file_path}")
            print(f"Sending PDF: {file_path}")

    def send_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg")])
        if file_path:
            self.status_var.set(f"Image Sent: {file_path}")
            print(f"Sending Image: {file_path}")

    def open_youtube(self):
        webbrowser.open("https://www.youtube.com/watch?v=malicious_video")
        self.status_var.set("YouTube attack launched!")

if __name__ == "__main__":
    app = CyberDhoraApp()
    app.mainloop()
