from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Booking,FeadBack

class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name','last_name','phone']
        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'نام خود را وارد کنید'
            }),
            'last_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'نام خانوادگی خود را وارد کنید'
            }),
            'phone':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'شماره تماس خود را وارد کنید'
            }),
        }
        

class FeadBackForm(forms.ModelForm):
    class Meta:
        model = FeadBack
        fields = ['fullname','description']
        widgets = {
            'fullname':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'نام و نام‌خانوادگی خود را وارد کنید'
            }),
            'description':forms.Textarea(attrs={
                'class':'form-control'
            })
        }