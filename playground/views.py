from django.shortcuts import render # render html pages
from django.http import HttpResponse
# from django.core.exceptions import ObjectDoesNotExist
# from django.db.models import Q, F, ExpressionWrapper
# from django.db.models.aggregates import Count, Max, Min, Avg, Sum
# # from store.models import Products, OrderItem, Order, Collection
# from tags.models import TaggedItem
# from django.db.models import DecimalField
# from django.contrib.contenttypes.models import ContentType
# from django.db import transaction
# # Create your views here.
# # request --> response
#
# # @transaction.atomic()
# def say_hello(request):
#     # query_set = Products.objects.all() # for all dataset
#
#     # for product in query_set:
#     #     print(product)
#     # retrieveing data
#     # try:
#     #     product = Products.objects.get(pk=0)
#     # except ObjectDoesNotExist:
#     #     pass
#     # OR
#     # product = Products.objects.filter(pk=0).first() # return None or query set
#     # exist = Products.objects.filter(pk=0).exists() // return bool value
#
#     # Filtering objects
#     # queryset = Products.objects.filter(last_update__year=2021)
#     # Q objects -- using AND, OR
#     # queryset = Products.objects.filter(inventory__lt=10, price__lt=20) # or we can chain filter ops
#     # using Q object
#     # Products: inventory > 20 OR price < 10
#     # queryset = Products.objects.filter(Q(inventory__lt = 10) | Q(price__lt=20))
#     # using F object
#     # queryset = Products.objects.filter(inventory=F('collection__id') )
#     # Sorting
#     # queryset = Products.objects.order_by('price',  '-title').reverse()
#     # select related
#     # queryset = Order.objects.select_related('Customer').order_by('-placed_at')[:5]
#     # ExpressionWrapper
#     # discounted_price = ExpressionWrapper(F('price') * 0.8, output_field= DecimalField() )
#     # queryset = Products.objects.annotate(
#     #     discounted_price=discounted_price
#     # )
#
#     # TaggedItem.objects.get_tags_for(Products, 1);
#
#     # Creating Objects
#     # collection = Collection()
#     # collection.name = 'Video Games'
#     # collection.featured_product = Products(pk=1)
#     # collection.save()
#     # # OR
#     # collection = Collection.objects.create(name='a', featured_product_id=1)
#     # updating Objects
#     # collection = Collection(pk=11)
#     # collection.title = 'Games'
#     # collection.featured_product = None
#     # collection.save()
#     # OR
#     # Collection.objects.filter(pk=11).update(featured_product=None)
#     # # Deleting Objects
#     # collection = Collection(pk=11)
#     # collection.delete()
#
#     # Collection.objects.filter(id__gt=5).delete()
#     # with transaction.atomic():
#     #     order = Order()
#     #     order.customer_id = 1
#     #     order.save()
#
#     #     item = OrderItem()
#     #     item.order = order
#     #     item.product_id = 1
#     #     item.quantity = 1
#     #     item.price = 10
#     #     item.save()
#
#     # Exec raw sql queries
#
#     # queryset = Products.objects.raw('SELECT * from store_product')
#
#
    # return render(request, 'hello.html', {'name': 'Devansh', 'tags': list()})

def say_hello(request):
    return HttpResponse('OK')