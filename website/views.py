from django.shortcuts import render
from django.http import HttpResponse
from website.models import *
import mimetypes

# Create your views here.


def home(request):
    highlights = Highlight.objects.filter(visible=True)
    print(highlights)
    return render(request, 'home.html', context={'highlights': highlights}, )


def coaches(request):
    categories = Coach.objects.all().values_list(
        'category', flat=True).distinct().order_by('order')
    toc = {category: Coach.objects.filter(category=category).values('english_name', 'persian_name')
           for category in categories}
    coaches = Coach.objects.all()

    return render(request, 'coaches.html', context={'toc': toc, 'coaches': coaches}, )


def contact(request):
    return render(request, 'contact.html')


def courses(request):
    semesters = Semester.objects.filter(active=True)
    courses = Course.objects.filter(semester__active=True)
    return render(request, 'courses.html', context={'semesters': semesters, 'courses': courses}, )


def free_session(request):
    semester = Semester.objects.filter(active=True).first()
    print(semester)
    freeSession = Course.objects.get(semester=semester, title='سانس آزاد')
    freeSession.description = freeSession.description.replace(':', ' ')
    return render(request, 'free-session.html', context={'freeSession': freeSession}, )


def para(request):
    return render(request, 'para.html')


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
