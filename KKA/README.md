Analisis Bagian 1: Latihan Praktikum 1-6 (Tema Game Hero)
Fokus pada pemahaman dasar setiap pilar OOP secara bertahap.

Class & Objek: Menunjukkan bagaimana sebuah "cetakan" bernama Hero bisa menghasilkan banyak individu yang berbeda (Layla, Eudora, Miya) namun memiliki struktur dasar yang sama.

Interaksi Objek: Menunjukkan bahwa objek tidak berdiri sendiri. Saat hero1 memanggil method .serang(hero2), terjadi komunikasi data antar objek di mana HP hero2 berkurang berdasarkan attack_power dari hero1.

Encapsulation (Keamanan): Melalui method set_hp, program mampu menyaring input. Ini mencegah data "rusak", seperti HP yang bernilai negatif yang tidak masuk akal dalam logika game.

Inheritance (Pewarisan): Menggunakan super() pada class Mage dan Archer membuktikan efisiensi kode. Kita tidak perlu menulis ulang atribut name dan hp berkali-kali, cukup menurunkan dari class Hero.

Abstraction: Memaksa setiap Hero memiliki fungsi serang. Jika ada hero baru dibuat tapi tidak punya fungsi serang, Python akan memberikan error. Ini menjamin standarisasi karakter.

Polymorphism: Menunjukkan variasi aksi. Meskipun perintahnya sama-sama .serang(), Mage mengeluarkan sihir sedangkan Archer menembakkan panah.


Analisis Bagian 2: Final Challenge (Tema Sistem Toko Elektronik)
Fokus pada integrasi seluruh konsep ke dalam sistem yang fungsional sesuai halaman 14.

Keamanan Data (Encapsulation): Stok barang dilindungi secara ketat dengan atribut private (__stok). Analisisnya: User tidak boleh bisa menambah stok barang secara ilegal (seperti angka negatif). Validasi pada set_stok memastikan integritas data gudang.

Standarisasi Produk (Abstraction): Menggunakan Produk sebagai Abstract Base Class. Analisisnya: Kita tidak bisa menjual "Produk" secara umum, kita harus menjual barang nyata seperti "Laptop" atau "Smartphone". Ini memastikan setiap barang baru yang masuk ke sistem toko wajib memiliki info produk dan perhitungan pajak.

Logika Bisnis yang Berbeda (Polymorphism): Ini adalah poin paling krusial. Analisisnya: Sistem perpajakan berbeda-beda (Laptop 10% dan Smartphone 5%). Dengan polimorfisme, fungsi buat_transaksi tidak perlu peduli apa jenis barangnya; ia cukup memanggil .hitung_pajak() dan objek tersebut akan menghitung pajaknya sendiri dengan benar.

Manajemen Stok (Fungsionalitas): Terdapat logika otomatisasi di mana setiap kali transaksi berhasil, stok barang di dalam objek akan berkurang secara otomatis. Jika stok 0 atau kurang dari jumlah beli, transaksi ditolak.

User Interface (Output): Format output menggunakan pemisah ribuan (titik) untuk memastikan laporan keuangan toko mudah dibaca oleh manusia (sesuai target hasil di modul).