from django.shortcuts import render
from django.http import HttpResponse
from website.models import *

# Create your views here.


def main(request):
    return render(request, 'template.html')


def read_CV(person):
    filepath = './website/content/CV/'+person+'.txt'
    print(filepath)
    try:
        with open(filepath, 'r', encoding='UTF-8') as f:
            cv = f.read()
    except:
        print("Could not find the resaults file.")
        return None
    return cv


def coaches(request):
    categories = Coach.objects.all().values_list(
        'category', flat=True).distinct().order_by('order')
    toc = {category: Coach.objects.filter(category=category).values('english_name', 'persian_name')
           for category in categories}
    coaches = Coach.objects.all()

    return render(request, 'coaches.html', context={'toc': toc, 'coaches': coaches})
