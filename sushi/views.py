from django.db.models import Prefetch
from django.shortcuts import render

from .models import Menu,Sortirovka


def base(request):

    spisok = []
    # info_dish = Menu.objects.all().prefetch_related(Prefetch('ingredient',queryset=Sortirovka.objects.all().only('name','ingredient','slug','price','weight','image',)))
    info_dish = Menu.objects.all().prefetch_related(Prefetch('ingredient',queryset=Sortirovka.objects.all().only('ingredient_name')))

    # info_dish = Menu.objects.prefetch_related('ingredient').only('name','slug','price','weight','image',)
    print(info_dish)
    for index,value in enumerate(info_dish):
        spisok.append(value)


    # ind = info_dish[0]
    # for i in ind:
    #     print(i)

    # for i in info_dish[0]:
    #     print(i)
    context = {

        'info_dish':info_dish,
        'spisok':spisok,
    }

    return render(request,'sushi/base.html',context)
