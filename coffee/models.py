from django.db import models


class Coffee(models.Model):
    """
    Coffee Database Model.
    includes Name & Price only
    """
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def __str__(self):
        return self.name
