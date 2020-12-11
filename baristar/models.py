from django.db import models
from django.http import Http404
from coffee_machine.models import CoffeeMachine


class Baristar(models.Model):
    """
    Baristar Model
    """

    name = models.CharField(max_length=100)

    def get_baristar(self, pk):
        try:
            return Baristar.objects.get(pk=pk)
        except Baristar.DoesNotExist:
            raise Http404

    def make_coffee(self, menu):
        """
        메뉴를 입력받아 커피 머신에서 커피를 만든다.
        커피를 만들 수 없는 경우 False를 리턴한다
        커피가 만들어진 경우 True를 리턴한다.
        """
        coffeeMachine = CoffeeMachine.objects.get(pk=1)
        if coffeeMachine.get_coffee(menu):
            return True
        else:
            return False
