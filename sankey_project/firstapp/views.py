from django.shortcuts import render

# Create your views here.
def all_index(request):
    return render(request,'firstapp/all_index.htm')