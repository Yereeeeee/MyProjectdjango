from django.shortcuts import render


# Create your views here.

def myHandler404(request, exception):
    return render(request, '404page.html', status=404)


def myHandler500(request, exception):
    return render(request, template_name='404page.html', status=500)
