"""Here we create fonctions for login and registration"""

from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
    )

User = get_user_model()


class UserLoginForm(forms.Form):
    """this is form for login and run session"""

    username = forms.CharField(label='Pseudo', 
                    widget=forms.TextInput(attrs={'placeholder': 'Pseudo'}))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               label='Password')


    def clean(self, *args, **kwargs):
        """cleanning entrance"""

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('logins erronés')

            if not user.check_password(password):
                forms.ValidationError('password erronés')

        return super(UserLoginForm, self).clean(*args, **kwargs)              


class UserRegisterForm(forms.ModelForm):
    """This is form for register"""



    username = forms.CharField(label='Pseudo', 
                    widget=forms.TextInput(attrs={'placeholder': 'Pseudo'}))
    
    email = forms.EmailField(label='Email', 
                    widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    
    email2 = forms.EmailField(label='Confirmer Email', 
                    widget=forms.TextInput(attrs={'placeholder': 'Confirmer Email'}))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               label='Password')
                               




    class Meta:
        """We call username email and password from meta class"""

        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
            ]

    def clean(self, *args, **kwargs):
        """We cleanning it"""

        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("pas les meme email")

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "email existe deja")

        return super(UserRegisterForm, self).clean(*args, **kwargs)
