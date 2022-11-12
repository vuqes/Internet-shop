from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, FormView

from .models import *
from .forms import *
from .utils import *


def home(request):
    basket = Basket.objects.filter(user_of=request.user.username)
    try:
        user = Account.objects.create(username=request.user.username)
    except:
        user = request.user.username
    context = {
        'get': Product.objects.all(),
        'get_cat': Category.objects.all(),
        'counter': basket.count,
        'title': 'E-shop',
    }
    return render(request, 'catalog/home.html', context)


class CategoryList(ListView):
    template_name = 'catalog/list_cat.html'
    context_object_name = 'get'

    def get_queryset(self):
        queryset = Product.objects.filter(category__slug=self.kwargs['slug'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['counter'] = basket_user(self.request).count
        context['title'] = Category.objects.filter(slug=self.kwargs['slug'])[0]
        context['user_name'] = basket_user(self.request)
        context['get_cat'] = Category.objects.all()
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
        context['counter'] = basket_user(self.request).count
        context['title'] = Product.objects.filter(slug=self.kwargs['slug'])[0]
        context['already_in_basket'] = have_prod_basket(self.request, self.kwargs['slug'])
        return context


def my_basket(request):
    context = {
        'get': Product.objects.all(),
        'get_cat': Category.objects.all(),
        'counter': basket_user(request).count,
        'title': 'Корзина',
        'sum_basket': get_total_basket_sum(request),
        'products_user': basket_user(request),
    }
    return render(request, 'catalog/basket.html', context)


def add_basket(request, slug):  # Добавляем товар в корзину, а если он там есть, то к value + 1 и к price
    get = Product.objects.get(slug=slug)
    try:
        add = Basket.objects.get(slug=slug)
        if add.user_of == request.user.username:
            add.value += 1
            add.price += get.price
            add.save()
        else:
            Basket.objects.create(name=get.name, price=get.price, slug=get.slug, value=1, image=get.image,  user_of=request.user.username)
    except:
        Basket.objects.create(name=get.name, price=get.price, slug=get.slug, value=1, image=get.image, user_of=request.user.username)

    return redirect(request.META.get('HTTP_REFERER'))


def remove_basket(request, slug):  # Удаляем товар из корзины
    basket_prod = Basket.objects.filter(user_of=request.user.username).get(slug=slug)
    basket_prod.delete()
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
    template_name = 'catalog/user_room.html'
    context_object_name = 'get'
    extra_context = {'title': 'Личный кабинет'}

    def get_queryset(self):
        queryset = Account.objects.get(username=self.request.user.username)
        return queryset


class EditUserProfile(ShopMixin, FormView):
    form_class = UserRoomForm
    template_name = 'catalog/edit_user_profile.html'
    extra_context = {'title': 'Редактировать профиль'}

    def form_valid(self, form):
        user_data = Account.objects.get(username=self.request.user.username)
        user_data.first_name = form.cleaned_data['first_name']
        user_data.last_name = form.cleaned_data['last_name']
        user_data.email = form.cleaned_data['email']
        user_data.image = form.cleaned_data['image']
        user_data.phone = form.cleaned_data['phone']
        user_data.address = form.cleaned_data['address']
        user_data.save()
        return redirect('user_room')

