from django.db import models


class TelegramUserAccount(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    telegram_id = models.IntegerField()
    