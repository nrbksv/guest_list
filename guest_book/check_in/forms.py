from django.forms import ModelForm, TextInput, Textarea, EmailInput
from django import forms

from check_in.models import Guest


class GuestForm(ModelForm):

    class Meta:
        model = Guest
        fields = ['name', 'e_mail', 'reg_info']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control'
            }),
            'e_mail': EmailInput(attrs={
                'class': 'form-control'
            }),
            'reg_info': Textarea(attrs={
                'class': 'form-control'
            }),
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50)
