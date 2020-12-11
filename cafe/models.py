from django.db import models
from django.http import Http404
from baristar.models import Baristar
from coffee.models import Coffee
from coffee_machine.models import CoffeeMachine
from fridge.models import Fridge


class Cafe(models.Model):
    """
    Cafe Model
    """
    balance = models.IntegerField(default=1000000)

    def get_cafe(self, pk):
        try:
            return Cafe.objects.get(pk=pk)
        except Cafe.DoesNotExist:
            raise Http404

    def get_coffee(self, menu):
        coffee = Coffee.objects.get(name=menu)
        baristar = Baristar.objects.get(pk=1)

        if baristar.make_coffee(menu):
            self.balance = self.balance + coffee.get_price()
            self.save()
            return True
        else:
            return False
