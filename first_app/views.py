from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.


# ---------------------------------


def home(req):
    return render(req, 'home.html')



# ---------------------------------


def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = forms.RegisterForm(request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                messages.success(request, f"Account for '{user_name}' created successfully!")
                form.save(commit = True)
                print(form.cleaned_data)
                return redirect("home")
                
        else:
            form = forms.RegisterForm()
            
        return render(request, 'signup.html', {'form' : form})
    else:
        return redirect("profile")


# ---------------------------------

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                
                user = authenticate(username = name, password = user_pass) # check kortechi user database e ache kina!!
                if user is not None:
                    login(request, user)
                    return redirect("profile") # profile page e redirect korbe
        
        else:   
            form = AuthenticationForm()
            
        return render(request, "login.html", {'form' : form})
    
    else:
        return redirect("profile")



# -------------------------------


def user_profile(request):
    # if req.user.is_authenticated:  
    #     return render(req, 'profile.html', {'user' : req.user})   
    # else:
    #     return redirect("user_login")   
    if request.user.is_authenticated:
        if request.method == "POST":
            form = forms.ChangeUserData(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request, "Account updated successfully!")
                form.save(commit = True)
                # print(form.cleaned_data)
                # return redirect("profile")              
        else:
            form = forms.ChangeUserData(instance = request.user)
            
        return render(request, 'profile.html', {'form' : form})
    else:
        return redirect("user_login")
      
            
            
# --------------------------------



def user_logout(req):
    logout(req)
    return redirect("user_login")


            
# --------------------------------
            
        
def pass_change(req):
    if req.user.is_authenticated:
        if req.method == "POST":
            form = PasswordChangeForm(user= req.user, data = req.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(req, form.user) # password update korbe
                return redirect("profile")
        else:
            form = PasswordChangeForm(user = req.user)
        
        return render(req, 'pass_change.html', {"form" : form})
    else:
        return redirect("user_login")
    
    

# --------------------------------

            
        
def pass_change_2(req):
    if req.user.is_authenticated:
        if req.method == "POST":
            form = SetPasswordForm(user= req.user, data = req.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(req, form.user) # password update korbe
                return redirect("profile")
        else:
            form = SetPasswordForm(user = req.user)
        
        return render(req, 'pass_change.html', {"form" : form})
    else:
        return redirect("user_login")
    

# ---------------------------------


# def change_user_Data(request):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             form = forms.ChangeUserData(request.POST, instance = request.user)
#             if form.is_valid():
#                 messages.success(request, "Account updated successfully!")
#                 form.save(commit = True)
#                 print(form.cleaned_data)
#                 # return redirect("profile")
                
#         else:
#             form = forms.ChangeUserData()
            
#         return render(request, 'profile.html', {'form' : form})
#     else:
#         return redirect("user_login")

