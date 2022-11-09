from django.shortcuts import render
from .forms import RegistrationUserForm


def login_view(request):
    pass


def registration_view(request):
    form = RegistrationUserForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()

        return render(request, 'registration_done.html', context={'user': new_user})
    return render(request, 'registration.html', context={'form': form})


def logout_view(request):
    pass