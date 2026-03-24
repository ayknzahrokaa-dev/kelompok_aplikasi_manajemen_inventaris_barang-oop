class ValidasiMixin:
    def validasi_stok(self, stok):
        if stok < 0:
            raise ValueError("Stok tidak boleh negatif")

    def validasi_harga(self, harga):
        if harga < 0:
            raise ValueError("Harga tidak boleh negatif")
