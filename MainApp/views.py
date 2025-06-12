from django.shortcuts import render, HttpResponse

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
    context = {"items": items}
    return render(request, "items.html", context)


def item_page(request, id):
    for item in items:
        if item["id"] == id:
            return render(request, "item.html", item)
