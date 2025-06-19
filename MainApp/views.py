from MainApp.models import Item
from django.shortcuts import render, HttpResponse, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


# Create your views here.
def home(request):
    context = {
        "name": "Евгений",
        "surname": "Юрченко"
    }
    return render(request, "index.html", context)


def about(request):
    text = "Автор: Евгений"
    return HttpResponse(text)


def items_list(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "items.html", context)


def item_page(request, id):
    # 200 OK
    # 404 NOT FOUND
    try:
        item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Товар с id={id} не найден")
    context = {
        "item": item
    }
    return render(request, "item.html", context)


def item_add(request):
    if request.method == "GET": # страницу с формой
        return render(request, 'create_item.html')
    elif request.method == "POST": # данные от формы
        name = request.POST.get("name")
        brand = request.POST.get("brand")
        count = request.POST.get("count")
        description = request.POST.get("description")

        item = Item(name=name, brand=brand, count=count, description=description)
        item.save()

        return redirect('items-list')
