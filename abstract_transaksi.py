from abc import ABC, abstractmethod
from datetime import datetime

class AbstractTransaksi(ABC):
    def __init__(self, id_transaksi):
        self._id = id_transaksi
        self._tanggal = datetime.now()

    @abstractmethod
    def proses(self):
        pass