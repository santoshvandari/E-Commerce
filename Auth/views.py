from django.shortcuts import render,redirect

# Create your views here.
def log_in(request):
    # checck user is authenticated or not 
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method=='POST':
        username=request.POST.get('username').strip()
        password=request.POST.get('password')
        if username and password:
            return render(request, 'Auth/login.html', {'error': '* Please fill all the fields'})
        print(username,password)
        # return redirect('/home')
    return render(request, 'Auth/login.html')


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method=='POST':
        firstname=request.POST.get('firstname').strip()
        lastname=request.POST.get('lastname').strip()
        username=request.POST.get('username').strip()
        email=request.POST.get('email').strip()
        password=request.POST.get('password')
        if firstname and lastname and username and email and password:
            return render(request, 'Auth/signup.html', {'error': '* Please fill all the fields'})
        print(firstname,lastname,username,email,password)
        
    
    return render(request, 'Auth/signup.html')
