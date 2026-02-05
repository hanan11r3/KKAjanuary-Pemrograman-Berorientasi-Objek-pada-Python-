from abc import ABC, abstractmethod

# ==========================================
# 1. ABSTRACTION (Struktur)
# ==========================================
class Produk(ABC):
    def __init__(self, nama, harga_dasar, stok):
        self.nama = nama
        self.harga_dasar = harga_dasar
        # 2. ENCAPSULATION (Keamanan)
        self.__stok = stok 

    def get_stok(self):
        return self.__stok

    def set_stok(self, jumlah):
        # Validasi stok tidak boleh negatif (Poin 25 Keamanan)
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
            return False
        else:
            self.__stok = jumlah
            return True

    @abstractmethod
    def hitung_pajak(self):
        pass

    @abstractmethod
    def info_produk(self):
        pass

# ==========================================
# 3. INHERITANCE & POLYMORPHISM (Logika Pajak)
# ==========================================
class Laptop(Produk):
    def __init__(self, nama, harga_dasar, stok, processor):
        super().__init__(nama, harga_dasar, stok)
        self.processor = processor

    def hitung_pajak(self):
        return self.harga_dasar * 0.1  # Pajak 10%

    def info_produk(self):
        return f"[LAPTOP] {self.nama} | Proc: {self.processor}"

class Smartphone(Produk):
    def __init__(self, nama, harga_dasar, stok, kamera):
        super().__init__(nama, harga_dasar, stok)
        self.kamera = kamera

    def hitung_pajak(self):
        return self.harga_dasar * 0.05  # Pajak 5%

    def info_produk(self):
        return f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}"

# ==========================================
# 4. SISTEM TRANSAKSI
# ==========================================
def buat_transaksi(produk, jumlah_beli):
    if jumlah_beli <= produk.get_stok():
        pajak = produk.hitung_pajak()
        subtotal = (produk.harga_dasar + pajak) * jumlah_beli
        
        # Update stok
        produk.set_stok(produk.get_stok() - jumlah_beli)
        
        print(f"{produk.info_produk()}")
        # Format angka menggunakan titik sebagai pemisah ribuan
        print(f" Harga Dasar: Rp {produk.harga_dasar:,.0f} | Pajak: Rp {pajak:,.0f}")
        print(f" Beli: {jumlah_beli} unit | Subtotal: Rp {subtotal:,.0f}\n".replace(',', '.'))
        return subtotal
    else:
        print(f"Stok {produk.nama} tidak mencukupi!\n")
        return 0

# ==========================================
# EXECUTION (Sesuai Target Hasil Modul)
# ==========================================
if __name__ == "__main__":
    print("--- SETUP DATA ---")
    
    rog = Laptop("ROG Zephyrus", 20000000, 0, "Ryzen 9")
    iphone = Smartphone("iPhone 13", 15000000, 0, "12MP")

    # Uji coba validasi stok (Langkah 1 & 2 di Modul)
    if rog.set_stok(10): 
        print(f"Berhasil menambahkan stok {rog.nama}: {rog.get_stok()} unit.")
    
    iphone.set_stok(-5) # Mencoba stok negatif (Akan gagal)
    
    if iphone.set_stok(20):
        print(f"Berhasil menambahkan stok {iphone.nama}: {iphone.get_stok()} unit.")

    print("\n--- STRUK TRANSAKSI ---")
    
    total = 0
    total += buat_transaksi(rog, 2)
    total += buat_transaksi(iphone, 1)

    print("-" * 40)
    print(f"TOTAL TAGIHAN: Rp {total:,.0f}".replace(',', '.'))
    print("-" * 40)