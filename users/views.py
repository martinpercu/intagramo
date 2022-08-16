""" This is the users view"""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required  #nor really needed because is not possible to arrive the view if you are not already logged


# Create your views here.

# Forms
from users.forms import ProfileForm, SignupForm

# def for an experimental django Middleware.... 

@login_required
def update_profile(request):
    """ 
    Update user profile .. atention!! experiment to use Middlewares    
    """
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.picture = data['picture']

            profile.save()
            print(form.cleaned_data)

            return redirect('feed')
    else:
        form = ProfileForm()


    return render(
        request = request,
        template_name = 'users/update_profile.html',
        context = {
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )


def login_view(request):
    """ Login view """

    # import pdb; pdb.set_trace()

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # We check in console if POST is working OK
        # print(username, password)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'The username and/or password not found'})
    return render(request, 'users/login.html')

@login_required #in normal use no need this decorator.---> You are in this 'post' page if you are already logged.
def logout_view(request):
    """ Logout view """

    logout(request)

    return render(request, 'users/login.html', {'messageLogout': 'You just logout.'})


def signup(request):
    """Signup View"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(
        request=request,
        template_name='users/signup.html',
        context={'form': form}
    )
        