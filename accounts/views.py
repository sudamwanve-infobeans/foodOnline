from django.shortcuts import render, redirect
from .forms import UserForm
from vendor.forms import VendorForm
from .models import User,UserProfile
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
            messages.success(request, 'User registerd Successfully')
            return redirect('registerUser')  # Redirect to a success page, e.g., 'login'
        else:
            context = {'form': form}
            return render(request, 'accounts/registerUser.html', context)  # Re-render with errors
    else:
        form = UserForm()  # Instantiate an empty form
        context = {'form': form}
        return render(request, 'accounts/registerUser.html', context) 


def registerVendor(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        v_form = VendorForm(request.POST,request.FILES)
        if form.is_valid() and v_form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                phone_number=phone_number,
                email=email,
                password = password
                )
            user.role = User.VENDOR
            user.save()
            vendor =v_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            messages.success(request, "Your account has been registered successfully! Please wait for the approval.")
            return redirect('registerVendor')
        else:
            print("Invalid Form")
            print(form.errors)
    else:
        form = UserForm()
        v_form = VendorForm()
        context = {
            'form' : form,
            'v_form' : v_form
        }
        return render(request, 'accounts/registervendor.html', context) 