from abc import ABC, abstractmethod

# ==========================================
# 1. ABSTRACTION (Latihan 5)
# Menentukan "Kontrak" atau Blueprint Dasar
# ==========================================
class GameUnit(ABC):
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    @abstractmethod
    def serang(self, lawan):
        pass

    def diserang(self, damage):
        self.hp -= damage
        print(f"Darah {self.name} berkurang menjadi {self.hp}")

# ==========================================
# 2. ENCAPSULATION & INHERITANCE (Latihan 3 & 4)
# Mengatur Hak Akses dan Penurunan Sifat
# ==========================================
class Hero(GameUnit):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.__stok_potion = 5  # Atribut Private (Encapsulation)

    # Method Setter untuk validasi HP (Latihan 4)
    def set_hp(self, value):
        if value < 0:
            print(f"!!! Error: HP {self.name} tidak boleh negatif!")
        else:
            self.hp = value

    # Method menyerang dasar (Latihan 2)
    def serang(self, lawan):
        print(f"\n[ATTACK] {self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

# ==========================================
# 3. POLYMORPHISM (Latihan 6)
# Berbagai bentuk serangan meski method sama
# ==========================================
class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def serang(self, lawan):
        print(f"\n[MAGIC] {self.name} merapal mantra ke {lawan.name}!")
        lawan.diserang(self.attack_power + 10) # Bonus damage magic

class Archer(Hero):
    def serang(self, lawan):
        print(f"\n[RANGED] {self.name} menembakkan panah ke {lawan.name}!")
        lawan.diserang(self.attack_power)

# ==========================================
# 4. EKSEKUSI PROGRAM (MAIN)
# ==========================================
if __name__ == "__main__":
    print("--- SETUP GAME ---")
    
    # Inisialisasi Berbagai Objek (Polymorphism)
    hero1 = Hero("Layla", 100, 15)
    hero2 = Mage("Eudora", 80, 20, 100)
    hero3 = Archer("Miya", 90, 18)

    # List untuk simulasi loop Polymorphism
    tim_kita = [hero1, hero2, hero3]
    monster = Hero("Lord", 500, 50)

    # Latihan 1 & 4: Uji Coba Enkapsulasi & Akses Langsung
    print(f"\nUji Enkapsulasi:")
    hero1.set_hp(-50)  # Validasi Setter bekerja
    hero1.set_hp(150)  # Menambah HP lewat Setter
    print(f"HP {hero1.name} sekarang: {hero1.hp}")

    # Latihan 6: Loop Polymorphism
    print("\n--- WAR START ---")
    for hero in tim_kita:
        hero.serang(monster)

    print("\n--- STATUS AKHIR ---")
    print(f"Sisa HP {monster.name}: {monster.hp}")