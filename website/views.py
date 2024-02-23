from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .forms import AddRecordForm
from .models import Record
# Create your views here.
#request are request that are sent from interaction with the webpage and are sent to the backend to process them
def home(request):
    records = Record.objects.all()
    print(records)
    # Checks to see if they are logging in
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
        return render(request, 'home.html', {'records' : records})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')

# request.method is looking for a post from the url request 
# register, if there is a post, it will define form as signupform(request.post) which gets the post from user and sends the sign up form

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully created an account.")
            return redirect('home')
            return render(request, 'register.html', {'form' : form })
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form' : form })
    
    return render(request, 'register.html')


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record' : customer_record })
    else:
        messages.success(request, "User not logged in.")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Customer record has successfully been deleted.")
        return redirect('home')
    else:
        messages.success(request, "User not logged in.")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":   
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added")
                return redirect('home')
        return render(request, 'add_record.html', {'form' : form})
    else:
        messages.success(request, "User not logged in")
        return redirect('home')