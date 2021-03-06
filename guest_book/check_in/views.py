from django.shortcuts import render

from check_in.models import Guest


def guest_list_view(request):
    guests = Guest.objects.all().order_by('-create_date')
    return render(request, 'main_page.html', {'guests': guests})
