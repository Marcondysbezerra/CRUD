from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import GeekModel
from .forms import GeeksForm


# Create your views here.

def create_view(request):
    context = {}

    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    
    context['form'] = form
    return render(request, template_name='create_view.html', context=context)


def list_view(request):
    context = {}
    context['dataset'] = GeekModel.objects.all()
    return render(request, template_name='list_view.html', context=context)


# pass id attribute from urls
def detail_view(request, id): 
    context ={}
    context["data"] = GeekModel.objects.get(id = id)
    return render(request, "detail_view.html", context)

def update_view(request, id):
    context = {}
    obj = get_object_or_404(GeekModel, id=id)

    form = GeeksForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/'+id)
    
    context['form'] = form
    return render(request, template_name='update_view.html', context=context)


def delete_view(request, id):
    context = {}
    obj = GeekModel.objects.get(id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, template_name='delete_view.html', context=context)