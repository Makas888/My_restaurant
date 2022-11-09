from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationUserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', )

    def clean_password2(self):
        data = self.cleaned_data

        if data['password'] == data['password2']:
            return data['password2']

        raise forms.ValidationError('Паролі не співпадають')
