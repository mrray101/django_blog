from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method != 'POST':
        form = UserRegisterForm()
    else:
        form = UserRegisterForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user) # login() takes a request and user object
            return redirect('blog:home')

    context = {'form': form}
    return render(request, 'user/register.html', context)


@login_required
def profile(request):
    return render(request, 'user/profile.html')

