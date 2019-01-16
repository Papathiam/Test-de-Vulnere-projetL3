from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
# from .models import InscriptionForm

# Create your views here.



def index(request):
    return render(request, 'account/index.html')

def register(request):
    if request.method == 'POST': 
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username , password=password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()

    context = {'form' : form}
   
    return render(request, 'registration/register.html', context)


# def logout(request):
#     if request.method == 'POST':
#         logout(request)
#         return  redirect('index')

# def Inscription(request):
#     form = InscriptionForm(request.POST)
#     if form.is_valid():
#         inscri = InscriptionForm()

#         inscri.username = form.cleaned_data["username"]
#         inscri.email = form.cleaned_data["email"]
#         inscri.password1 = form.cleaned_data["password1"]
#         inscri.telephone = form.cleaned_data["telephone"]

#         inscri.save()

#     return render(request, 'articles/inscription.html', {'form': form})
