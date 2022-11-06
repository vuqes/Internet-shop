from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .models import *
from .forms import *
from .utils import ShopMixin


class Home(ShopMixin, ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'get'
    extra_context = {'title': 'E-shop'}


class CategoryList(ListView):
    template_name = 'catalog/list_cat.html'
    context_object_name = 'get'

    def get_queryset(self):
        queryset = Product.objects.filter(category__slug=self.kwargs['slug'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['get_cat'] = Category.objects.all()
        context['counter'] = Basket.objects.all().count
        context['title'] = Category.objects.filter(slug=self.kwargs['slug'])[0]
        return context


class ShowProduct(DetailView):
    template_name = 'catalog/product.html'
    context_object_name = 'get'

    def get_queryset(self):
        queryset = Product.objects.filter(slug=self.kwargs['slug'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['get_cat'] = Category.objects.all()
        context['counter'] = Basket.objects.all().count
        context['title'] = Product.objects.filter(slug=self.kwargs['slug'])[0]
        return context


class MyBasket(ShopMixin, ListView):
    model = Basket
    template_name = 'catalog/basket.html'
    context_object_name = 'get'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['get_cat'] = Category.objects.all()
        context['counter'] = Basket.objects.all().count
        context['sum_basket'] = self.get_total_basket_sum
        context['title'] = 'Корзина'
        return context


def add_basket(request, slug):  # Добавляем товар в корзину, а если он там есть, то к value + 1
    get = Product.objects.get(slug=slug)
    price = get.price
    try:
        add = Basket.objects.get(slug=slug)
        add.value += 1
        add.price += price
        add.save()
    except:
        Basket.objects.create(name=get.name, price=get.price, stock=get.stock, category_id=get.category_id, image=get.image, slug=get.slug, value=1)
    return redirect(request.META.get('HTTP_REFERER'))


def remove_basket(request, slug):  # Удаляем товар из корзины
    delete = Basket.objects.get(slug=slug)
    delete.delete()
    return redirect('basket')


class Register(CreateView):
    form_class = RegisterForm
    template_name = 'catalog/register.html'
    extra_context = {'title': 'Регистрация'}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'catalog/login.html'
    extra_context = {'title': 'Вход'}

    def get_success_url(self):
        return reverse_lazy('home')


class UserRoom(ShopMixin, ListView):
    model = Product
    template_name = 'catalog/user_room.html'
    context_object_name = 'get'
    extra_context = {'title': 'Личный кабинет'}
