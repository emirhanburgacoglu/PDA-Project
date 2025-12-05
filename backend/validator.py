# backend/validator.py

class PDA_Logic:
    def __init__(self):
        # NOT: Kodun sonsuz döngüye girmemesi için "Right Recursive" (Sağ Özyinelemeli)
        # mantık kullanıyoruz. Matematiksel sonucu değiştirmez, sadece işlem sırasını düzeltir.
        pass

    def validate_expression(self, input_string, log_callback=None):
        """
        LL(1) Parsing mantığıyla (Right Recursion) yığın simülasyonu.
        """
        # 1. Hazırlık
        # Stack Başlangıcı: E (Expression)
        stack = ["Z", "E"] 
        clean_input = input_string.replace(" ", "")
        input_buffer = list(clean_input) + ["Z"]
        current_idx = 0
        step_count = 1

        if log_callback:
            log_callback(f"BAŞLANGIÇ: Girdi='{clean_input}' | Stack=['Z', 'E']\n" + "-"*50 + "\n")

        # 2. Döngü
        while len(stack) > 0:
            top = stack.pop()
            
            # Girdinin sonuna geldik mi kontrolü
            if current_idx < len(input_buffer):
                current_char = input_buffer[current_idx]
            else:
                current_char = ""

            # Loglama
            if log_callback:
                # Görsellik için stack'i stringe çevir
                stack_view = str(stack + [top]) 
                log_callback(f"Adım {step_count}: Okunan='{current_char}' | Yığın={stack_view}\n")
            
            step_count += 1
            
            # Güvenlik Kilidi (Çok uzarsa durdur)
            if step_count > 100:
                if log_callback: log_callback("HATA: İşlem çok uzadı (Sonsuz Döngü Koruması).\n")
                return False

            # --- DURUM A: Eşleşme (Match) ---
            # Yığının tepesindeki sembol, terminal ise (n, +, *, (, ) )
            if top in ["+", "*", "(", ")", "n", "Z"]:
                if top == current_char:
                    if top == "Z":
                        if log_callback: log_callback("-" * 50 + "\nSONUÇ: Yığın Boşaldı. Girdi Bitti.\n")
                        return True
                    current_idx += 1 # Sonraki karaktere geç
                    continue
                else:
                    # Beklenen karakter gelmedi
                    if log_callback: log_callback(f"HATA: '{top}' bekleniyordu, '{current_char}' geldi.\n")
                    return False
            
            # --- DURUM B: Değişken Açılımı (Expand) ---
            # Buradaki kurallar Right-Recursive (Sağ Özyinelemeli) olarak düzenlendi.
            # E  -> T E'
            # E' -> + T E' | ε
            # T  -> F T'
            # T' -> * F T' | ε
            # F  -> ( E ) | n

            expansion = []

            if top == "E":
                # E -> T E'
                expansion = ["T", "E_prime"]
            
            elif top == "E_prime":
                if current_char == "+":
                    # E' -> + T E'
                    expansion = ["+", "T", "E_prime"]
                else:
                    # E' -> ε (Boşluk - Epsilon)
                    # Yığına bir şey ekleme, sadece E_prime'ı yok et.
                    if log_callback: log_callback(f"   -> Epsilon Geçişi (E_prime silindi)\n")
                    continue 

            elif top == "T":
                # T -> F T'
                expansion = ["F", "T_prime"]

            elif top == "T_prime":
                if current_char == "*":
                    # T' -> * F T'
                    expansion = ["*", "F", "T_prime"]
                else:
                    # T' -> ε
                    if log_callback: log_callback(f"   -> Epsilon Geçişi (T_prime silindi)\n")
                    continue

            elif top == "F":
                if current_char == "(":
                    # F -> ( E )
                    expansion = ["(", "E", ")"]
                elif current_char == "n" or current_char.isalnum():
                    # F -> n
                    expansion = ["n"]
                else:
                    if log_callback: log_callback(f"HATA: F kuralı için '{current_char}' geçersiz.\n")
                    return False
            
            else:
                if log_callback: log_callback(f"HATA: Tanımsız sembol '{top}'.\n")
                return False

            # Kuralları yığına TERS sırada ekle (Push)
            for symbol in reversed(expansion):
                stack.append(symbol)
            
            if log_callback: 
                log_callback(f"   -> KURAL: {top} -> {''.join(expansion)}\n")

        return False