from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store/',views.Store_page, name='store'),
    path('store/catgory/<slug:category_slug>/', views.Store_page, name='Product catgory'),
    path('store/catgory/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='Product detail'),
    path('search/',views.search, name='search'),
]

