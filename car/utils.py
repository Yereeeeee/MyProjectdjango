from car.models import Category


class DataMixin:
    def context_data(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context["cats"] = cats
        return context
