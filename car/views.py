from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView
from django.views.generic.list import MultipleObjectMixin

from car.forms import RegisterForm
from car.models import Category, Car
from car.utils import DataMixin


# Create your views here.

def myHandler404(request, exception):
    return render(request, '404page.html', status=404)


def myHandler500(exception):
    return render(template_name='404page.html', status=500)


def index(request):
    return render(request, template_name='car/index.html')


class IndexView(DataMixin, TemplateView):
    template_name = "car/index.html"

    def get_context_data(self, **kwargs):
        return self.context_data(title="index")


class CategoryCars(DataMixin, DetailView, MultipleObjectMixin):
    template_name = 'car/category_cars.html'
    model = Category
    slug_field = "url"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        object_list = Car.objects.filter(category=self.get_object())
        context = super(CategoryCars, self).get_context_data(object_list=object_list, **kwargs)
        mixin = self.context_data(title="category")
        return dict(list(context.items()) + list(mixin.items()))


class Login(DataMixin, LoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('index')
    template_name = 'car/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.context_data(title="login page")
        return dict(list(context.items()) + list(mixin.items()))


class RegisterView(DataMixin, CreateView):
    form_class = RegisterForm
    template_name = 'car/register.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.context_data(title="login page")
        return dict(list(context.items()) + list(mixin.items()))


def carShow(request, slug, url):
    categories = Category.objects.all()
    car = Car.objects.get(url=url)
    context = {"cats": categories, "title": "show car", "car": car}
    return render(request, template_name="car/car_details.html", context=context)


@login_required
def sign_out(request):
    logout(request)
    return redirect('/')
