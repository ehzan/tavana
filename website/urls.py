from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.home),

    path('about/', views.about),
    path('coaches/', views.coaches),
    path('contact/', views.contact),

    path('courses/', views.courses),
    path('free-session/', views.page, name='free-session'),
    path('para-tabletennis/', views.page, name='para-tabletennis'),
    path('tournaments/', views.tournaments),
    path('rating-system/', views.page, name='rating-system'),

    path('news/', views.news),

    path('files/<str:filename>', views.file_delivery, name='file'),
]
