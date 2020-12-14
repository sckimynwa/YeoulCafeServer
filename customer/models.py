from django.db import models
from django.http import Http404
from cafe.models import Cafe
from coffee.models import Coffee


class Customer(models.Model):
    """
    Customer Model
    """
    name = models.CharField(max_length=100)
    balance = models.IntegerField(default=10000)

    def get_customer(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def order_coffee(self, menu):
        """
        Order Coffee
        Note that Only One Cafe Exists.
        """
        cafe = Cafe.objects.get(pk=1)
        coffee = Coffee.objects.get(name=menu)

        # Balance Check
        if self.balance < coffee.get_price():
            return False

        # Order Coffee
        if cafe.make_coffee(menu):
            self.balance = self.balance - coffee.get_price()
            self.save()
            return True
        else:
            return False
