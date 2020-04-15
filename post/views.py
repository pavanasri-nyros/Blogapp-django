from django.shortcuts import render

# Create your views here.
def post(request):
    context = {
        "name":" first page"

    }
    return render(request,'admin.html', context)