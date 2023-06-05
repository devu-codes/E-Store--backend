from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
# pprint(router.urls)

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

cart_routers = routers.NestedDefaultRouter(router, 'carts', lookup='cart_pk')
cart_routers.register('items', views.CartItemViewSet, basename='cart-items')
# URLConf
urlpatterns = router.urls + product_router.urls + cart_routers.urls

# urlpatterns = [
    # path('products/', views.ProductList.as_view()),
    # path('products/<int:pk>/', views.ProductDetail.as_view()),
    # path('collections/', views.CollectionList.as_view()),
    # path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail'),
# ]
