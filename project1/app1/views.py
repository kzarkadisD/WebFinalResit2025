import json

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from .cart import Cart
from .models import *
from django.db.models import Q, Avg


def home(request):
    # Your view logic here
    return render(request, 'app1/shop.html')  # You should return an HTTP response


def about(request):
    return render(request, 'app1/about.html')

class ProductListView(ListView):
    model = Product
    template_name = 'app1/shop.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['subcategories'] = SubCategory.objects.all()
        return context


def product_search(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        products = Product.objects.all()

    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    return render(request, 'app1/search.html', {'products': products, 'categories': categories, 'subcategories': subcategories})

@csrf_exempt
def submit_rating(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = data.get("item_id")
        rating_value = data.get("rating")

        Rating.objects.create(
            product=Product.objects.get(pk=product_id),
            rating=rating_value,
            user_id=request.user.id
        )
        calculate_avg_rating(product_id)

        return JsonResponse({"success": True})

    return JsonResponse({"success": False}, status=400)

def calculate_avg_rating(product_id):
    avg_rating = (Rating.objects
                  .filter(product=Product.objects.get(pk=product_id))
                  .aggregate(Avg('rating')))
    product = Product.objects.get(pk=product_id)
    product.ratingavg= avg_rating['rating__avg']
    product.save()
    return;
#============== Cart views ==========================================================
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'app1/cart_detail.html', {'cart': cart})

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product)
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')