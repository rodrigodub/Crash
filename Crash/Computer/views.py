from django.shortcuts import render, get_object_or_404
from .models import CCTransistor
from .forms import TransistorForm

# Create your views here.
def computer_home(request):
    return render(request, 'Computer/computer_home.html')


def transistor_list(request):
    transistors = CCTransistor.objects.order_by('-id')
    # POST
    if request.method == 'POST':
        transForm = TransistorForm(request.POST)
    # TO BE CONTINUED
