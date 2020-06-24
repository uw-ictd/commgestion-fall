from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime
from datetime import timedelta

from web.forms import UserSearchTimeForm, ModalForm

from . import (_api, _network_stats, _network_users, _profiles, _public)


# Redefine api as a publicly exportable top level object in the package.
api = _api


def public_info(request):
    return render(request,
                  'public_info.html',
                  context=_public.generate_context(),
                  )


@login_required
@user_passes_test(lambda u: u.is_superuser)
def network_stats(request):
    context = _network_stats.generate_test_data()
    return render(request, 'network_stats.html', context=context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def profiles(request):
    context = _profiles.generate_table()
    context['form'] = ModalForm()
    if request.method == 'POST':
        form = ModalForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            # phone = form.cleaned_data['phone']
            imsi = form.cleaned_data['imsi']
            # guti = form.cleaned_data['guti']
            # resident_status = form.cleaned_data['resident_status']
            # role = form.cleaned_data['role']
            # connection_status = form.cleaned_data['connection_status']
            # password = form.cleaned_data['password']
        else:
            context['form'] = form
            print(form.errors)
            print('invalid')
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
    context = _network_users.generate_context(from_date=from_date, to_date=to_date)
    context['form'] = UserSearchTimeForm()
    return render(request, 'network_users.html', context=context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def addForm(request):
    if request.method == 'POST':
        form = ModalForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            imsi = form.cleaned_data['imsi']
            # guti = form.cleaned_data['guti']
            # phone = form.cleaned_data['phone']
            # resident_status = form.cleaned_data['resident_status']
            role = form.cleaned_data['role']
            rate_limit = form.cleaned_data['rate_limit']
            connection_status = form.cleaned_data['connection_status']
            context = network_users.lookup_user(imsi)