from django.shortcuts import render
from web.form import DocForm
from .models import doc
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    documentation = doc.objects.all()
    return render(request, 'web/index.html', locals())


def add(request):
    form = DocForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        form = DocForm(request.POST)
        form.save()
        return HttpResponseRedirect('/')
    form = DocForm()
    return render(request, 'web/add.html', locals())


def edit(request, id_doc):
    idd = id_doc
    documentation = doc.objects.get(id=idd)
    form = DocForm(request.POST, instance=documentation)
    if request.method == 'POST' and form.is_valid():
        documentation.save()
        return HttpResponseRedirect('/')
    form = DocForm(instance=documentation)
    return render(request, 'web/edit.html', locals())


def view(request, id_doc):
    documentation = doc.objects.get(id=id_doc)
    return render(request, 'web/view.html', locals())
