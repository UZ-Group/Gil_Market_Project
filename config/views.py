from django.db.models import Q
from django.shortcuts import render
import random

from Gil_Order.models import Order
from Gil_Product_Brand.models import ProductBrand
from Gil_Products.models import Product
from Gil_Products_Category.models import ProductCategory
from Gil_Sliders.models import Slider, Advertise
from base_user_account.models import User


# header code behind
def header(request, *args, **kwargs):
    firstName = None
    count = 0
    open_order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if request.user.is_authenticated:
        firstName = request.user.first_name
        if open_order:
            for item in open_order.orderdetail_set.all():
                count += 1

    category_list = ProductCategory.objects.all()
    brand = ProductBrand.objects.all()

    context = {
        'firstName': firstName,
        'categoryList': category_list,
        'brand': brand,
        'count': count

    }
    return render(request, 'shared/Header.html', context)


# footer code behind
def footer(request, *args, **kwargs):
    context = {}
    return render(request, 'shared/Footer.html', context)


# code behind
def home_page(request):
    slider = Slider.objects.all()
    advertise = Advertise.objects.first()
    category_list = ProductCategory.objects.all()
    discount = Product.objects.filter(~Q(discount=0), active=True)
    try:
        random_discount = random.sample(list(discount), 3)
    except:
        random_discount = None
    context = {
        'categoryList': category_list,
        'discount': random_discount,
        'sliders': slider,
        'advertise': advertise,

    }
    return render(request, 'home_page.html', context)
