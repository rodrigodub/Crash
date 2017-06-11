from django.shortcuts import render, get_object_or_404

# Create your views here.
def computer_home(request):
    return render(request, 'Computer/computer_home.html')