from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Voucher(models.Model):
    token = models.TextField()
    client = models.ForeignKey(Client)
    price = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    expire_date = models.DateTimeField(default=timezone.now)
    state = models.BooleanField(default=False)

    def create(self):
        self.save()

    def recharge(self):
        pass

    def __str__(self):
        return self.price, self.client, self.token, self.expire_date

