class DetailTransaksi:
    def __init__(self, barang, jumlah):
        self.__barang = barang
        self.set_jumlah(jumlah)

    def get_barang(self):
        return self.__barang

    def get_jumlah(self):
        return self.__jumlah

    def set_jumlah(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah harus positif")
        self.__jumlah = jumlah

    def subtotal(self):
        return self.__barang.get_harga() * self.__jumlah
