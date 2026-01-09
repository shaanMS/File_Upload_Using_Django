

# Create your views here.

from django.shortcuts import render, redirect
from .forms import DocumentForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Document
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='30/h', method='GET', block=True)  # bahut important
@login_required(login_url = '/')  # jahan redirect karna hai wahan ka url daal diya - y decorator way hai warna bina decorator k is authenticated way bhi use kar sakte hai par wo more control deta hai logic par 
def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file-list')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})


@login_required(login_url='/')
def file_list(request):
    documents = Document.objects.all()
    return render(request, 'file_list.html', {'documents': documents})