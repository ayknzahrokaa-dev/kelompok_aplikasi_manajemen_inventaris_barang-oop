from abstract_user import AbstractUser

class Admin(AbstractUser):
    def akses(self):
        return "Akses penuh"
