from django.db import models
from django.utils import timezone


class Rejestracja(models.Model):
    RECEPCJONISTA = models.ForeignKey('auth.User')
    nr = models.AutoField
    nazwisko_pacjenta = models.CharField(max_length=32)
    imie_pacjenta = models.CharField(max_length=32)
    adres_email = models.EmailField
    data_rejestracji = models.DateTimeField(
            default=timezone.now)
    data_wizyty = models.DateTimeField(
            blank=True, null=True)
    uwagi = models.CharField(max_length=200)

    def publish(self):
        self.data_rejestracji = timezone.now()
        self.save()

    def __str__(self):
        return self.nazwisko_pacjenta
