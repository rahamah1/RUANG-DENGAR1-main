from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Manager kustom untuk model user kita
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Membuat dan menyimpan user baru dengan email dan password.
        """
        if not email:
            raise ValueError('Email harus diisi')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Membuat dan menyimpan superuser baru.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', CustomUser.Role.ADMIN)  # 🧩 Tambahkan role otomatis

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser harus memiliki is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser harus memiliki is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


# Model User Kustom
class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'User'

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.USER,
    )

    email = models.EmailField('Email Kampus', unique=True)
    nama_lengkap = models.CharField('Nama', max_length=255)
    username = models.CharField('Username', max_length=150, unique=True, null=True, blank=True)
    nidn = models.CharField('NIDN', max_length=50, blank=True, null=True)
    nim = models.CharField('NIM', max_length=50, blank=True, null=True)
    prodi = models.CharField('Prodi', max_length=100, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nama_lengkap', 'username']

    def __str__(self):
        return f"{self.nama_lengkap} ({self.role})"
