from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
    return render(request, "home.html")
def name_view(request):
    return render(request, "name.html")
def groupe_view(request):
    return render(request, "groupe.html")
def age_view(request):
    return render(request, "age.html")
def common_view(request):
    return render(request, "common.html")