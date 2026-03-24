from abstract_user import AbstractUser

class Staff(AbstractUser):
    def akses(self):
        return "Akses terbatas"
