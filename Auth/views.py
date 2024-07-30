from django.shortcuts import render,redirect

# Create your views here.
def log_in(request):
    # checck user is authenticated or not 
    if request.user.is_authenticated:
        return redirect('/home')
    return render(request, 'login.html')


def sign_up(request):
    return render(request, 'signup.html')
