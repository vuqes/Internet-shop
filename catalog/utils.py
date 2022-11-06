from .models import *


class ShopMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['get_cat'] = Category.objects.all()
        context['counter'] = Basket.objects.all().count
        return context

    @staticmethod
    def get_total_basket_sum():
        basket = Basket.objects.all()
        value = 0
        for i in basket:
            value += i.price
        return value
