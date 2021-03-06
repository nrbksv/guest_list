from django.shortcuts import render, redirect

from check_in.models import Guest
from check_in.forms import GuestForm


def guest_list_view(request):
    form = GuestForm()
    guests = Guest.objects.filter(status='active').order_by('-create_date')
    return render(request, 'main_page.html', {'guests': guests, 'form': form})


def guest_add_view(request):
    form = GuestForm(data=request.POST)
    if form.is_valid():
        guest = Guest.objects.create(
            name=form.cleaned_data.get('name'),
            e_mail=form.cleaned_data.get('e_mail'),
            reg_info=form.cleaned_data.get('reg_info')
        )
        return redirect('guest-list')
    return render(request, 'guest_add.html', {'form': form})

