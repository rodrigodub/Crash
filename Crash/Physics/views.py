from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import HTVector, HTExercise, HTData
from .forms import VectorForm, ExerciseForm, ExerciseDataForm


# Create your views here.
def home(request):
    # return HttpResponse('Physics Home Page')
    return render(request, 'Physics/home.html')


# vector list
def vector_list(request):
    vlist = HTVector.objects.order_by('-id')

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        vform = VectorForm(request.POST)
        # check whether it's valid:
        if vform.is_valid():
            # process the data in form.cleaned_data as required
            vform.save(commit=True)
            # take the last vector and recalculate
            a = HTVector.objects.all()[len(HTVector.objects.all())-1]
            a.calculate()
            a.save()
            # redirect to a new URL:
            return render(request, 'Physics/vectors.html', {'vector_list': vlist, 'vector_form': VectorForm()})
    # if a GET (or any other method) we'll create a blank form
    else:
        vform = VectorForm()
    context = {'vector_list': vlist, 'vector_form': vform}
    return render(request, 'Physics/vectors.html', context)


# individual vector
def vector_num(request, id):
    vector = get_object_or_404(HTVector, pk=id)
    picture = vector.drawVector()
    return render(request, 'Physics/vector_detail.html', {'vector': vector})


# exercises list
def exercise_list(request):
    elist = HTExercise.objects.order_by('-id')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        eform = ExerciseForm(request.POST)
        # check whether it's valid:
        if eform.is_valid():
            # process the data in form.cleaned_data as required
            eform.save(commit=True)
            # redirect to a new URL:
            return render(request, 'Physics/exercise.html', {'exercise_list': elist, 'exercise_form': ExerciseForm()})
    # if this is a GET (or any other method) we'll create a blank form
    else:
        eform = ExerciseForm()
    context = {'exercise_list': elist, 'exercise_form': eform}
    return render(request, 'Physics/exercise.html', context)


# individual exercise
def exercise_num(request, id):
    exercise = get_object_or_404(HTExercise, pk=id)
    datalist = HTData.objects.filter(container_id=id)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        dataform = ExerciseDataForm(request.POST)
        # check whether it's valid:
        if dataform.is_valid():
            # process the data in form.cleaned_data as required
            dataform.save(commit=True)
            # redirect to a new URL:
            return render(request, 'Physics/exercise_details.html', {'exercise': exercise, 'datalist': datalist, 'dataform': ExerciseDataForm(initial={'container': exercise})})
    # if this is a GET (or any other method) we'll create a blank form
    else:
        dataform = ExerciseDataForm(initial={'container': exercise})
    return render(request, 'Physics/exercise_details.html', {'exercise': exercise, 'datalist': datalist, 'dataform': dataform})