from django.shortcuts import render
from django.http import HttpResponse
# from AppTwo.models import User
from AppTwo.forms import NewUser

# Create your views here.
def index(request):
    my_dict = {'insert_me': 'Go to /users to find more!'}
    return render(request, 'AppTwo/index.html', context=my_dict)

def user(request):
    form = NewUser()

    if (request.method == 'POST'):
        form = NewUser(request.POST)

        if (form.is_valid()):
            form.save(commit=True)
            return index(request)

        else:
            print ('ERROR FORM INVALID')

    return render(request, 'AppTwo/users.html', {'form': form})
