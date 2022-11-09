from .models import *


def get_total_basket_sum(request):
    value = 0
    basket = Basket.objects.filter(user_of=request.user.username)
    for i in basket:
        value += i.price
    return value


def basket_user(request):
    return Basket.objects.filter(user_of=request.user.username)


def have_prod_basket(request, slug):
    try:
        Basket.objects.filter(user_of=request.user.username).get(slug=slug)
        have = True
    except:
        have = False
    return have




class ShopMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['get_cat'] = Category.objects.all()
        context['counter'] = basket_user(self.request).count
        return context

