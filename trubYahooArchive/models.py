from django.db import models


class TrubEmail(models.Model):
    rawEmail = models.TextField()

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

    def __str__(self):
        return self.pk
