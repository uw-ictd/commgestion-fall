from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime
from datetime import timedelta

from web import public_view
from web.forms import UserSearchTimeForm, ModalForm

from . import network_stats_view
from . import network_users_view
from . import profiles_view


def public_info(request):
    gauge = public_view.generate_test_data()
    return render(request, 'public_info.html', context=gauge)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def network_stats(request):
    context = network_stats_view.generate_test_data()
    return render(request, 'network_stats.html', context=context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def profiles(request):
    if request.method == 'POST':
        form = ModalForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phoneNumber = form.cleaned_data['phoneNumber']
            display = form.cleaned_data['display']
            isLocal = form.cleaned_data['localNonLocal']
            role = form.cleaned_data['role']
            connected = form.cleaned_data['connected']
            activeStatus = form.cleaned_data['active']
            print(name, phoneNumber, display, isLocal, role, connected, activeStatus)
    
    context = profiles_view.generate_table()
    context['form'] = ModalForm()
    return render(request, 'profiles.html', context=context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def network_users(request):
    if request.method == 'POST':
        form = UserSearchTimeForm(request.POST)
        if form.is_valid():
            from_date = form.cleaned_data['from_date']
            to_date = form.cleaned_data['to_date']
    else:
        from_date = datetime.now() - timedelta(days=7)
        to_date = datetime.now()
    context = network_users_view.generate_test_data(from_date=from_date, to_date=to_date)
    context['form'] = UserSearchTimeForm()
    return render(request, 'network_users.html', context=context)
