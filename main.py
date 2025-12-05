# main.py
import tkinter as tk
from frontend.gui import Application

if __name__ == "__main__":
    # Ana pencereyi oluştur
    root = tk.Tk()
    
    # Uygulamayı başlat
    app = Application(root)
    
    # Döngüyü başlat
    root.mainloop()