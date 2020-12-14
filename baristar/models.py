from django.db import models
from django.http import Http404
from coffee_machine.models import CoffeeMachine


class Baristar(models.Model):
    """
    Baristar Model
    """

    name = models.CharField(max_length=100)
    cafe_id = models.ForeignKey('cafe.Cafe', on_delete=models.CASCADE)

    def get_coffee_machine(self):
        """
        Baristar가 속한 Cafe의 CoffeeMachine을 리턴한다.
        Cafe의 규모가 작으므로 CoffeeMachine은 하나라고 가정한다.
        """
        try:
            return CoffeeMachine.objects.get(cafe_id=self.cafe_id)
        except CoffeeMachine.DoesNotExist:
            raise Http404

    def make_coffee(self, menu):
        """
        메뉴를 입력받아 커피 머신에서 커피를 만든다.
        커피를 만들 수 없는 경우 False를 리턴한다
        커피가 만들어진 경우 True를 리턴한다.
        """
        coffee_machine = self.get_coffee_machine()
        if coffee_machine.make_coffee(menu):
            return True
        else:
            return False
