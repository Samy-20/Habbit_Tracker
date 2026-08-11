from django.shortcuts import render, redirect, get_object_or_404
from . models import habbit, HabbitLog
from . forms import HabbitForm
from datetime import date

# Create your views here.

def home(request):
    habbits = habbit.objects.all().order_by("created_at")
    return render(request, "home.html", {
        "habbits":habbits
    })
    
def add_habbit(request):
    if request.method == "POST":
        form = HabbitForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect(home)
    
    else:
        form = HabbitForm()
        
    return render(request, "add_habbit.html", {
        "form" : form
    })
    
def update_habbit(request, id):
    habit = get_object_or_404(habbit, id=id)
    
    if request.method == "POST":
        form = HabbitForm(request.POST, instance=habit)
    
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form =  HabbitForm(instance=habit)
        
    return render(request, "update_habbit.html", {
        "form": form
    })
    
def delete_habbit(request, id):
    habit = get_object_or_404(habbit, id=id)
    
    habit.delete()
    
    return redirect('home')   

def complete_today(request, id):

    habit = get_object_or_404(habbit, id=id)

    today = date.today()

    already_completed = HabbitLog.objects.filter(
        habit=habit,
        completed_on=today
    ).exists()

    if not already_completed:
        HabbitLog.objects.create(
            habit=habit
        )

    return redirect("home")