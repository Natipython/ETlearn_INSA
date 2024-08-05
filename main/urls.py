from django.urls import path
from .views import *


urlpatterns = [
    path('', main, name='home'),
    path('courses', courses, name='courses'),
    path('contact', contact, name='contact'),
    path('login', login, name='login'),
    path('room/<str:course>', room, name='room')

]
