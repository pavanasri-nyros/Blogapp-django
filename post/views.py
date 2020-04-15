from django.shortcuts import render

# Create your views here.
def post(request):
    context = {
        "name":"pavana"

    }
    return render(request,'admin.html', context)