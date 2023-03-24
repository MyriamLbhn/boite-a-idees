from django.shortcuts import render, redirect, get_object_or_404
from userapp.forms import UserCreationFormCustom
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.db.models import Sum
from django.contrib import messages
from django.db.models import Sum

from .models import Idea, Voter
from .forms import IdeaForm

class SignupPage(CreateView):
    success_url = reverse_lazy('login')
    template_name = 'userapp/signup.html'
    form_class = UserCreationFormCustom


@login_required
def home(request):
    liste_idee = Idea.objects.all()
    for idee in liste_idee:
        idee.total_votes = Voter.objects.filter(idea=idee).aggregate(Sum('vote'))['vote__sum']
    context = {'liste_idee': liste_idee}
    if request.method == 'POST':
        vote_value = int(request.POST.get('vote_value'))
        idea_id = int(request.POST.get('idea_id'))
        idea = get_object_or_404(Idea, pk=idea_id)
        voter, created = Voter.objects.get_or_create(voter=request.user, idea=idea)
        if created:
            voter.vote = vote_value
            voter.save()
        elif voter.vote == vote_value:
            voter.delete()
        else:
            voter.vote = vote_value
            voter.save()
        return redirect('userapp/home')
    return render(request, 'userapp/home.html', context)


@login_required
def ajouter_idee(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            nouvelle_idee = form.save(commit=False)
            nouvelle_idee.author = request.user
            nouvelle_idee.save()
            return redirect('home')
    else:
        form = IdeaForm()
    context = {'form': form}
    return render(request, 'userapp/ajouter_idee.html', context)

