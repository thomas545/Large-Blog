from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.forms import UserRegisterForm , UserUpdateForm , ProfileUpdateForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request ,'Your Account Has Been Created! You Can Login Now!')
            return redirect('login')



    else:
        form = UserRegisterForm()
    return render(request,'registration/register.html' , {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST , instance=request.user)
        profile_form = ProfileUpdateForm(request.POST , request.FILES ,
                                        instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request ,'Your Account Has Been Updated!')
            return redirect('profile')


    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':user_form,
        'p_form':profile_form
    }


    return render(request,'registration/profile.html',context)
