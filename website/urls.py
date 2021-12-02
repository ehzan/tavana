from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/home/')),
    path('home/', views.home, name='home'),
    path('coaches/', views.coaches),
    path('contact/', views.contact),

    path('para/', views.para),
    path('tournaments/', views.tournaments),
    path('rating-system/', views.rating_system),

    path('files/<str:filename>', views.file_delivery, name='file')
]
