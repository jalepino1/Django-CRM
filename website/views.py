from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
#request are request that are sent from interaction with the webpage and are sent to the backend to process them
def home(request):
    if request.method == "POST":

        # If POST is passed in our request, we will get the username and password from the post, and define it as variables.
        Username = request.POST['username']
        Password = request.POST['password']
        # This uses the django built-in authenticate 
        user = authenticate(request, username=Username, password=Password)
        if user is not None:
            login(request, user)
            messages.success(request, "Sign in successful")
            return redirect('home')
        else:
            messages.success(request, "Login unsuccessful")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')

def register_user(request):
    pass