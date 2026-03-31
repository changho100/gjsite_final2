from django.shortcuts import render
from .models import Visitor


# Create your views here.
def index(request):
    try :
        visitor = Visitor.objects.get(pk=1)
        visitor.total_count += 1
    except:
        visitor = Visitor()
        visitor.total_count = 1

    visitor.save()

    return render(request, 'mpage/index.html')