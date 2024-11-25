from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El correo electrónico es obligatorio")
        email = self.normalize_email(email)
        extra_fields.setdefault("is_active", True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("El superusuario debe tener is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("El superusuario debe tener is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=50, verbose_name="Nombre(s)")
    last_name = models.CharField(max_length=50, verbose_name="Apellido Paterno")
    middle_name = models.CharField(max_length=50, verbose_name="Apellido Materno", blank=True, null=True)
    date_of_birth = models.DateField(verbose_name="Fecha de Nacimiento")
    gender = models.CharField(
        max_length=20,
        choices=[("Hombre", "Hombre"), ("Mujer", "Mujer"), ("Otro", "Otro")],
        verbose_name="Género"
    )
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "date_of_birth", "gender"]

    def __str__(self):
        return self.email