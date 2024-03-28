from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.Forms import SnippetForm

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == "GET": # получаем чистую форму для заполнения
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
            }
        return render(request, 'pages/add_snippet.html', context)
    
    if request.method == "POST": # создаем новый сниппет с данными из формы
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('snippets-list')



def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {
        'pagename': 'Просмотр сниппетов',
        'snippets': snippets
        }
    
    return render(request, 'pages/view_snippets.html', context)

def snippet_detail(request, id):
    snippet = Snippet.objects.get(id=id)
    # except ObjectDoesNotExist:
    #     return HttpResponseNotFound(f'Товар c id = {id} не найден')
    # items = Item.objects.all()
    # for item in items:
    #     if item.id == id:
    context = {
        "pagename": "Просмотр сниппета",
        "snippet": snippet
    }
    return render(request, "pages/snippet_detail.html", context)

# def snippet_create(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         lang = request.POST['lang']
#         code = request.POST['code']
#         snippet = Snippet(name=name, lang=lang, code=code)
#         snippet.save()
#         return redirect('snippets-list')
