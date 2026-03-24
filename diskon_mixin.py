class DiskonMixin:
    def hitung_diskon(self, harga, persen):
        return harga - (harga * persen / 100)
