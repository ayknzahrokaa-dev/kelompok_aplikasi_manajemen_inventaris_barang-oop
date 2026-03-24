from abstract_transaksi import AbstractTransaksi

class BarangKeluar(AbstractTransaksi):

    def __init__(self, id_transaksi, barang, jumlah):
        super().__init__(id_transaksi)
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

    def proses(self):
        try:
            self.__barang.kurangi_stok(self.__jumlah)
            print("Barang keluar berhasil")
        except Exception as e:
            print("Error:", e)
