from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.paginator import Paginator
from .models import GeekModel
from .forms import GeeksForm



def create_view(request):
    context = {}

    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    
    context['form'] = form
    return render(request, template_name='CRUD/create_view.html', context=context)


def list_view(request):
    
    dados = GeekModel.objects.all()
    
    paginator = Paginator(GeekModel.objects.all(), 2)
    page = request.GET.get('page')
    pages = paginator.get_page(page)

    context = {
        'dados': dados,
        'pages': pages,
    }
    return render(request, template_name='CRUD/list_view.html', context=context)


def detail_view(request, id): 
    context ={}
    context["data"] = GeekModel.objects.get(id = id)
    return render(request, template_name="CRUD/detail_view.html", context=context)


def update_view(request, id):
    context = {}
    obj = get_object_or_404(GeekModel, id=id)

    form = GeeksForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/'+id)
    
    context['form'] = form
    return render(request, template_name='CRUD/update_view.html', context=context)


def delete_view(request, id):
    context = {}
    obj = get_object_or_404(GeekModel,id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, template_name='CRUD/delete_view.html', context=context)