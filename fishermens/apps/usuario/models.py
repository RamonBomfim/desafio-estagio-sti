import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, \
    PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Usuário', max_length=30,
                                unique=True,
                                validators=[
                                    validators.RegexValidator(
                                        re.compile('^[\\w.@+-]+$'),
                                        'Imforme um nome de usuário válido.'
                                        'Este valor deve conter apenas letras, números '
                                        'e os caracteres: @/./+/-/_.', 'invalid'
                                    )
                                ], help_text='Um nome curto que será usado para identificá-lo de '
                                'forma única na plataforma'
                                )
    name = models.CharField('Nome', max_length=60)
    email = models.EmailField('E-mail', unique=True)
    cpf = models.CharField('CPF', max_length=11)
    phone = models.CharField('Telefone celular', max_length=11)
    address = models.CharField('Endereço', max_length=100)
    complement = models.CharField('Complemento', max_length=50, null=True, blank=True)
    image = models.ImageField("Foto", upload_to='users_images', null=True, blank=True)
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]
