from django.db import models
from django.http import Http404
from baristar.models import Baristar
from coffee.models import Coffee


class Cafe(models.Model):
    """
    Cafe Model
    """
    id = models.BigAutoField(primary_key=True)
    balance = models.IntegerField(default=1000000)

    def get_baristar(self):
        try:
            return Baristar.objects.get(cafe_id=self.id)
        except Baristar.DoesNotExist:
            raise Http404

    def get_coffee(self):
        try:
            return Coffee.objects.get(cafe_id=self.id)
        except Coffee.DoesNotExist:
            raise Http404

    def make_coffee(self, menu):
        """
        Make Coffee
        if Coffee is Made, return True, else return False
        """
        baristar = self.get_baristar()
        coffee = self.get_coffee()

        if baristar.make_coffee(menu):
            self.balance = self.balance + coffee.get_price()
            self.save()
            return True
        else:
            return False
