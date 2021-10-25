from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username    =forms.CharField(max_length=50,label="Kullanıcı Adı",required=True,widget=forms.TextInput(attrs={'placeholder': 'Kullanıcı adınızı giriniz'}))
    password=forms.CharField(label="Parola",widget=forms.PasswordInput(attrs={"placeholder":"Parolanınızı giriniz"}),required=True)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'
class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50,label="Kullanıcı Adı",required=True,widget=forms.TextInput(attrs={"placeholder":"Kullanıcı adınızı giriniz","class":"form-control form-control-lg"}))
    email   =forms.CharField(max_length=100,label="E posta Adresi",required=True,widget=forms.TextInput(attrs={"placeholder":"E posta adresinizi giriniz","class":"form-control form-control-lg"}))
    password=forms.CharField(max_length=100,label="Parola",required=True,widget=forms.PasswordInput(attrs={"placeholder":"Parolanınızı giriniz","class":"form-control form-control-lg"}))
    confirm = forms.CharField(max_length=50, label="Parolayı Doğrula", required=True,widget=forms.PasswordInput(attrs={"placeholder":"Parolanınızı tekrar giriniz","class":"form-control form-control-lg"}))
    accept  =forms.BooleanField(widget=forms.CheckboxInput(attrs={"class":"form-check-input me-2"}),label="Kullanım koşullarını okudum ve kabul ediyorum")


    def clean(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        if password and confirm and password != confirm:
            raise ValidationError("Parolalar eşleşmiyor.")
        values = {
            "username": username,
            "email": email,
            "password": password
        }
        return values





