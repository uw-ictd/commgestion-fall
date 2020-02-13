from django.shortcuts import render

from web import public_view
from . import stats_view
from . import usuario_view
from . import profile_view


# Create your views here.
def home(request):
    gauge = public_view.generate_test_data()
    print(gauge)
    return render(request, 'home.html', context=gauge)


def net_stats(request):
    context = stats_view.generate_test_data()
    return render(request, 'stats.html', context=context)


def public_info(request):
    gauge = public_view.generate_test_data()
    print(gauge)
    return render(request, 'public_info.html', context=gauge)


def profile(request):
    subs = profile_view.generate_table()
    return render(request, 'profile.html', context=subs)


def usuario(request):
    context = usuario_view.generate_test_data()
    return render(request, 'usuario_pie.html', context=context)