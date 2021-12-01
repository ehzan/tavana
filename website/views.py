from django.shortcuts import render
from django.http import HttpResponse
from website.models import *
import mimetypes

# Create your views here.


def home(request):
    return render(request, 'template.html')


def coaches(request):
    categories = Coach.objects.all().values_list(
        'category', flat=True).distinct().order_by('order')
    toc = {category: Coach.objects.filter(category=category).values('english_name', 'persian_name')
           for category in categories}
    coaches = Coach.objects.all()

    return render(request, 'coaches.html', context={'toc': toc, 'coaches': coaches})


def contact(request):
    return render(request, 'contact.html')


def tournaments(request):
    return render(request, 'tournaments.html')


def rating_system(request):
    return render(request, 'rating-system.html')


def file_delivery(request, filename):
    filetype, fuck = mimetypes.guess_type('./website/files/'+filename)
    print(filetype)
    try:
        with open('./website/files/'+filename, 'rb') as f:
            resp = HttpResponse(f.read(), filetype)
        # response['Content-Type'] = filetype
        return resp
    except:
        return HttpResponse('sorry')
