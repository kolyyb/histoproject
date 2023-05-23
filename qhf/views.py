from django.shortcuts import render, get_object_or_404
from .models import Card, Category


def index(request):
    context = {
        "cards": Card.objects.all()


    }
    return render(request, "qhf/index.html", context)


def category_list(request):
    context = {
        "categories": Category.objects.all()
    }
    return render(request, "qhf/category_list.html", context)


def show_card(request, card_id):
    context = {"card": get_object_or_404(Card, pk = card_id)}

    return render(request, "qhf/show_card.html", context)
