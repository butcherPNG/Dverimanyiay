from myapp.models import *
from django import forms
from django.core.exceptions import ValidationError

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ('fullname', 'phone', 'address', 'date')

class AddDoorForm(forms.ModelForm):
    class Meta:
        model = Door
        fields = ('name', 'color', 'material', 'size', 'price', 'img')

class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-styling'}))
    password2 = forms.CharField(label="Повторить пароль", widget=forms.PasswordInput(attrs={'class': 'form-styling'}))

    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-styling'}))
    email = forms.EmailField(label="Почта", widget=forms.EmailInput(attrs={'class': 'form-styling'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user