from django import forms


class LoginForm(forms.Form):
    username    =forms.CharField(max_length=50,label="Kullanıcı Adı",required=True,widget=forms.TextInput(attrs={'placeholder': 'Kullanıcı adınızı giriniz'}))
    password=forms.CharField(label="Parola",widget=forms.PasswordInput(attrs={"placeholder":"Parolanınızı giriniz"}),required=True)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'
class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50,label="Kullanıcı Adı",required=True,widget=forms.TextInput(attrs={"placeholder":"Kullanıcı adınızı giriniz"}))
    email   =forms.CharField(max_length=100,label="E posta Adresi",required=True,widget=forms.TextInput(attrs={"placeholder":"E posta adresinizi giriniz"}))
    password=forms.CharField(max_length=100,label="Parola",required=True,widget=forms.PasswordInput(attrs={"placeholder":"Parolanınızı giriniz"}))
    confirm = forms.CharField(max_length=50, label="Parolayı Doğrula", required=True,widget=forms.PasswordInput(attrs={"placeholder":"Parolanınızı tekrar giriniz"}))

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'

    def clean(self):
        username = self.cleaned_data.get("username")
        mail = self.cleaned_data.get("mail")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar eşleşmiyor.")
        values = {
            "username": username,
            "mail": mail,
            "password": password
        }
        return values





