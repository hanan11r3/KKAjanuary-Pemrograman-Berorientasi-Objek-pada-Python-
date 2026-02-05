class AkunBank:
    def __init__(self, saldo):
        self.__saldo = saldo
    def cek_saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah


    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Berhasil tarik: {jumlah}")
        elif jumlah > self.__saldo:
            print("Gagal tarik: Saldo tidak mencukupi!")
        else:
            print("Gagal tarik: Jumlah harus lebih dari 0")


rekening = AkunBank(1000)
rekening.setor(500)
rekening.tarik(300)

print(f"Saldo akhir: {rekening.cek_saldo()}")