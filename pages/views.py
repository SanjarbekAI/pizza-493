from django.shortcuts import render, redirect

from pages.models import ScrollModel, GalleryModel, MenuModel, ReservationModel
from pages.forms import ReservationForm

def home_page_view(request):
    scrolls = ScrollModel.objects.all().order_by('-pk')[:5]
    images = GalleryModel.objects.all().order_by('-pk')
    burgers = MenuModel.objects.filter(category__title__icontains='Burgers').order_by('-pk')
    pizza = MenuModel.objects.filter(category__title__icontains='Pizza').order_by('-pk')
    fries = MenuModel.objects.filter(category__title__icontains='Fries').order_by('-pk')
    salads = MenuModel.objects.filter(category__title__icontains='Salad').order_by('-pk')
    drinks = MenuModel.objects.filter(category__title__icontains='Drinks').order_by('-pk')
    context = {
        "scrolls": scrolls,
        "images": images,
        "burgers": burgers,
        "pizza": pizza,
        "fries": fries,
        "salads": salads,
        "drinks": drinks
    }
    return render(request, 'index.html', context)

def reserve_view(request):
    if request.method == 'POST':
        form = ReservationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:home')
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')

