from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserLoginForm, RegistrationForm

import pyrebase as firebase

firebaseConfig = {
    "apiKey": "AIzaSyAGy2iRgkPP_PVOFYiAfESLgYb_eLrT6eU",
    "authDomain": "django-3aca5.firebaseapp.com",
    "projectId": "django-3aca5",
    "storageBucket": "django-3aca5.appspot.com",
    "messagingSenderId": "212972838840",
    "appId": "1:212972838840:web:ff68185a3545e5628e394d",
    "measurementId": "G-WGEYCC1HFJ",
    "databaseURL": "https://django-3aca5-default-rtdb.firebaseio.com",

}

app = firebase.initialize_app(firebaseConfig)
authenticate_user = app.auth()
user_db = app.database()


# class UserLogin(LoginView):
#     authentication_form = UserLoginForm
#     template_name = 'users/login.html'

def login_view(request):
    form = UserLoginForm()
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = authenticate_user.sign_in_with_email_and_password(email, password)
            
            # data = {"name": "sarahj_KE"}
            # verify_user = user_db.child("users").push(data, user["IdToken"])
            # print(f'User: {user}')
            
            if user is not None:
                return redirect('homepage')

        except:
            messages.error(request, 'INVALID CREDENTIALS! Username and password may be case-sensitive.')
            return redirect('login')

        print(f'User: {user}')
    context = {'form': form}
    return render(request, "users/login.html", context)



def signup_view(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form_info = form.save(commit=False)
            new_user = authenticate_user.create_user_with_email_and_password(form_info.email, form_info.password)
            print('New User: ', new_user)
            
            uid = new_user["localId"]
            data = {"name": form_info.username, "status": "1"}

            user_db.child("users").child(uid).child("details").set(data)
            
            messages.success(request, "You have successfully created an account!")
            return redirect('login')

    context = {'signup_form': form}
    return render(request, 'users/signup.html', context)

def homepage_view(request):

    return render(request, 'users/homepage.html')


class LogoutUser(LogoutView):
    template_name = 'users/logout.html'