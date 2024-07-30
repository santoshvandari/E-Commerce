from django.shortcuts import render,redirect

# Create your views here.
def Home(request):
    # if request.user.is_authenticated:
    #     return redirect('/login')
    return render(request,'Store/home.html')