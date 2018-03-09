from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings

# Create your views here.
def read_file(request):
    if request.method == 'POST':
        if request.FILES['file'] is not None:
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("aaa")
    else:
        return render(request, 'upload_form.html')

def handle_uploaded_file(f):
    full_filename = os.path.join(settings.BASE_DIR, 'upload\data', f.name)
    with open(full_filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)