from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.EmailBackEnd import EmailBackEnd
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def login_view(request):
    return render(request, 'login.html')

def check(request):

    if request.method == 'POST':
        print("called")
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user using custom EmailBackEnd
        user = EmailBackEnd.authenticate(request, username=email, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            user.send_otp()
            user.save()
            
            return render(request, 'verify.html')
        else:
            return redirect('login_page')
    
    return redirect('login_page')


def verify(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        user = request.user

        if user and int(user.otp) == int(entered_otp):
            print(user.otp)
            user.otp = 0  # Clear OTP after successful verification
            user.save()
            return render(request, 'dashboard.html')  # Redirect to dashboard or desired page
    
    print('failed')
    return redirect('login_page')