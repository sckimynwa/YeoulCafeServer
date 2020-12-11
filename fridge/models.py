from django.db import models
from django.http import Http404


class Fridge(models.Model):
    """
    milk & bean & water filled to 100 each when cafe opened
    """
    name = models.CharField(max_length=100)
    milk = models.IntegerField(default=100)
    bean = models.IntegerField(default=100)
    water = models.IntegerField(default=100)

    def get_fridge(self, pk):
        try:
            return Fridge.objects.get(pk=pk)
        except Fridge.DoesNotExist:
            raise Http404

    def is_empty_ingridients(self, ingridient, amount):
        """
        커피를 만들기 전에 재료가 충분한지를 사전에 확인하는 내부 메소드
        """
        if ingridient == 'milk' and self.milk < amount:
            return True
        elif ingridient == 'bean' and self.bean < amount:
            return True
        elif ingridient == 'water' and self.water < amount:
            return True
        else:
            return False

    def fill_ingridients(self, ingridient, amount):
        """
        재료를 채워 넣는다.
        """
        if ingridient == 'bean':
            self.bean = self.bean + amount
            self.save()
        elif ingridient == 'water':
            self.water = self.water + amount
            self.save()
        elif ingridient == 'milk':
            self.milk = self.milk + amount
            self.save()

    def get_ingridients(self, coffee):
        """
        커피의 종류를 알려주면,
        재료를 커피 머신에게 공급한다. 
        return True, False
        """
        if coffee == 'Americano':
            if not(self.is_empty_ingridients('bean', 1)) and not(self.is_empty_ingridients('water', 1)):
                self.bean = self.bean - 1
                self.water = self.water - 1
                self.save()
                return True
            else:
                return False
        elif coffee == 'Espresso':
            if not(self.is_empty_ingridients('bean', 1)) and not(self.is_empty_ingridients('water', 1)):
                self.bean = self.bean - 1
                self.water = self.water - 1
                self.save()
                return True
            else:
                return False

    def __str__(self):
        return self.name
