from django.shortcuts import render
from .models import Person
from .forms import Person_Create


# Create your views here.

def person_view(request):
    persons = Person.objects.all()
    return render(request, 'person/persons.html', context={'persons': persons})


def person_detail_view(request, name):
    person = Person.objects.get(name__iexact=name)
    return render(request, 'person/person_detail.html', context={'person': person})


def person_create(request):
    person_form = Person_Create(request.POST or None)
    if person_form.is_valid():
        person_form.save()
        person_form = Person_Create()
    return render(request, 'person/person_create.html', context={'person_form': person_form})
