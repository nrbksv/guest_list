from django.shortcuts import render, redirect, get_object_or_404

from check_in.models import Guest
from check_in.forms import GuestForm


def guest_list_view(request):
    form = GuestForm()
    guests = Guest.objects.filter(status='active').order_by('-create_date')
    return render(request, 'main_page.html', {'guests': guests, 'form': form})


def guest_add_view(request):
    form = GuestForm(data=request.POST)
    if form.is_valid():
        Guest.objects.create(
            name=form.cleaned_data.get('name'),
            e_mail=form.cleaned_data.get('e_mail'),
            reg_info=form.cleaned_data.get('reg_info')
        )
        return redirect('guest-list')
    return render(request, 'main_page.html', {'form': form})


def guest_data_update(request, pk):
    guest = get_object_or_404(Guest, id=pk)
    guests = Guest.objects.filter(status='active').order_by('-create_date')
    if request.method == 'GET':
        form = GuestForm(initial={
            'name': guest.name,
            'e_mail': guest.e_mail,
            'reg_info': guest.reg_info,
        })
        return render(request, 'main_page.html', {'guests': guests, 'form': form, 'guest': guest, 'update': 'ok'})
    elif request.method == 'POST':
        form = GuestForm(data=request.POST)
        if form.is_valid():
            guest.name = form.cleaned_data.get('name')
            guest.e_mail = form.cleaned_data.get('e_mail')
            guest.reg_info = form.cleaned_data.get('reg_info')
            guest.save()

            return redirect('guest-list')
        return render(request, {'guests': guests, 'form': form, 'guest': guest})

