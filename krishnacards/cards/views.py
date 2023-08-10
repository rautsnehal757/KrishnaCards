from django.shortcuts import render
from .models import Categories,Cards,Carousel,CardsCategory
# Create your views here.
def home(request):
    mydata = Carousel.objects.all()
    cards = CardsCategory.objects.all()
    print(mydata)
    context = {
        'carousel': mydata,
        'card': cards
    }
    return render(request, "home.html", context)

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def cards_view(request,category_id):
    cat = Categories.objects.get(id=category_id)
    get_cards = Cards.objects.filter(category=category_id)
    context = {"cards":get_cards,"cat":cat}
    return render(request, "cards_view.html",context)

