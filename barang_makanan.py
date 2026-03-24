from abstract_barang import AbstractBarang

class BarangMakanan(AbstractBarang):

    def __init__(self, id, nama, stok, harga, expired):
        super().__init__(id, nama, stok, harga)
        self.__expired = expired

    def get_info(self):
        return f"Makanan: {self.get_nama()} | Expired: {self.__expired}"
