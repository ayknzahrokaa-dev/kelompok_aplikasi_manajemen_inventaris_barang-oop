from abstract_barang import AbstractBarang
from mixins.diskon_mixin import DiskonMixin

class BarangElektronik(AbstractBarang, DiskonMixin):

    def __init__(self, id, nama, stok, harga, garansi):
        super().__init__(id, nama, stok, harga)
        self.__garansi = garansi

    def get_info(self):
        return f"Elektronik: {self.get_nama()} | Stok: {self.get_stok()} | Garansi: {self.__garansi}"
