from datetime import datetime

class LogMixin:
    def log(self, pesan):
        print(f"[LOG {datetime.now()}] {pesan}")
