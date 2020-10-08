from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm

def register(request):

    if request.method  == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Votre compte a été créé avec succès {username} avec adresse {email}! Vous pouvez maintenant vous connecter')
            return redirect('login')

    else:

        form = UserRegisterForm()
    return render(request, 'register/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'register/profile.html')


#OPTIONS of messages that pops up once after specific action
#messages.debug
#messages.info
#messages.success
#messages.warning
#messages.error