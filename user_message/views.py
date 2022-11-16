from django.shortcuts import render, redirect
from .models import UserMessage
from django.contrib.auth.decorators import login_required, user_passes_test


def is_manager(user):
    return user.groups.filter(name='Менеджер').exists()


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def message_list(request):
    messages = UserMessage.objects.filter(archived=False)
    return render(request, 'user_message_list.html', context={'user_message_list': messages})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def add_archive(request, pk):
    UserMessage.objects.filter(pk=pk).update(archived=True)
    return redirect('user_message:message_list')
