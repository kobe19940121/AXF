from django.shortcuts import render

# Create your views here.
from app.models import Wheel, Nav, Mustbuy, Shop, Mainshow


def home(request):
    wheels = Wheel.objects.all()
    navs =  Nav.objects.all()
    mustbuys = Mustbuy.objects.all()
    shops = Shop.objects.all()
    shophead= shops[0]
    shoptabs= shops[1:3]
    shopclass_list = shops[3:7]
    shopcommends = shops[7:11]
    mainshows = Mainshow.objects.all()

    request_dir={
       'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
        'shophead':shophead,
        'shoptabs':shoptabs,
        'shopclass_list':shopclass_list,
        'shopcommends':shopcommends,
        'mainshows':mainshows,


    }
    return render(request,'home/home.html',context=request_dir)


def market(request):
    return render(request,'market/market.html')


def cart(request):
    return render(request,'cart/cart.html')


def mine(request):
    return render(request,'mine/mine.html')