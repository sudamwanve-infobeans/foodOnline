from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.contrib import messages
# Create your views here.

def registerUser(request):
    if request.method == 'POST':
        print(request.POST)  # Debugging print statement
        form = UserForm(request.POST)  # Instantiate the form with POST data
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)  # Save the user if the form is valid
            user.set_password(password)
            user.role = User.CUSTOMER
            user.save()
            messages.error(request, 'User registerd Successfully')
            return redirect('registerUser')  # Redirect to a success page, e.g., 'login'
        else:
            context = {'form': form}
            return render(request, 'accounts/registerUser.html', context)  # Re-render with errors
    else:
        form = UserForm()  # Instantiate an empty form
        context = {'form': form}
        return render(request, 'accounts/registerUser.html', context) 
