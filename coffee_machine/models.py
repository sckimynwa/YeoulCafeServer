from django.db import models
from django.http import Http404
from fridge.models import Fridge


class CoffeeMachine(models.Model):
    """
    Coffee Machine Model
    """

    name = models.CharField(max_length=100)
    broken_status = models.BooleanField(default=False)

    def get_coffee_machine(self, pk):
        try:
            return CoffeeMachine.objects.get(pk=pk)
        except CoffeeMachine.DoesNotExist:
            raise Http404

    def get_coffee_machine_status(self):
        return self.broken_status

    def fix_coffee_machin(self):
        self.broken_status = False
        self.save()

    def make_coffee(self, menu):
        """
        커피를 만든다. 만들 수 없는 경우 False를 리턴한다.
        커피를 만드는데 필요한 재료는 냉장고에서 가져오고 냉장고는 하나만 있다고 가정한다.
        추후 여러 개의 냉장고가 추가될 경우 재료가 있는 냉장고 중 하나에서 가져오면 된다.
        """
        fridge = Fridge.objects.get(pk=1)

        # Coffee Machine Status Check
        if self.broken_status:
            return False

        # Coffee Ingridients Check from Fridge
        if fridge.get_ingridients(menu):
            return True
        else:
            return False
