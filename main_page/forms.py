from django import forms
from manager.models import UserReservation


class UserReservationForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                                'type': "text",
                                'name': "name",
                                'class': """form-control""",
                                'id': "name",
                                'placeholder': "Ваше ім'я",
                                'data - rule': "minlen:4",
                                'data - msg': "Please enter at least 4 chars",
                            }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                                'type': "email",
                                'class': "form-control",
                                'name': "email",
                                'id': "email",
                                'placeholder': "Ваш Email",
                                'data-rule': "email",
                                'data-msg': "Please enter a valid email"
                            }))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
                                'type': "text",
                                'class': "form-control",
                                'name': "phone",
                                'id': "phone",
                                'placeholder': "номер телефона (380**)",
                                'data-rule': "minlen:4",
                                'data-msg': "Please enter at least 4 chars"
                            }))
    date_reserve = forms.DateField(widget=forms.DateInput(attrs={
                                'type': "date",
                                'name': "date",
                                'class': "form-control",
                                'id': "date",
                                'placeholder': "Дата",
                                'data-rule': "minlen:4",
                                'data-msg': "Please enter at least 4 chars"
                            }))
    time_reserve = forms.TimeField(widget=forms.TimeInput(attrs={
                                'type': "time",
                                'class': "form-control",
                                'name': "time",
                                'id': "time",
                                'placeholder': "Час",
                                'data-rule': "minlen:4",
                                'data-msg': "Please enter at least 4 chars"
                            }))
    persons = forms.IntegerField(widget=forms.NumberInput(attrs={
                                'type': "number",
                                'class': "form-control",
                                'name': "people",
                                'id': "people",
                                'placeholder': "# Людей",
                                'data-rule': "minlen:1",
                                'data-msg': "Please enter at least 1 chars"
                            }))
    message = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={
                                'class': "form-control",
                                'name': "message",
                                'rows': "5",
                                'placeholder': "Повідомлення"
                            }))

    class Meta:
        model = UserReservation
        fields = ('name', 'email', 'phone', 'date_reserve', 'time_reserve', 'persons', 'message')
