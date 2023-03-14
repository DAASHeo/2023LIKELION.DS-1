from django import forms
from .models import babyLion

class ViewBabylionForm(forms.ModelForm):
    class Meta:
        model = babyLion
        fields = '__all__'

        labels = {
            'name' : '',
            'phone_num' : '',
            'email' : ''
        }

        widgets = {
            "name": forms.TextInput(attrs={
                'placeholder': '이름',
            }),
            "phone_num": forms.TextInput(attrs={
                'placeholder': '전화번호',
            }),
            "email": forms.TextInput(attrs={
                'placeholder': '이메일',
            }), 
        }