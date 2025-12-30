from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from cart.models import *
from cart.views import _cart_id
from category.models import Category
from django.db.models import Q

# Create your views here.

def home(request):
    products = Product.objects.all()

    context ={
        'products': products,
    }
    return render(request, 'store/index.html', context)

def Store_page(request, category_slug=None):
    categories = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all()

        product_count = products.count()               # Always defined

        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)



def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = Items.objects.filter(cart__cart_id = _cart_id(request), product = single_product).exists()

    except Exception as e:
        raise e
    context = {
        'single_product': single_product,
        'in_cart' : in_cart
    }
    return render(request, 'store/product-detail.html', context)

def search(request):
    keyword = request.GET.get('Keword')

    if keyword:
        products = Product.objects.filter(
            Q(name__icontains=keyword) |
            Q(description__icontains=keyword)
        )
        product_count = products.count()
    else:
        products = []
        product_count = 0

    context = {
        'products': products,
        'product_count': product_count,
    }

    return render(request, 'store/store.html', context)