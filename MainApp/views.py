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
    text = "<h1>Welcome!</h1>"
    return HttpResponse(text)


def about(request):
    text = "Автор: Евгений"
    return HttpResponse(text)


def items_list(request):
    html_result = """
    Список товаров:
    <ul>
    """
    for item in items:
        html_result += f"<li><a href='/item/{item['id']}'> {item['name']}</a></li>"

    html_result += "</ul>"

    return HttpResponse(html_result)

def item_page(request, id):
    for item in items:
        if item["id"] == id:
            html_result = f"""
                <h3>{item['name']}</h3>
                Количество: {item['quantity']}
                """
            return HttpResponse(html_result)















