# frontend/gui.py

import tkinter as tk
from tkinter import scrolledtext
from backend.validator import PDA_Logic  # Backend'i buraya bağlıyoruz

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("PDA Project Simulator")
        self.root.geometry("700x550")
        
        # Mantık sınıfını başlat
        self.logic_engine = PDA_Logic()

        self._setup_ui()

    def _setup_ui(self):
        # --- Başlık ---
        header_frame = tk.Frame(self.root, bg="#333", pady=15)
        header_frame.pack(fill="x")
        tk.Label(header_frame, text="Matematiksel İfade Doğrulayıcı (PDA)", 
                 font=("Segoe UI", 16, "bold"), fg="white", bg="#333").pack()

        # --- Giriş Alanı ---
        input_frame = tk.Frame(self.root, pady=20)
        input_frame.pack()

        tk.Label(input_frame, text="İfade:", font=("Segoe UI", 12)).pack(side=tk.LEFT, padx=5)
        
        self.entry = tk.Entry(input_frame, font=("Consolas", 12), width=25, bd=2, relief="groove")
        self.entry.pack(side=tk.LEFT, padx=5)
        self.entry.insert(0, "n+n*n")

        self.btn_run = tk.Button(input_frame, text="ANALİZ ET", 
                                 command=self.run_simulation, 
                                 bg="#007ACC", fg="white", 
                                 font=("Segoe UI", 10, "bold"), padx=15)
        self.btn_run.pack(side=tk.LEFT, padx=10)

        # --- Sonuç Alanı ---
        self.lbl_result = tk.Label(self.root, text="Sonuç Bekleniyor...", font=("Segoe UI", 12, "bold"), fg="gray")
        self.lbl_result.pack(pady=5)

        # --- Log Alanı ---
        tk.Label(self.root, text="Yığın (Stack) Hareketleri:", font=("Segoe UI", 10)).pack(anchor="w", padx=25)
        
        self.log_area = scrolledtext.ScrolledText(self.root, width=80, height=20, font=("Consolas", 9))
        self.log_area.pack(padx=20, pady=5)

    def log_message(self, message):
        """Logic katmanından gelen mesajları ekrana yazar"""
        self.log_area.insert(tk.END, message)
        self.log_area.see(tk.END)

    def run_simulation(self):
        # Ekranı temizle
        self.log_area.delete(1.0, tk.END)
        self.lbl_result.config(text="Çalışıyor...", fg="blue")
        self.root.update()

        input_text = self.entry.get()
        
        # Backend'i çalıştır ve log fonksiyonunu parametre olarak gönder
        is_valid = self.logic_engine.validate_expression(input_text, self.log_message)

        if is_valid:
            self.lbl_result.config(text=f"✅ KABUL EDİLDİ: {input_text}", fg="green")
            self.log_area.insert(tk.END, "\n>>> BAŞARILI: İfade gramere uygundur.\n", "success")
        else:
            self.lbl_result.config(text=f"❌ REDDEDİLDİ: {input_text}", fg="red")
            self.log_area.insert(tk.END, "\n>>> BAŞARISIZ: İfade gramere uygun değildir.\n", "error")