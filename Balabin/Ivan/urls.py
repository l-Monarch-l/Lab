from django.urls import path
from .views import name_view, groupe_view, age_view, common_view
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('name/', name_view, name='name'),
    path('groupe/', groupe_view, name='groupe'),
    path('age/', age_view, name='age'),
    path('common/', common_view, name='common'),
]
