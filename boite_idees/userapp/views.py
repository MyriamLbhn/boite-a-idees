from django.shortcuts import render, redirect
from userapp.forms import UserCreationFormCustom
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy


from .models import Idea, Voter
from .forms import IdeaForm

class SignupPage(CreateView):
    success_url = reverse_lazy('login')
    template_name = 'userapp/signup.html'
    form_class = UserCreationFormCustom

def home(request):

    ideas = Idea.objects.all()

    return render(request, 'userapp/home.html',{'liste_idee': ideas})

def login_view(request):
    return render(request, 'userapp/login.html')

def logout_view(request):
    return render(request, 'userapp/logout.html')

    
@login_required
def ajouter_idee(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.author = request.user
            idea.save()
            return redirect('home')
    else:
        form = IdeaForm()
    return render(request, 'userapp/ajouter_idee.html', {'form': form})

