from abstract_barang import AbstractBarang

class BarangPakaian(AbstractBarang):

    def __init__(self, id, nama, stok, harga, ukuran):
        super().__init__(id, nama, stok, harga)
        self.__ukuran = ukuran

    def get_info(self):
        return f"Pakaian: {self.get_nama()} | Ukuran: {self.__ukuran}"
